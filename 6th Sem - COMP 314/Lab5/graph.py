import collections
import time
import random
from pprint import pformat
from tabulate import tabulate


import matplotlib.pyplot as plt
import networkx as nx


class Graph:
    """ """

    _graph = None
    no_of_nodes = None
    no_of_edges = None
    longest_short_path_info = None

    def __init__(self, relative_filepath: str, edge_data: tuple = None):
        self._import_graph(relative_filepath, edge_data)
        self.no_of_nodes = self._graph.number_of_nodes()
        self.no_of_edges = self._graph.number_of_edges()

    def _get_all_pairs_shortest_path_dict(self, start_node=None, end_node=None):
        """
        Method to get all the shortest paths.
        Shortest path is the path with shortest distance between two vertices.

        Returns a dict where
        index (start node) : {
            end node 1 : [path from start to end],
            end node 2 : [path from start to end],
            and so on
            }
        """
        return dict(nx.all_pairs_dijkstra_path(self._graph))

    def _get_all_pairs_shortest_path_length_dict(self, start_node=None, end_node=None):
        """
        Method to get all the lengths of the shortest paths.
        Shortest path is the path with shortest distance between two vertices

        Returns a dict where
        index (start node) : {
            end node 1 : length from start to end,
            end node 2 : length from start to end,
            and so on
            }
        """
        return dict(nx.all_pairs_dijkstra_path_length(self._graph))

    def _import_graph(self, relative_filepath: str, edge_data: tuple = None):
        """Import graph from a edgelist file"""

        self._graph = nx.read_edgelist(
            relative_filepath,
            nodetype=int,
            data=(edge_data),
        )

    def _check_connected(self):
        """Check whether graph is connected graph"""

        return nx.is_connected(self._graph)

    def display_graph(self):
        """Display Network Graph"""

        nx.draw(self._graph, alpha=0.4)
        plt.show()

    def display_degree_distribution_scatterplot(self):
        """Display Scatterplot for Degree Distribution"""

        degrees, frequency = self.degree_distribution()
        colors = [random.randint(0, 1000) / 1000 for _ in range(len(degrees))]
        area = [100] * len(degrees)
        plt.title("Graph degree distribution Scatter plot")
        plt.xlabel("Degrees")
        plt.ylabel("Frequency")
        plt.scatter(degrees, frequency, s=area, c=colors, alpha=0.5)
        plt.show()

    def average_degree(self):
        """
        Average degree is simply the average number of edges per node in the graph.
        """

        return round((self.no_of_edges / self.no_of_nodes), 5)

    def clustering_coefficient(self):
        """
        In graph theory, a clustering coefficient is a measure of the degree
        to which nodes in a graph tend to cluster together.

        Returns average clustering coefficient : float
        """
        G = self._graph

        clusters_coeffs = []

        for node in G.nodes():
            # neighbors of a node
            neighbors = [neighbor for neighbor in G.neighbors(node)]
            sub_graph = nx.subgraph(G, neighbors)  # get subgraph of each neighbor
            Ki = len(neighbors)  # number of neighbors
            Ei = sub_graph.number_of_edges()  # no of edges of neighbor's subgraph
            # calculate clustering coefficients for clusters of size > 1
            Ci = (2 * Ei) / (Ki * (Ki - 1)) if Ki > 1 else 0
            clusters_coeffs.append(Ci)

        # return the average clustering coefficient
        return round(sum(clusters_coeffs) / len(clusters_coeffs), 5)

    def degree_distribution(self):
        """
        Distribution of degrees in the graph

        Return list of degrees, list of frequency of corresponding degrres :tuple
        """

        degrees_sequence = sorted([d for n, d in self._graph.degree()], reverse=True)

        degrees_count = collections.Counter(degrees_sequence)
        degrees, count = zip(*degrees_count.items())

        return list(degrees), list(count)

    def density(self) -> float:
        """
        Ratio of the number of edges to the number of possible
        edges in a network, given by

        Returns density: float
        """

        V = self.no_of_nodes
        E = self.no_of_edges

        return 0 if abs(V) < 1 else round((2 * E) / (V * (V - 1)), 5)

    def diameter(self):
        """
        Diameter is the largest number of vertices which must be traversed in order to
        travel from one vertex to another when paths which backtrack, detour, or
        loop are excluded from consideration.

        Returns diameter: int
        """
        if not self._check_connected():
            return "Graph not connected"

        if self.longest_short_path_info == None:
            self.longest_short_path()

        return len(self.longest_short_path_info["path"]) - 1

    def longest_short_path(self):
        """
        Method to calculate the longest of the shortest paths

        Returns {'starting_node': int, 'ending_node': int, 'path': list, 'weighted_distance': int} : dictionary
        """
        if not self._check_connected():
            return "Graph not connected"

        if self.longest_short_path_info == None:
            paths = self._get_all_pairs_shortest_path_dict()  # all the shortest paths
            lengths = (
                self._get_all_pairs_shortest_path_length_dict()
            )  # length of the shortest paths

            longest = 0  # for comapring length of the shortest paths
            longest_short_path = None  # store longest short path based on the length
            longest_short_path_length = None  # store length of the longest short path
            longest_short_path_info = dict()  # for final information

            # iterating through shortest path lengths
            for (start_node, end_nodes) in lengths.items():
                # iterating through endnodes
                for (end_node, length) in end_nodes.items():
                    # compare and assign longest
                    if length > longest:
                        longest = length
                        longest_short_path = dict(
                            starting_node=start_node,
                            ending_node=end_node,
                            path=paths[start_node][end_node],
                        )
                        longest_short_path_length = dict(
                            weighted_distance=end_nodes[end_node]
                        )

            longest_short_path_info.update(longest_short_path)
            longest_short_path_info.update(longest_short_path_length)
            self.longest_short_path_info = longest_short_path_info

        return self.longest_short_path_info

    def show_properties(self):

        # d = self.display_degree_distribution_scatterplot()
        time.sleep(1)

        head = ["Property", "Value", "Library Value"]

        data = [
            ["No. of Nodes", self.no_of_nodes, self._graph.number_of_nodes()],
            ["No. of Edges", self.no_of_edges, self._graph.number_of_edges()],
            ["Average Degree", self.average_degree(), "-"],
            ["Density", self.density(), round(nx.density(self._graph), 5)],
            [
                "Diameter",
                self.diameter(),
                nx.diameter(self._graph) if nx.is_connected(self._graph) else "-",
            ],
            [
                "Longest Shortest Path",
                pformat(self.longest_short_path(), sort_dicts=False),
                "-",
            ],
            [
                "Clustering coefficients",
                self.clustering_coefficient(),
                round(nx.average_clustering(self._graph), 5),
            ],
        ]

        print("####################")
        print("# GRAPH PROPERTIES #")
        print("####################")
        print(tabulate(data, headers=head, tablefmt="fancy_grid"))


def show_graph_info(relative_filepath: str, edge_data: tuple = None):
    graph = Graph(relative_filepath, edge_data)
    graph.show_properties()
    graph.display_graph()
    graph.display_degree_distribution_scatterplot()


if __name__ == "__main__":

    # Small
    show_graph_info("data/mammalia-voles-bhp-trapping-55.edges", (("weight", int),))

    # Large
    show_graph_info("data/inf-euroroad.edges", ())
    show_graph_info("data/as-735.mtx", ())
    show_graph_info("data/bio-dmela.mtx", ())
    show_graph_info("data/ca-Erdos992.mtx", ())
    show_graph_info("data/DD21.edges", ())
    show_graph_info("data/Erdos02.mtx", ())
