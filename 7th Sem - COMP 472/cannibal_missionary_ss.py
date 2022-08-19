"""
Generating State Space of the Missionary-Cannibal Problem

Author: Sambeg Shrestha
License: MIT
Created: 17 Aug, 2022
"""

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from networkx.drawing.nx_agraph import graphviz_layout


class StateSpace(nx.Graph):
    """
    Initialize an object to find the State Space of
    the Missionary Cannibals problems using a Directed Graph
    implemented using NetworkX(https://networkx.org/)

    Attributes
    ----------
    graph: networkx.DiGraph
        A directed graph implementation using networkx

    current_node: int
        For keeping track of the number of nodes currently
        in the graph

    added_state_list: list
        For keeping track of states(tuples) present in the graph.
        Example, [(3,3,1),] present during initialization

    devour_state_list: list
        For keeping track of invalid/devour states for the problem.
        A state is invalid if the number of cannibals are greater
        than missionary.
        Example, [(1,3,0),]
    """

    graph = None
    current_node = None
    added_state_list = []
    devour_state_list = []

    def __init__(self):
        """
        Initialize graph with initial state (3,3,1) and node id 0
        """

        start_state = [np.array([3, 3, 1])]

        self.graph = nx.DiGraph()
        self.current_node = 0
        self._add_state_node(0, start_state)

    #########################
    #       PRIVATE
    #########################

    def _check_state_return_color(self, state: np.array):
        """
        Checks the state of a given np.array if it is valid, invalid,
        goal or starting

        Returns
        -------
        state: np.array or None
            the verified state

        color: str or None
            string of color either red, blue, green, orange
        """

        miss, cann, cross = state
        if 0 <= miss <= 3 and 0 <= cann <= 3:
            # check state
            if (miss, cann, cross) == (0, 0, 0):  # goal state
                return state, "green"

            elif (miss, cann, cross) == (3, 3, 1):  # start state
                return state, "orange"

            elif miss != 0 and cann != 0 and miss < cann:  # killed state
                self.devour_state_list.append(tuple(state))
                return state, "red"

            else:  # valid state
                return state, "blue"

        return None, None

    def _add_state_node(self, parent: int, state_action: list):
        """
        Adds node and edge to graph with parameterized attributes

        Parameters
        ----------
        parent : int
            id of parent node i.e the previous state

        state_action : list
            list matrix of containing state and action performed
            to obtain state.
            Uses first value to create nodes and second for edges.
            Example, [array([2,3,0]), array([1,1,-1])]
        """

        current = self.current_node
        confirmed_state, color = self._check_state_return_color(state_action[0])
        if confirmed_state is not None:
            # add node
            self.graph.add_node(current, state=confirmed_state, color=color)
            # add edge
            self.graph.add_edge(
                parent, current, edge_data=state_action[1]
            ) if current != 0 else None

            # increment node count and add to added states
            self.current_node += 1
            self.added_state_list.append(tuple(confirmed_state))

    def _add_states(self, parent: int, states: list):
        """
        Add states to the graph from a list of tuples

        Parameteres
        -----------
        states: list
            Contains matrices of states and actions performed to
            obtained state
            Example, [[array([2,3,0]), array([1,1,-1])], ...]
        """
        if states:
            for state_actions in states:
                if tuple(state_actions[0]) in self.added_state_list:
                    continue
                self._add_state_node(parent, state_actions)

    def _generate_possible_states(self, node: int):
        """
        Generates states to the state space graph depending on the
        attributes of a seed node

        Parameters
        ----------
        node : int
            The position of the seed node in the graph

        Returns
        -------
        states: list
            A list containing np.arrays of all possible states

        Examples
        --------
        >>> self.graph.nodes[1]

        `1: {'states': array([3,3,1]), 'color':'orange'}`

        >>> self._generate_possible_states(1)

        generates states as numpy array ie matrix, in given example,
        array([1,3,1]), ... etc. and returns it
        """

        seed_node = self.graph.nodes[node]
        seed_state, _ = tuple(seed_node.values())
        state_n_action, possible = [], []
        miss, cann, left = seed_state

        if tuple(seed_state) == (0, 0, 0):
            return
        elif tuple(seed_state) in self.devour_state_list:
            return

        # LEFT SIDE
        if left == 1:
            # move only missionaries
            if 0 < miss <= 3:
                possible += (
                    [np.array([-1, 0, -1]), np.array([-2, 0, -1])]
                    if miss > 1
                    else [np.array([-1, 0, -1])]
                )
            # move only cannibals
            if 0 < cann <= 3:
                possible += (
                    [np.array([0, -1, -1]), np.array([0, -2, -1])]
                    if cann > 1
                    else [np.array([0, -1, -1])]
                )
            # move both
            if miss >= 1 and cann >= 1:
                possible += [np.array([-1, -1, -1])]

        # RIGHT SIDE
        else:
            right_miss, right_cann = 3 - miss, 3 - cann
            # move only missionaries
            if 0 < right_miss <= 3:
                possible += (
                    [np.array([1, 0, 1]), np.array([2, 0, 1])]
                    if right_miss > 1
                    else [np.array([1, 0, 1])]
                )
            # move only cannibals
            if 0 < right_cann <= 3:
                possible += (
                    [np.array([0, 1, 1]), np.array([0, 2, 1])]
                    if right_cann > 1
                    else [np.array([0, 1, 1])]
                )
            # move both
            if right_miss >= 1 and right_cann >= 1:
                possible += [np.array([1, 1, 1])]

        for state in possible:
            state_n_action.append([seed_state + state, state])

        return state_n_action

    #########################
    #       PUBLIC
    #########################

    def generate_state_space(self):
        """
        Generate the State Space for the Missionary Cannibal problem
        by traversing in BFS manner by visiting neighbour nodes in sequence
        """

        traverse_nodes, visited = [0], []

        # traverse and create states until goal state is found
        while len(traverse_nodes) != 0:

            # find successor states and add to graph
            successor_states = self._generate_possible_states(traverse_nodes[0])
            self._add_states(traverse_nodes[0], successor_states)

            # find neighbour nodes that have not been already visited
            unvisited_neighbors = set(
                self.graph.neighbors(traverse_nodes[0])
            ).difference(set(visited))
            traverse_nodes += list(unvisited_neighbors)
            visited.append(traverse_nodes.pop(0))

    def draw_graph(self):
        """
        Draw the State Space Graph using matplotlib
        """

        # defining labels and colors
        node_ids = nx.nodes(self.graph)
        node_labels = nx.get_node_attributes(self.graph, "state")
        edge_labels = nx.get_edge_attributes(self.graph, "edge_data")
        colors = [node[1]["color"] for node in self.graph.nodes(data=True)]

        labels = {}
        for id, _ in enumerate(node_ids):
            labels[id] = f"{id}\n{node_labels[id]}"

        # display graph properties
        nx.nx_agraph.write_dot(self.graph, "test.dot")
        pos = graphviz_layout(self.graph, prog="dot")
        nx.draw(self.graph, pos)
        nx.draw_networkx_nodes(self.graph, pos, node_color=colors, node_size=3000)
        nx.draw_networkx_edge_labels(
            self.graph, pos, font_size=8, edge_labels=edge_labels
        )
        nx.draw_networkx_labels(
            self.graph,
            pos,
            font_size=10,
            labels=labels,
            font_color="white",
            font_family="monospace",
            font_weight="bold",
        )

        # show plot
        plt.show()


# Driver Code
if __name__ == "__main__":
    ss = StateSpace()
    ss.generate_state_space()
    ss.draw_graph()
