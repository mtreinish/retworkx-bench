# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import math
import random
import itertools

import retworkx

class PathFunctionBenchmarks:

    params = ([10, 100, 1000, 10000, 100000, 1000000],
              [10, 100, 1000, 10000, 100000, 1000000])
    param_names = ['Number of Nodes', 'Number of Edges']

    def setup(self, num_nodes, num_edges):
        random.seed(42 * num_nodes)
        self.graph = retworkx.PyDAG()
        nodes = []
        for i in range(num_nodes):
            nodes.append(self.graph.add_node(i))
        random.shuffle(nodes)
        node_ids = itertools.cycle(nodes)
        list_obj = []
        for i in range(num_edges):
            src = next(node_ids)
            target = next(node_ids)
            self.graph.add_edge(src, target, i)
        if hasattr(retworkx, 'dag_all_simple_paths'):
            self.all_simple_paths_func = retworkx.dag_all_simple_paths
        elif hasattr(retworkx, 'digraph_all_simple_paths'):
            self.all_simple_paths_func = retworkx.digraph_all_simple_paths
        else:
            self.all_simple_paths_func = None

    def time_dag_longest_path(self, _, __):
        retworkx.dag_longest_path(self.graph)

    def time_dag_longest_path_length(self, _, __):
        retworkx.dag_longest_path_length(self.graph)

    def time_all_simple_paths(self, num_nodes, __):
        self.all_simple_paths_func(self.graph, 1, num_nodes - 2)

class TestAstar:
    params = ([10],
              [10, 100, 1000, 10000, 100000, 1000000])
    param_names = ['Number of Nodes', 'Number of Edges']

    def setup(self, num_nodes, num_edges):
        if hasattr(retworkx, 'dag_astar_shortest_path'):
            self.astar_func = retworkx.dag_astar_shortest_path
        else:
            self.astar_func = retworkx.digraph_astar_shortest_path
        random.seed(42)
        self.graph = retworkx.PyDAG()
        nodes = []
        for i in range(num_nodes):
            nodes.append(self.graph.add_node(i))
        random.shuffle(nodes)
        node_ids = itertools.cycle(nodes)
        list_obj = []
        for i in range(num_edges):
            src = next(node_ids)
            target = next(node_ids)
            self.graph.add_edge(src, target, i)


    def time_astar_shortest_path(self, num_nodes, __):
        def match_goal(x):
            return x == 1

        self.astar_func(
                self.graph, 0, match_goal, lambda x: x,
                lambda x: 1)
