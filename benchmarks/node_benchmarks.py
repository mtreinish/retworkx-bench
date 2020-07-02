# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import retworkx


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
