"""
The limited infection algorithm is implemented here.
"""
from heapq import *

import itertools

def limited_infect(starting_user, new_site_version, num_users):
    """
    Currently infects exactly the specified num_users with the new site version.
    With more time, could also take a min and max and find a more optimal infection.

    This greedy algorithm aims to minimize outgoing edges from the infected
    partition by expanding to nodes of low partition-leaving degree and high
    partition-internal degree first.
    """

    # This implementation is a little messy, with lots of sets and dicts floating around.
    # Implementing a more complete priority queue first would make things much better
    # Desired features include;
    # - having a comparison key function
    # - deleting nodes efficiently

    num_infected = 0
    nodes_infected = set()

    # The users in the heap are stored as (priority, user) so they sort
    # priority = num_partition_external_connections - num_partition_internal_connections
    next_nodes = [(0, starting_user)]
    heapify(next_nodes)
    node_priorities = {starting_user: 0}

    # Add connected nodes by priority
    while len(next_nodes) > 0 and num_infected < num_users:
        priority, next_user = heappop(next_nodes)

        # Skip nodes that were already removed with a better priority
        # These extra entries aren't deleted
        if next_user not in node_priorities:
            continue

        # remove the user from node_priorities to signify its deletion
        del(node_priorities[next_user])

        # infect the node
        next_user.site_version = new_site_version
        nodes_infected.add(next_user)
        num_infected += 1

        # Add the connected nodes for infection consideration
        update_from_user_connections(next_nodes, next_user, node_priorities, nodes_infected)

    return num_infected

def update_from_user_connections(queue, new_user, node_priorities, nodes_infected):
    """Adds connected useres to the queue according to priority"""
    for u in users_connections(new_user):
        # no need to add already infected nodes
        if u in nodes_infected:
            continue

        # Check if this node is already in the queue
        if u in node_priorities:
            # Update its priority

            node_priorities[u] -= 1
            priority = node_priorities[u]

            # Add a new entry
            heappush(queue, (priority, u))
        else:
            # Add an entry in both the priorities and queue
            priority = user_priority(u, nodes_infected)
            node_priorities[u] = priority
            heappush(queue, (priority, u))


def user_priority(user, nodes_infected):
    """
    A user's prioirity for being infected is the difference between its
    number of uninfected neighbour and its number of infected neighbours.
    """
    priority = 0
    for u in users_connections(user):
        if u in nodes_infected:
            priority -= 1
        else:
            priority += 1

    return priority

def users_connections(user):
    return itertools.chain(user.learner_set, user.coach_set)