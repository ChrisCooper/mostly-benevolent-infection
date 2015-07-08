var GraphInterface = React.createClass({
    render: function () {
        return (
            <div className="graph-interface">
                <Controls />
                <Graph />
            </div>
        );
    }
});


var Controls = React.createClass({
    render: function () {
        return (
            <div className="controls">
                Controls
            </div>
        );
    }
});


var Graph = React.createClass({
    render: function () {
        return (
            <div id="graph-d3-root" className="d3-graph">
                Graphs
            </div>
        );
    }
});

React.render(
    <GraphInterface />,
    $("#container")[0]
);