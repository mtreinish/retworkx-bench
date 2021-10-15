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

    params = [10, 100, 1000, 10000, 100000, 1000000]
    param_names = ["Number of Nodes"]

    def setup(self, num_nodes):
        random.seed(42)
        self.graph = retworkx.PyDAG()
        nodes = self.graph.add_nodes_from(list(range(num_nodes)))
        node_iter = iter(nodes)
        parents = [next(node_iter)]
        count = 0
        while parents:
            source = parents.pop(0)
            try:
                target = next(nodes)
                parents.append(target)
                self.graph.add_edge(source, target, count)
                count += 1
            except StopIteration:
                break

    def time_topological_sort(self, _, __):
        retworkx.topological_sort(self.graph)

    def time_lexicographical_topological_sort(self, _, __):
        retworkx.lexicographical_topological_sort(self.graph, lambda x: str(x))
