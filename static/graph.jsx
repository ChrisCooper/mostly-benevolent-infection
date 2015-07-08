var GraphInterface = React.createClass({
    loadGraph: function(graph_params) {
        console.log("loading graph!");
    },
    render: function () {
        return (
            <div className="graph-interface">
                <Controls interface={this} />
                <Graph />
            </div>
        );
    }
});


var Controls = React.createClass({
    handleSubmit: function(e) {
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
            <div className="controls">
                <form onSubmit={this.handleSubmit}>
                    <input type="text" placeholder="# of classes (e.g. 10)" ref="num_classes" />
                    <input type="text" placeholder="Class size" ref="class_size" />
                    <input type="submit" value="Generate Graph" />
                </form>
            </div>
        );
    }
});


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
    <GraphInterface />,
    $("#container")[0]
);