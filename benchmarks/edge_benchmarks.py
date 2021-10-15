# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import itertools

import retworkx


class GraphAddEdgesBenchmarks:

    params = (
        [1, 10, 100, 1000, 10000, 100000, 1000000],
        [1, 10, 100, 1000, 10000, 100000, 1000000],
    )
    param_names = ["Number of Nodes", "Number of Edges"]

    def setup(self, num_nodes, num_edges):
        self.graph = retworkx.PyGraph()
        nodes = self.graph.add_nodes_from(list(range(num_nodes)))
        self.list_empty = []
        self.list_obj = []
        node_ids = itertools.cycle(nodes)
        for i in range(num_edges):
            node_a = next(node_ids)
            node_b = next(node_ids)
            self.list_empty.append((node_a, node_b))
            self.list_obj.append((node_a, node_b, i))

    def time_graph_add_edges_from(self, _, __):
        self.graph.add_edges_from(self.list_obj)

    def time_graph_add_edges_from_no_data(self, _, __):
        self.graph.add_edges_from_no_data(self.list_empty)

    def time_graph_add_edges_loop(self, _, __):
        for i in self.list_obj:
            self.graph.add_edge(i[0], i[1], i[2])


class DiGraphAddEdgesBenchmarks:

    params = (
        [1, 10, 100, 1000, 10000, 100000, 1000000],
        [1, 10, 100, 1000, 10000, 100000, 1000000],
        [False, True],
    )
    param_names = ["Number of Nodes", "Number of Edges", "Cycle Check"]

    def setup(self, num_nodes, num_edges, cycle_check):
        self.graph = retworkx.PyDAG(cycle_check)
        nodes = self.graph.add_nodes_from(list(range(num_nodes)))
        self.list_empty = []
        self.list_obj = []
        node_ids = itertools.cycle(nodes)
        for i in range(num_edges):
            node_a = next(node_ids)
            node_b = next(node_ids)
            self.list_empty.append((node_a, node_b))
            self.list_obj.append((node_a, node_b, i))

    def time_digraph_add_edges_from(self, _, __, ___):
        self.graph.add_edges_from(self.list_obj)

    def time_digraph_add_edges_from_no_data(self, _, __, ___):
        self.graph.add_edges_from_no_data(self.list_empty)

    def time_digraph_add_edges_loop(self, _, __, ___):
        for i in self.list_obj:
            self.graph.add_edge(i[0], i[1], i[2])
