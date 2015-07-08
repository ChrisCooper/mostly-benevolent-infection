
// Acknowledgments to http://emptypipes.org/2015/02/15/selectable-force-directed-graph/
// for the d3 starting point

var circle_radius = 7.5;

var width = 900;
var height = 900;


var InfectionGraph = function(selector) {

    var graph = this;

    var xScale = d3.scale.linear()
            .domain([0, width])
            .range([0, width]);
    var yScale = d3.scale.linear()
            .domain([0, height])
            .range([0, height]);

    var svg = d3.select(selector)
            .append("svg")
            .attr("width", width)
            .attr("height", height);

    // Source: http://bl.ocks.org/d3noob/5141278
    svg.append("svg:defs").selectAll("marker")
        .data(["end"])      // Different link/path types can be defined here
      .enter().append("svg:marker")    // This section adds in the arrows
        .attr("id", String)
        .attr("viewBox", "0 -5 10 10")
        .attr("refX", 23)
        .attr("refY", 0)
        .attr("markerWidth", 6)
        .attr("markerHeight", 6)
        .attr("orient", "auto")
        .append("svg:path")
        .attr("d", "M0,-4L10,0L0,4")
        .attr("class", "arrow");

    var zoomer = d3.behavior.zoom()
            .scaleExtent([0.01, 10])
            .x(xScale)
            .y(yScale)
            .on("zoom", redraw);

    function redraw() {
        vis.attr("transform",
                "translate(" + d3.event.translate + ")" + " scale(" + d3.event.scale + ")");
    }

    var svg_graph = svg.append('svg:g')
            .call(zoomer);

    var rect = svg_graph.append('svg:rect')
            .attr('width', width)
            .attr('height', height)
            .attr('fill', 'transparent')
            .attr('stroke', 'transparent')
            .attr('stroke-width', 1)
            .attr("id", "zrect");

    var vis = svg_graph.append("svg:g");

    vis.attr('stroke-width', 1)
            .attr('opacity', 0.6)
            .attr('id', 'vis');

    graph.link = vis.append("g")
            .attr("class", "link")
            .selectAll("line");

    graph.node = vis.append("g")
            .attr("class", "node")
            .selectAll("circle");

    graph.drag_ended = function(d) {
        graph.node.filter(function (d) {
            return d.selected;
        })
            .each(function (d) {
                d.fixed &= ~6;
            });

        d.selected = false;
    };

    // Called when the first graph is loaded
    graph.loadGraphData = function(graph_data, app) {

        graph.app = app;

        graph.graph_data = graph_data

        graph_data.links.forEach(function (d) {
            d.source = graph_data.nodes[d.source];
            d.target = graph_data.nodes[d.target];
        });

        graph.link = graph.link.data(graph_data.links).enter().append("line")
            .attr("x1", function (d) {return d.source.x;})
            .attr("y1", function (d) {return d.source.y;})
            .attr("x2", function (d) {return d.target.x;})
            .attr("y2", function (d) {return d.target.y;})
            .attr("marker-end", "url(#end)");


        graph.force = d3.layout.force()
            .charge(-120)
            .linkDistance(30)
            .nodes(graph_data.nodes)
            .links(graph_data.links)
            .size([width, height])
            .start();

        graph.drag_started = function(d, i) {
            d3.event.sourceEvent.stopPropagation();

            // unselect everything
            graph.node.classed("selected", function (p) {
                return p.selected = false;
            });

            d3.select(this).classed("selected", function (p) {
                return d.selected = true;
            });

            // Notify the UI of the selection
            graph.app.nodeWasSelected(i);

            graph.node.filter(function (d) {return d.selected;})
                .each(function (d) {d.fixed |= 2;});
        };

        graph.dragged = function(d) {
            graph.node.filter(function (d) {return d.selected;})
                .each(function (d) {
                    d.x += d3.event.dx;
                    d.y += d3.event.dy;

                    d.px += d3.event.dx;
                    d.py += d3.event.dy;
                });

            graph.force.resume();
        };

        graph.node = graph.node.data(graph_data.nodes).enter().append("circle")
            .attr("r", circle_radius)
            .attr("cx", function (d) {return d.x;})
            .attr("cy", function (d) {return d.y;})
            .on("dblclick", function (d) {
                d3.event.stopPropagation();
            })
            .on("click", function (d, i) {
                if (d3.event.defaultPrevented) return;

                // unselect everything
                graph.node.classed("selected", function (p) {
                    return p.selected = false;
                });

                // always select this node
                d3.select(this).classed("selected", d.selected = true);

                // Notify the UI of the selection
                graph.app.nodeWasSelected(i);
            })


            .call(d3.behavior.drag()
                .on("dragstart", graph.drag_started)
                .on("drag", graph.dragged)
                .on("dragend", graph.drag_ended));

        var clean_center = {x: 300, y: 200};
        var infected_center = {x: -300, y: 0};

        graph.tick = function(e) {
            // Position nodes based on the simulation
            graph.node.attr('cx', function (d) {return d.x;})
                .attr('cy', function (d) {return d.y;});

            // Position edges between nodes
            graph.link.attr("x1", function (d) {return d.source.x;})
                .attr("y1", function (d) {return d.source.y;})
                .attr("x2", function (d) {return d.target.x;})
                .attr("y2", function (d) {return d.target.y;});

            var k = e.alpha * .1;

            // Move nodes apart based on infection
            graph.graph_data.nodes.forEach(function(node) {
                if (node.infected) {
                    node.x += (infected_center.x - node.x) * k;
                    node.y += (infected_center.y - node.y) * k;
                } else {
                    node.x += (clean_center.x - node.x) * k;
                    node.y += (clean_center.y - node.y) * k;
                }
            });

        };
        graph.force.on("tick", graph.tick);
    };

    graph.infect_indices = function(indices) {
        $.each(indices, function( i_index, node_index ) {
            graph.graph_data.nodes[node_index].infected = true;
        });

        graph.node.classed("infected", function (d) {return d.infected;});

        graph.force.resume();

    };
};
