from flask import Flask, render_template, request
import json

from graph_generation import new_school, new_classroom

app = Flask(__name__)

# The *ahem*... global graph
graph = []


@app.route('/')
def visualization():
    """
    The main React app for displaying the graph and controls
    """
    return render_template('visualization.html')


@app.route('/graph', methods=['POST'])
def reset_graph():
    """
    Resets THE graph based on parameters
    """
    global graph

    # todo: extract parameters

    class_gen = lambda: new_classroom(25)
    graph = new_school(3, 1, class_gen)

    return users_to_graph_json(graph)


def users_to_graph_json(users):
    # todo: really encode users and links
    return json.dumps({
        "users": [
            {
                "site_version": 1,
                "email": "me@site.com"
            },
            {
                "site_version": 1,
                "email": "you@site.com"
            }],
        "links": [
            {
                "source": 0,
                "target": 1
            }
        ]
    })


if __name__ == '__main__':
    app.run()
