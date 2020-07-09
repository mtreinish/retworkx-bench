# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Module for estimating import times."""

import retworkx


class RetworkxGraphCreation:
    def time_graph_creation(self):
        retworkx.PyGraph()

    def time_digraph_creation(self):
        retworkx.PyDiGraph()

    def time_digraph_creation_with_cycle_check(self):
        retworkx.PyDiGraph(check_cycle=True)

    def time_dag_creation(self):
        retworkx.PyDAG()

    def time_dag_creation_with_cycle_check(self):
        retworkx.PyDAG(check_cycle=True)
