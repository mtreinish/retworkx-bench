# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import os
import random
import itertools

import retworkx

from .gr_parser import parse_gr_from_file
from .metis_parser import parse_metis_from_file


class PathFunctionBenchmarks:

    params = (
        [10, 100, 1000, 10000, 100000, 1000000],
        [10, 100, 1000, 10000, 100000, 1000000],
    )
    param_names = ["Number of Nodes", "Number of Edges"]

    def setup(self, num_nodes, num_edges):
        random.seed(42 * num_nodes)
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
        if hasattr(retworkx, "dag_all_simple_paths"):
            self.all_simple_paths_func = retworkx.dag_all_simple_paths
        elif hasattr(retworkx, "digraph_all_simple_paths"):
            self.all_simple_paths_func = retworkx.digraph_all_simple_paths
        else:
            self.all_simple_paths_func = None

    def time_dag_longest_path(self, _, __):
        retworkx.dag_longest_path(self.graph)

    def time_dag_longest_path_length(self, _, __):
        retworkx.dag_longest_path_length(self.graph)

    def time_all_simple_paths(self, num_nodes, __):
        self.all_simple_paths_func(self.graph, 1, num_nodes - 2)


class TestAstar:
    params = ([10], [100, 1000, 10000, 100000, 1000000])
    param_names = ["Number of Nodes", "Number of Edges"]

    def setup(self, num_nodes, num_edges):
        random.seed(42)
        self.graph = retworkx.directed_gnm_random_graph(num_nodes, num_edges)
        for x in self.graph.node_indexes():
            self.graph[x] = x
        for edge in self.graph.edge_indices():
            self.graph.update_edge_by_index(edge, random.randint(1, 10000))

    def time_astar_shortest_path(self, num_nodes, __):
        def match_goal(x):
            return x == 1

        retworkx.astar_shortest_path(
            self.graph, 0, match_goal, float, lambda x: self.graph.out_degree(x)
        )


class PathsUSANYCRoadGraph:
    params = [True, False]
    param_names = ["Directed Graph"]

    def setup(self, directed):
        gr_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "graphs", "USA-road-d.NY.gr"
        )
        self.graph = parse_gr_from_file(gr_file, directed=directed)
        if directed:
            if hasattr(retworkx, "dag_all_simple_paths"):
                self.all_simple_paths_func = retworkx.dag_all_simple_paths
                self.astar_func = retworkx.dag_astar_shortest_path
            elif hasattr(retworkx, "digraph_all_simple_paths"):
                self.all_simple_paths_func = retworkx.digraph_all_simple_paths
                self.astar_func = retworkx.digraph_astar_shortest_path
            else:
                raise NotImplementedError
        else:
            if hasattr(retworkx, "graph_all_simple_paths"):
                self.all_simple_paths_func = retworkx.graph_all_simple_paths
                self.astar_func = retworkx.graph_astar_shortest_path
            else:
                raise NotImplementedError

    def time_all_simple_paths(self, _):
        # NOTE: this doesn't really traverse the graph, a full traversal is
        # too slow (for now) for a graph this large and takes over 10mins
        self.all_simple_paths_func(self.graph, 1, 0)

    def time_astar_shortest_path(self, directed):
        def match_goal(x):
            return x == 5123

        if directed:
            retworkx.astar_shortest_path(
                self.graph, 0, match_goal, float, lambda x: self.graph.out_degree(x)
            )
        else:
            retworkx.astar_shortest_path(
                self.graph, 0, match_goal, float, lambda x: self.graph.degree(x)
            )


class PathsRoadGraphWesternUSA:
    params = [True, False]
    param_names = ["Directed Graph"]

    def setup(self, directed):
        gr_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "graphs", "USA-road-t.W.gr.gz"
        )
        self.graph = parse_gr_from_file(gr_file, directed=directed)

    def time_astar_shortest_path(self, directed):
        def match_goal(x):
            return x == 5123

        if directed:
            retworkx.astar_shortest_path(
                self.graph, 0, match_goal, float, lambda x: self.graph.out_degree(x)
            )
        else:
            retworkx.astar_shortest_path(
                self.graph, 0, match_goal, float, lambda x: self.graph.degree(x)
            )


class PathsRoadGraphFullUSA:
    timeout = 600
    params = [True, False]
    param_names = ["Directed Graph"]

    def setup(self, directed):
        gr_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "graphs", "USA-road-t.USA.gr.gz"
        )
        self.graph = parse_gr_from_file(gr_file, directed=directed)

    def time_astar_shortest_path(self, directed):
        def match_goal(x):
            return x == 5123

        if directed:
            retworkx.astar_shortest_path(
                self.graph, 0, match_goal, float, lambda x: self.graph.out_degree(x)
            )
        else:
            retworkx.astar_shortest_path(
                self.graph, 0, match_goal, float, lambda x: self.graph.degree(x)
            )
