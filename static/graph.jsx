// The root component. Has a control section and a graph section
var GraphInterface = React.createClass({
    getInitialState: function () {
        return {
            initial_request_sent: false,
            banner_message: undefined,
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
                app.setState(results);
            }
            catch (e) {
                app.setState({
                    banner_message: "Error loading graph! " + e
                });
                console.log(e);
            }
        });
    },
    render: function () {
        var banner = (<div>{this.state.banner_message}</div>);

        // Only show the controls if a request hasn't been sent yet
        if (! this.state.initial_request_sent) {
            var controls = (<GraphParameterForm interface={this}/>);
        }

        return (
            <div className="graph-interface">
                <div className="controls">
                    {controls}
                </div>
                <div className="banner-message">
                    {banner}
                </div>
                <Graph />
            </div>
        );
    }
});

// User submits this to actually load a graph
var GraphParameterForm = React.createClass({
    handleSubmit: function (e) {
        e.preventDefault();
        var num_classes = React.findDOMNode(this.refs.num_classes).value.trim();
        var class_size = React.findDOMNode(this.refs.class_size).value.trim();

        this.props.interface.loadGraph({
            num_classes: num_classes,
            class_size: class_size
        });
    },
    render: function () {
        return (
            <form onSubmit={this.handleSubmit}>
                # of classes:
                <input type="text" placeholder="1 to 25" ref="num_classes"/>
                Average class size:
                <input type="text" placeholder="1 - 30" ref="class_size"/>
                <input type="submit" value="Generate Graph"/>
            </form>
        );
    }
});

// This component is mostly a container for d3's SVG
var Graph = React.createClass({
    render: function () {
        return (
            <div id="graph-d3-root" className="d3-graph">
                Graph
            </div>
        );
    }
});


React.render(
    <GraphInterface graph_url="/graph" />,
    $("#container")[0]
);