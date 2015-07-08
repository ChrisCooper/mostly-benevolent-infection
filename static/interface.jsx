// The root component
var GraphInterface = React.createClass({
    getInitialState: function () {
        return {
            initial_request_sent: false,
            banner_message: undefined,
            node_is_selected: false
        };
    },

    // Send the graph parameters to the server, and hide the form
    loadGraph: function (graph_params) {
        this.setState({
            initial_request_sent: true,
            banner_message: "Loading graph..."
        });

        var app = this;

        $.post(this.props.graph_url, graph_params, function (data) {
            try {
                var results = $.parseJSON(data);
            }
            catch (e) {
                app.setState({
                    banner_message: "Error loading graph! " + e
                });
                console.log(e);
                return;
            }
            app.setState(results);
            app.setState({
                banner_message: "Scroll to zoom, and click to drag users around! You can also pan."
            });
            app.props.graph.loadGraphData(results, app);
        });
    },

    nodeWasSelected: function(node_index) {
        this.setState({selected_node: node_index, node_is_selected: true});
    },
    infectNode: function(infection_limit) {
        var app = this;
        $.post(
            this.props.infect_url,
            {user_index: this.state.selected_node, limit: infection_limit},
            function (data) {
                try {
                    var infected_indices = $.parseJSON(data);
                    app.props.graph.infect_indices(infected_indices);
                }
                catch (e) {
                    app.setState({
                        banner_message: "Error infecting graph! " + e
                    });
                    console.log(e);
                }
            });
    },
    render: function () {
        var banner = (<div>{this.state.banner_message}</div>);
        var infect_button;

        // Only show the controls if a request hasn't been sent yet
        if (! this.state.initial_request_sent) {
            var controls = (<GraphParameterForm interface={this}/>);
        } else if (this.state.node_is_selected) {
            var selected_email = this.state.nodes[this.state.selected_node].email;
            infect_button = <InfectButton app={this} selected_email={selected_email} />
        } else {
            infect_button = <InfectButton app={this} />
        }

        return (
            <div className="graph-interface">
                <div className="controls">
                    {controls}
                </div>
                <div className="banner-message">
                    {banner}
                </div>
                {infect_button}
            </div>
        );
    }
});

// User submits this to actually load a graph
var GraphParameterForm = React.createClass({
    handleSubmit: function (e) {
        e.preventDefault();
        var num_schools = React.findDOMNode(this.refs.num_schools).value.trim();
        var num_classes = React.findDOMNode(this.refs.num_classes).value.trim();

        this.props.interface.loadGraph({
            num_schools: num_schools,
            num_classes: num_classes
        });
    },
    render: function () {
        return (
            <form onSubmit={this.handleSubmit}>
                # of schools:
                <input type="text" placeholder="1 to 10" ref="num_schools"/>
                classes per school:
                <input type="text" placeholder="1 to 20" ref="num_classes"/>
                <input type="submit" value="Generate Graph"/>
            </form>
        );
    }
});

var InfectButton = React.createClass({
    handleClick: function (e) {
        var infection_limit = React.findDOMNode(this.refs.infection_limit).value.trim();
        this.props.app.infectNode(infection_limit);
    },
    render: function () {
        var button;
        if (this.props.selected_email) {
            button = (
                <button onClick={this.handleClick} ref="button">Infect {this.props.selected_email}!</button>
            );
        } else {
            button = (
                <button disabled onClick={this.handleClick} ref="button">Select a user to infect first</button>
            );
        }

        return(
            <div>
                {button}
                <input type="text" placeholder="optional infection limit" ref="infection_limit"/>
            </div>
        );
    }
});

var infection_graph = new InfectionGraph("#d3_graph_root");

React.render(
    <GraphInterface
        graph_url="/graph"
        infect_url="/infect"
        graph={infection_graph}
    />,
    $("#container")[0]
);