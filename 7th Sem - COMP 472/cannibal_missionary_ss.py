"""Generating State Space of the Missionary Cannibal Problem"""

import networkx as nx
import matplotlib.pyplot as plt


class StateSpace(nx.Graph):
    """ """

    graph = None
    current_node = None
    added_state_list = []
    devour_state_list = []

    def __init__(self):
        """
        Initialize graph with initial state (3,3,False) and number of node 1
        """

        self.graph = nx.Graph()
        self.current_node = 0
        self.add_state_node(0, 3, 3, False)

    def add_state_node(
        self, parent: int, missionary: int, cannibal: int, boat_crossed: bool
    ):
        """
        Adds node and edge to graph with parameterized attributes

        Parameters
        ----------
        parent : int
            the parent node i.e the previous state

        missionary : int
            the number of missionaries present at the left side

        cannibal : int
            the number of cannibals present at the left side

        boat_crossed : bool
            whether the boat crossed (true if at right, false if at left)

        Raises
        ------
        AssertionError
            raises assertion error for
            if boat_crossed is not a boolean
        """

        assert isinstance(boat_crossed, bool)

        if missionary <= 3 and cannibal <= 3:

            if (missionary, cannibal, boat_crossed) == (0, 0, True):
                color = "green"
            elif (missionary, cannibal, boat_crossed) == (3, 3, False):
                color = "orange"
            elif missionary < cannibal:
                color = "red"
            else:
                color = "blue"

            # add node
            self.graph.add_node(
                self.current_node,
                missionary=missionary,
                cannibal=cannibal,
                boat_crossed=boat_crossed,
                color=color,
            )

            # add edge
            if self.current_node != 0:
                direction = "left" if not boat_crossed else "right"
                self.graph.add_edge(
                    parent,
                    self.current_node,
                    edge_data=f"{missionary}m{cannibal}c {direction}",
                )

            # increment node count and add to added states
            self.current_node += 1
            self.added_state_list.append((missionary, cannibal, boat_crossed))

    def add_states(self, parent: int, states: list):
        """
        Add states to the graph from a list of tuples

        Parameteres
        -----------
        states: list
            A list containing a tuple of states (Eg. (2,1,False))

        """
        for state in states:
            if state not in self.added_state_list:
                self.add_state_node(parent, *state)

    def generate_possible_states(self, node: int):
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
            A list containing tuples of all possible states

        Examples
        --------
        >>> self.graph.nodes[1]

        `{'misisonary':3, 'cannibals':3, 'boat_crossed':False}`

        >>> self.generate_possible_states(1)

        generates states as tuple, in given example,
        (1,3,True), (2,3,True), (3,1,True), (3,2,True), (2,2,True)
        then adds these as nodes for the graph with edges connected to 1 ie (3,3,False)
        """
        states = []
        seed_node = self.graph.nodes[node]
        miss, cann, cross, color = tuple(seed_node.values())

        # check goal state
        if (miss, cann, cross) == (0, 0, False):
            return

        # if parent state has not crossed ie is at left side ie False
        # then carries out difference, because moving right decreases people in left

        if not cross:
            if miss != cann != 0 and miss < cann:
                self.devour_state_list.append((miss, cann, cross))
                return []

            # move only missionaries
            if 0 < miss <= 3:
                states += (
                    [(miss - 1, cann, not cross)]
                    if miss == 1
                    else [(miss - 2, cann, not cross), (miss - 1, cann, not cross)]
                )
            # move only cannibals
            if 0 < cann <= 3:
                states += (
                    [(miss, cann - 1, not cross)]
                    if cann == 1
                    else [(miss, cann - 2, not cross), (miss, cann - 1, not cross)]
                )
            # move both
            if miss >= 1 and cann >= 1:
                states += [(miss - 1, cann - 1, not cross)]

        # When at right side
        else:
            right_miss, right_cann = 3 - miss, 3 - cann

            if right_miss != right_cann != 0 and right_miss < right_cann:
                self.devour_state_list.append((miss, cann, cross))
                return []

            # move only missionaries
            if 0 < right_miss <= 3:
                states += (
                    [(miss + 1, cann, not cross)]
                    if right_miss == 1
                    else [(miss + 2, cann, not cross), (miss + 1, cann, not cross)]
                )
            # move only cannibals
            if 0 < right_cann <= 3:
                states += (
                    [(miss, right_cann + 1, not cross)]
                    if right_cann == 1
                    else [(miss, cann + 2, not cross), (miss, cann + 1, not cross)]
                )
            # move both
            if right_miss >= 1 and right_cann >= 1:
                states += [(miss + 1, right_cann + 1, not cross)]

        return states

    def generate_state_space(self):
        """
        Generate the State Space for the Missionary Cannibal problem
        by traversing in BFS manner by visiting neighbour nodes in sequence
        """
        traverse_nodes = [0]
        visited = []
        # find states until goal state is found
        while len(traverse_nodes) != 0:
            successor_states = self.generate_possible_states(traverse_nodes[0])
            self.add_states(traverse_nodes[0], successor_states)

            unvisited_neighbors = set(
                self.graph.neighbors(traverse_nodes[0])
            ).difference(set(visited))

            traverse_nodes += list(unvisited_neighbors)
            visited.append(traverse_nodes.pop(0))

    def draw_graph(self):
        """
        Draw the State Space Graph
        """
        node_labels1 = list(nx.get_node_attributes(self.graph, "missionary").values())
        node_labels2 = list(nx.get_node_attributes(self.graph, "cannibal").values())
        node_labels3 = list(nx.get_node_attributes(self.graph, "boat_crossed").values())

        labels = {}
        for i in range(0, len(node_labels1)):
            labels[i] = f"{node_labels1[i],node_labels2[i],node_labels3[i]}"
        edge_labels = nx.get_edge_attributes(self.graph, "edge_data")
        colors = [node[1]["color"] for node in self.graph.nodes(data=True)]

        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos)
        nx.draw_networkx_nodes(self.graph, pos, node_color=colors, node_size=3000)
        nx.draw_networkx_edge_labels(
            self.graph, pos, font_size=8, edge_labels=edge_labels
        )
        nx.draw_networkx_labels(
            self.graph,
            pos,
            font_size=8,
            labels=labels,
            font_color="white",
            font_family="monospace",
        )
        plt.show()


if __name__ == "__main__":
    ss = StateSpace()
    ss.generate_state_space()
    ss.draw_graph()
