# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import os

import retworkx

from .gr_parser import parse_gr_from_file


class NodeCreation:

    params = ([1, 10, 100, 1000, 10000, 100000, 1000000, 100000000])
    param_names = ['Number of Nodes']

    def setup(self, num_nodes):
        self.empty_graph = retworkx.PyGraph()
        self.empty_digraph = retworkx.PyDAG()
        self.list_objs = list(range(num_nodes))

    def time_graph_add_nodes_from(self, _):
        self.empty_graph.add_nodes_from(self.list_objs)

    def time_graph_add_nodes_loop(self, num_nodes):
        for i in self.list_objs:
            self.empty_graph.add_node(i)

    def time_digraph_add_node_from(self, _):
        self.empty_digraph.add_nodes_from(self.list_objs)

    def time_digraph_add_nodes_loop(self, num_nodes):
        for i in self.list_objs:
            self.empty_digraph.add_node(i)


class GraphNodeAddition:
    params = ([1, 10, 100, 1000, 10000, 100000, 1000000],
              [1, 10, 100, 1000, 10000, 100000, 1000000])
    param_names = ['Graph Size', 'Number of Nodes']

    def setup(self, graph_size, num_nodes):
        self.full_graph = retworkx.PyGraph()
        self.list_obj = list(range(num_nodes))
        self.full_graph.add_nodes_from(list(range(graph_size)))

    def time_add_from(self, _, __):
        self.full_graph.add_nodes_from(self.list_obj)

    def time_add_loop(self, _, __):
        for i in self.list_obj:
            self.full_graph.add_node(i)


class DiGraphNodeAddition:
    params = ([1, 10, 100, 1000, 10000, 100000, 1000000],
              [1, 10, 100, 1000, 10000, 100000, 1000000])
    param_names = ['Graph Size', 'Number of Nodes']

    def setup(self, graph_size, num_nodes):
        self.full_graph = retworkx.PyDAG()
        self.list_obj = list(range(num_nodes))
        self.full_graph.add_nodes_from(list(range(graph_size)))

    def time_add_from(self, _, __):
        self.full_graph.add_nodes_from(self.list_obj)

    def time_add_loop(self, _, __):
        for i in self.list_obj:
            self.full_graph.add_node(i)


class USANYCRoadGraph:
    params = ([True, False])
    param_names = ["Directed Graph"]

    def setup(self, directed):
        gr_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               'graphs', "USA-road-d.NY.gr")
        self.graph = parse_gr_from_file(gr_file, directed=directed)

    def time___len__(self, _):
        len(self.graph)

    def time_remove_node(self, _):
        self.graph.remove_node(425)

    def time_nodes(self, _):
        self.graph.nodes()

    def time_nodes_indexes(self, _):
        self.graph.node_indexes()

    def time_get_node_data(self, _):
        self.graph.get_node_data(5210)
