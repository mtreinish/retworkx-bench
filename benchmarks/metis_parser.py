# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import bz2
import itertools

import retworkx

"""Parser for graph specification files from the METIS Version 4.0 input format

This module contains tools for parsing the graph input file format for
METIS 4.0. These were used in the 10th DIMACS challenge which are documented
here:

https://www.cc.gatech.edu/dimacs10/downloads.shtml
"""


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def parse_metis_from_file(path):
    """Parse a graph specification file and return a retworkx graph object

    :param str path: A path to the graph specification file to parse
    :param bool directed: Whether the returned graph is directed or not
        if set to True a PyDAG function is returned (with cycle_check set to
        False so it's a PyDiGraph) to maximize compatibility with functions
        that predate the PyDiGraph class

    :returns: A retworkx PyGraph or PyDAG object representing the input gr
        file
    """
    return_graph = retworkx.PyGraph()

    props_set = False
    node_index = 0
    weight = 0
    ncon = 0
    count = 0
    with bz2.open(path, "rt") as fd:
        for line in fd:
            line = line.rstrip()
            if not line:
                continue
            if line.startswith("%"):
                continue
            if not props_set:
                components = line.split(" ")
                if len(components) >= 3:
                    weight = int(components[2])
                if len(components) == 4:
                    ncon = int(components[3])
                if weight < 10:
                    if ncon > 0:
                        raise Exception("ncon requires node weight")
                    num_nodes = int(components[0])
                    for i in range(num_nodes):
                        return_graph.add_node(i)
                props_set = True
            else:
                raw_components = line.split(" ")
                if weight >= 10:
                    if ncon:
                        ncon_list = raw_components[:ncon]
                        node_index = return_graph.add_node(ncon_list)
                        if weight == 11:
                            for v, w in pairwise(raw_components[ncon:]):
                                vertex = int(v) - 1
                                weight = int(w)
                                return_graph.add_edge(node_index, vertex, weight)
                        else:
                            vertex_list = raw_components[:-ncon]
                            for v in vertex_list:
                                vertex = int(v) - 1
                                return_graph.add_edge(node_index, vertex, None)
                    else:
                        node_index = return_graph.add_node(raw_components[0])
                        if weight == 11:
                            for v, w in pairwise(raw_components[1:]):
                                vertex = int(v) - 1
                                weight = int(w)
                                return_graph.add_edge(node_index, vertex, weight)
                        else:
                            for v in raw_components[1:]:
                                vertex = int(v) - 1
                                return_graph.add_edge(node_index, vertex, None)
                else:
                    if weight == 1:
                        for v, w in pairwise(raw_components):
                            vertex = int(v) - 1
                            weight = int(w)
                            return_graph.add_edge(node_index, vertex, weight)
                    else:

                        for v in raw_components:
                            vertex = int(v) - 1
                            return_graph.add_edge(node_index, vertex, None)
                    node_index += 1
    return return_graph
