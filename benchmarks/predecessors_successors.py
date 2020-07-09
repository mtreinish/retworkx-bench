# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
import os
import itertools

import retworkx

from .gr_parser import parse_gr_from_file


class PredecessorsSuccessorBenchmarks:

    params = ([10, 100, 1000, 10000, 100000, 1000000],
              [10, 100, 1000, 10000, 100000, 1000000])
    param_names = ['Number of Nodes', 'Number of Edges']

    def setup(self, num_nodes, num_edges):
        self.graph = retworkx.PyDAG()
        self.nodes = []
        for i in range(num_nodes):
            self.nodes.append(self.graph.add_node(i))
        node_ids = itertools.cycle(self.nodes)
        for i in range(num_edges):
            self.graph.add_edge(next(node_ids), next(node_ids), i)
        if num_edges <= num_nodes:
            self.end_edge_index = num_edges - 1
        else:
            self.end_edge_index = num_nodes - 1

    def time_bfs_successors(self, _, __):
        retworkx.bfs_successors(self.graph, self.nodes[0])

    def time_successors(self, _, __):
        self.graph.successors(self.nodes[0])

    def time_predecessors(self, _, __):
        self.graph.predecessors(self.nodes[self.end_edge_index])

    def time_ancestors(self, _, __):
        retworkx.ancestors(self.graph, self.nodes[self.end_edge_index])

    def time_descendants(self, _, __):
        retworkx.descendants(self.graph, self.nodes[0])

    def time_number_weakly_connected_components(self, _, __):
        retworkx.number_weakly_connected_components(self.graph)


class PredecessorsSuccessorsUSANYCRoadGraph:

    def setup(self):
        gr_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               'graphs', "USA-road-d.NY.gr")
        self.graph = parse_gr_from_file(gr_file, directed=True)

    def time_bfs_successors(self):
        retworkx.bfs_successors(self.graph, 10240)

    def time_successors(self):
        self.graph.successors(10240)

    def time_predecessors(self):
        self.graph.predecessors(10240)

    def time_ancestors(self):
        retworkx.ancestors(self.graph, 10240)

    def time_descendants(self):
        retworkx.descendants(self.graph, 10240)

    def time_number_weakly_connected_components(self):
        retworkx.number_weakly_connected_components(self.graph)
