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


class FloydWarshall:

    params = ([10, 100, 1000],
              [10, 100, 1000])
    param_names = ['Number of Nodes', 'Number of Edges']

    def setup(self, num_nodes, num_edges):
        random.seed(4242)
        self.graph = retworkx.PyDAG()
        nodes = []
        for i in range(num_nodes):
            nodes.append(self.graph.add_node(i))
        random.shuffle(nodes)
        node_ids = itertools.cycle(nodes)
        for i in range(num_edges):
            src = next(node_ids)
            target = next(node_ids)
            self.graph.add_edge(src, target, i)

    def time_floyd_warshall(self, _, __):
        retworkx.floyd_warshall(self.graph)

    def peakmem_floyd_warshall(self, _, __):
        retworkx.floyd_warshall(self.graph)
