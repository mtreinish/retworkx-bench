# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import random
import itertools

import retworkx


class GraphAdjacencyMatrixBenchmarks:

    params = ([10, 100, 1000, 10000, 100000], [10, 100, 1000, 10000, 100000])
    param_names = ["Number of Nodes", "Number of Edges"]

    def setup(self, num_nodes, num_edges):
        random.seed(1234)
        self.graph = retworkx.undirected_gnm_random_graph(
            num_nodes, num_edges, seed=4242
        )
        for edge in self.graph.edge_indices():
            self.graph.update_edge_by_index(edge, random.randint(0, 20000))

    def time_adjacency_matrix(self, _, __):
        retworkx.graph_adjacency_matrix(self.graph, weight_fn=float)

    def peakmem_adjacency_matrix(self, _, __):
        retworkx.graph_adjacency_matrix(self.graph, weight_fn=float)


class DiGraphAdjacencyMatrixBenchmarks:

    params = (
        [10, 100, 1000, 10000, 100000],
        [10, 100, 1000, 10000, 100000],
        [False, True],
    )
    param_names = ["Number of Nodes", "Number of Edges", "Removed Nodes"]

    def setup(self, num_nodes, num_edges, remove_nodes):
        random.seed(12345)
        self.graph_func = retworkx.digraph_adjacency_matrix
        self.graph = retworkx.directed_gnm_random_graph(num_nodes, num_edges, seed=4242)
        for edge in self.graph.edge_indices():
            self.graph.update_edge_by_index(edge, random.randint(0, 20000))

    def time_adjacency_matrix(self, _, __, ___):
        self.graph_func(self.graph, lambda x: x)

    def peakmem_adjacency_matrix(self, _, __, ___):
        self.graph_func(self.graph, lambda x: x)
