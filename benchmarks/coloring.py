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

class ColoringBenchmarks:

    params = ([1, 10, 100, 1000, 10000, 100000, 1000000],
              [1, 10, 100, 1000, 10000, 100000, 1000000])
    param_names = ['Number of Nodes', 'Number of Edges']

    def setup(self, num_nodes, num_edges):
        random.seed(4242)
        self.graph = retworkx.PyGraph()
        nodes = self.graph.add_nodes_from(list(range(num_nodes)))
        random.shuffle(nodes)
        node_ids = itertools.cycle(nodes)
        list_obj = []
        for i in range(num_edges):
            list_obj.append((next(node_ids), next(node_ids), i))
        self.graph.add_edges_from(list_obj)

    def time_graph_greedy_coloring(self, _, __):
        retworkx.graph_greedy_color(self.graph)
