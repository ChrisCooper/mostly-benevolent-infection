from flask import Flask, render_template, request
import json

from graph_generation import new_school, new_classroom
from infection import infect
from limited_infection import limited_infect

app = Flask(__name__)

# The *ahem*... global graph
graph = []


@app.route('/')
def visualization():
    """The main React app for displaying the graph and controls"""
    return render_template('visualization.html')


@app.route('/graph', methods=['POST'])
def reset_graph():
    """Resets THE graph based on parameters"""
    global graph

    num_schools = dict_int(request.form, 'num_schools', 5)
    num_classes = dict_int(request.form, 'num_classes', 10)

    class_gen = lambda: new_classroom(10, variation_coeff=1)
    schools = [new_school(num_classes, 0.5, class_gen, extra_coaching_rate=0.1) for i in range(num_schools)]

    # flatten schools list
    graph = [user for school in schools for user in school]

    return users_to_graph_json(graph)

def dict_int(dic, key, default):
    """Get an int from the dict or a default value"""
    try:
        return int(dic.get(key, default))
    except ValueError:
        return default

def users_to_graph_json(users):
    """Generate nodes and links json for the given users"""
    # Hard-coding of infected status here is ugly
    user_data = [{'infected': (u.site_version == 2), 'email': u.email} for u in users]

    links = []

    # build an index of the users, since we need to refer to indices
    index_of_users = {u: i for (i, u) in enumerate(users)}

    for user_idx, user in enumerate(users):
        for coach in user.coach_set:
            links.append({'source': index_of_users[coach], 'target': user_idx})

    return json.dumps({'nodes': user_data, 'links': links})


@app.route('/infect', methods=['POST'])
def infect_user():
    """Infects and returns the victim indices"""

    index = int(request.form['user_index'])

    # hardcoding version here is ugly
    #infect(graph[index], 2)
    limited_infect(graph[index], 2, 50)

    infected_indices = filter(lambda i: graph[i].site_version == 2, range(len(graph)))

    return json.dumps(infected_indices)

if __name__ == '__main__':
    app.run(debug=True)
