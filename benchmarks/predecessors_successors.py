# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
import os
import itertools

import retworkx

from .gr_parser import parse_gr_from_file


class PredecessorsSuccessorsUSANYCRoadGraph:
    def setup(self):
        gr_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "graphs", "USA-road-d.NY.gr"
        )
        self.graph = parse_gr_from_file(gr_file, directed=True)

    def time_bfs_successors(self):
        retworkx.bfs_successors(self.graph, 10240)

    def time_successors(self):
        self.graph.successors(10240)

    def time_predecessors(self):
        self.graph.predecessors(10240)

    def time_ancestors(self):
        retworkx.ancestors(self.graph, 10240)

    def time_descendants(self):
        retworkx.descendants(self.graph, 10240)

    def time_number_weakly_connected_components(self):
        retworkx.number_weakly_connected_components(self.graph)

    def time_strongly_connected_components(self):
        retworkx.strongly_connected_components(self.graph)


class PredecessorsSuccessorsRoadGraphWesternUSA:
    def setup(self):
        gr_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "graphs", "USA-road-t.W.gr.gz"
        )
        self.graph = parse_gr_from_file(gr_file, directed=True)

    def time_bfs_successors(self):
        retworkx.bfs_successors(self.graph, 10240)

    def time_successors(self):
        self.graph.successors(10240)

    def time_predecessors(self):
        self.graph.predecessors(10240)

    def time_ancestors(self):
        retworkx.ancestors(self.graph, 10240)

    def time_descendants(self):
        retworkx.descendants(self.graph, 10240)

    def time_number_weakly_connected_components(self):
        retworkx.number_weakly_connected_components(self.graph)

    def time_strongly_connected_components(self):
        retworkx.strongly_connected_components(self.graph)


class PredecessorsSuccessorsRoadGraphFullUSA:
    timeout = 600

    def setup(self):
        gr_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "graphs", "USA-road-t.USA.gr.gz"
        )
        self.graph = parse_gr_from_file(gr_file, directed=True)

    def time_bfs_successors(self):
        retworkx.bfs_successors(self.graph, 10240)

    def time_successors(self):
        self.graph.successors(10240)

    def time_predecessors(self):
        self.graph.predecessors(10240)

    def time_ancestors(self):
        retworkx.ancestors(self.graph, 10240)

    def time_descendants(self):
        retworkx.descendants(self.graph, 10240)

    def time_number_weakly_connected_components(self):
        retworkx.number_weakly_connected_components(self.graph)

    def time_strongly_connected_components(self):
        retworkx.strongly_connected_components(self.graph)
