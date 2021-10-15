# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import math

import retworkx


class LayersBenchmarks:

    params = [19, 57, 115, 193, 291, 409, 547, 705, 883, 1081, 1299]
    param_names = ["Number of Nodes"]

    def setup(self, num_nodes):
        d = math.ceil((math.sqrt((10 * num_nodes) + 6)) / 5)
        self.graph = retworkx.generators.directed_heavy_hex_graph(d)

    def time_layers(self, _):
        retworkx.layers(self.graph, [0])

    def peakmem_layers(self, _):
        retworkx.layers(self.graph, [0])
