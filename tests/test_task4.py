from pyformlang.regular_expression import Regex
from networkx import MultiDiGraph

from project.regular_path_query import bfs_rpq
from project.graph_module import make_two_cycle_graph


def test_empty_rpq():
    graph = make_two_cycle_graph(3, 3, labels=("a", "b"))
    regex = Regex("(c|d)*")
    res = bfs_rpq(graph, regex)
    res_for_each_node = bfs_rpq(graph, regex, for_each_node=True)
    assert res == set()
    assert res_for_each_node == set()


def test_full_rpq():
    graph = MultiDiGraph()
    graph.add_edges_from(
        [
            (0, 1, {"label": "a"}),
            (1, 2, {"label": "b"}),
            (2, 3, {"label": "a"}),
            (3, 4, {"label": "b"}),
            (0, 2, {"label": "a"}),
            (2, 5, {"label": "b"}),
            (3, 6, {"label": "a"}),
            (6, 0, {"label": "b"}),
        ]
    )
    regex = Regex("(a|b)*")
    res = bfs_rpq(graph, regex)
    assert res == {0, 1, 2, 3, 4, 5, 6}


def test_rpq():
    graph = MultiDiGraph()
    graph.add_edges_from(
        [
            (0, 1, {"label": "a"}),
            (0, 2, {"label": "c"}),
            (0, 3, {"label": "b"}),
            (3, 4, {"label": "aa"}),
        ]
    )

    regex = Regex("(a|b)(aa)*")
    result = bfs_rpq(graph, regex, {0})
    assert result == {1, 3, 4}


def test_for_each():
    graph = MultiDiGraph()
    graph.add_edges_from(
        [
            (0, 1, {"label": "a"}),
            (0, 2, {"label": "b"}),
            (1, 2, {"label": "b"}),
            (2, 2, {"label": "c"}),
        ]
    )
    regex = Regex("a.b*")
    result = bfs_rpq(graph, regex, {0, 1}, {2}, True)
    assert result == {(0, 2), (1, 2)}
