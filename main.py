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

    user_data = [{'site_version': u.site_version, 'email': u.email} for u in users]

    links = []

    # build an index of the users, since we need to refer to indices
    index_of_users = {u: i for (i, u) in enumerate(users)}

    for user_idx, user in enumerate(users):
        for coach in user.coach_set:
            links.append({'source': index_of_users[coach], 'target': user_idx})

    return json.dumps({'nodes': user_data, 'links': links})


if __name__ == '__main__':
    app.run(debug=True)
