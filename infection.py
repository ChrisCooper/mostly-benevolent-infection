"""
The infection algorithm proper is implemented here.
"""

import itertools

import models

def infect(user, new_site_version):
    """
    Perform a breadth-first-ish expansion from the given user, updating all with the new site version

    :returns the number of users infected
    """
    if user is None:
        raise ValueError('User to infect cannot be None')

    if not isinstance(user, models.User):
        raise TypeError('User to infect must be a models.User instance')

    num_infected = 0

    for user in all_connected_nodes(start=user):
        user.site_version = new_site_version
        num_infected += 1

    return num_infected

def all_connected_nodes(start):
    # A set is used here because the order doesn't matter
    nodes_to_visit = set([start])
    nodes_visited = set()

    # Pop from the set until we've visited everything
    while len(nodes_to_visit) > 0:
        node = nodes_to_visit.pop()
        nodes_visited.add(node)

        # Add connected learners and coaches for this node
        for u in itertools.chain(node.coach_set, node.learner_set):
            if u not in nodes_visited:
                nodes_to_visit.add(u)

        yield node

