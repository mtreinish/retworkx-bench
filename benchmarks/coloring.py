# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import itertools
import os
import random

import retworkx

from .gr_parser import parse_gr_from_file
from .metis_parser import parse_metis_from_file


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


class ColoringRoadMapNYC:
    def setup(self):
        gr_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               'graphs', "USA-road-d.NY.gr")
        self.graph = parse_gr_from_file(gr_file, directed=False)

    def time_graph_greedy_coloring(self):
        retworkx.graph_greedy_color(self.graph)

    def peakmem_graph_greedy_coloring(self):
        retworkx.graph_greedy_color(self.graph)


class ColoringRoadMapAsia:
    timeout = 120.0

    def setup(self):
        metis_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  'graphs', "asia.osm.graph.bz2")
        self.graph = parse_metis_from_file(metis_file)

    def time_graph_greedy_coloring(self):
        retworkx.graph_greedy_color(self.graph)

    def peakmem_graph_greedy_coloring(self):
        retworkx.graph_greedy_color(self.graph)


class RandomGeometricGraph:
    timeout = 120.0

    def setup(self):
        metis_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  'graphs', "rgg_n_2_22_s0.graph.bz2")
        self.graph = parse_metis_from_file(metis_file)

    def time_graph_greedy_coloring(self):
        retworkx.graph_greedy_color(self.graph)

    def peakmem_graph_greedy_coloring(self):
        retworkx.graph_greedy_color(self.graph)


class TwoDimensionalDynamicSimulation:
    timeout = 120.0

    def setup(self):
        metis_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  'graphs', "hugetric-00020.graph.bz2")
        self.graph = parse_metis_from_file(metis_file)

    def time_graph_greedy_coloring(self):
        retworkx.graph_greedy_color(self.graph)

    def peakmem_graph_greedy_coloring(self):
        retworkx.graph_greedy_color(self.graph)
