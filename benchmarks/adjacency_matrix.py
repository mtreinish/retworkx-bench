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

    params = ([10, 100, 1000, 10000, 100000],
              [10, 100, 1000, 10000, 100000])
    param_names = ['Number of Nodes', 'Number of Edges']

    def setup(self, num_nodes, num_edges):
        random.seed(4242)
        self.graph = retworkx.PyGraph()
        nodes = []
        for i in range(num_nodes):
            nodes.append(self.graph.add_node(i))
        random.shuffle(nodes)
        node_ids = itertools.cycle(nodes)
        for i in range(num_edges):
            self.graph.add_edge(next(node_ids), next(node_ids), i)

    def time_adjacency_matrix(self, _, __):
        retworkx.graph_adjacency_matrix(self.graph, lambda x: x)

    def peakmem_adjacency_matrix(self, _, __):
        retworkx.graph_adjacency_matrix(self.graph, lambda x: x)


class DiGraphAdjacencyMatrixBenchmarks:

    params = ([10, 100, 1000, 10000, 100000],
              [10, 100, 1000, 10000, 100000],
              [False, True])
    param_names = ['Number of Nodes', 'Number of Edges', 'Removed Nodes']

    def setup(self, num_nodes, num_edges, remove_nodes):
        if hasattr(retworkx, 'dag_adjacency_matrix'):
            self.graph_func = retworkx.dag_adjacency_matrix
        else:
            self.graph_func = retworkx.digraph_adjacency_matrix
        random.seed(4242)
        self.graph = retworkx.PyDAG()
        nodes = []
        for i in range(num_nodes):
            nodes.append(self.graph.add_node(i))
        random.shuffle(nodes)
        removed_node = None
        if remove_nodes:
            removed_node = random.randint(0, num_nodes)
            self.graph.remove_node(removed_node)
            nodes.remove(removed_node)
        node_ids = itertools.cycle(nodes)
        for i in range(num_edges):
            src = next(node_ids)
            target = next(node_ids)
            self.graph.add_edge(src, target, i)

    def time_adjacency_matrix(self, _, __, ___):
        self.graph_func(self.graph, lambda x: x)

    def peakmem_adjacency_matrix(self, _, __, ___):
        self.graph_func(self.graph, lambda x: x)
