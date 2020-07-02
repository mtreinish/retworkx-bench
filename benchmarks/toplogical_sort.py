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

class TopologicalSortBenchmarks:

    params = ([10, 100, 1000, 10000, 100000, 1000000],
              [10, 100, 1000, 10000, 100000, 1000000])
    param_names = ['Number of Nodes', 'Number of Edges']

    def setup(self, num_nodes, num_edges):
        random.seed(42)
        self.graph = retworkx.PyDAG()
        nodes = []
        for i in range(num_nodes):
            nodes.append(self.graph.add_node(i))
        random.shuffle(nodes)
        node_ids = itertools.cycle(nodes)
        list_obj = []
        for i in range(num_edges):
            list_obj.append((next(node_ids), next(node_ids), i))
        self.graph.add_edges_from(list_obj)

    def time_topological_sort(self, _, __):
        retworkx.topological_sort(self.graph)

    def time_lexicographical_topological_sort(self, _, __):
        retworkx.lexicographical_topological_sort(self.graph, lambda x: str(x))
