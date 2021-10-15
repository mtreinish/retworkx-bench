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


class FloydWarshall:

    params = ([10, 100, 1000, 10000], [10, 100, 1000, 10000])
    param_names = ["Number of Nodes", "Number of Edges"]

    def setup(self, num_nodes, num_edges):
        self.graph = retworkx.directed_gnm_random_graph(
            num_nodes, num_edges, seed=4242423
        )

    def time_floyd_warshall(self, _, __):
        retworkx.floyd_warshall(self.graph)

    def peakmem_floyd_warshall(self, _, __):
        retworkx.floyd_warshall(self.graph)
