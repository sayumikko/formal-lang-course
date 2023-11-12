from networkx import MultiDiGraph

from project.context_free_grammar_module import get_cfg_from_file
from project.hellings import cfpq


def build_graph(nodes, edges):
    graph = MultiDiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    return graph


def test_simple_path():
    graph = build_graph(
        {0, 1, 2, 3},
        [
            (0, 1, {"label": "a"}),
            (1, 2, {"label": "b"}),
            (2, 3, {"label": "c"}),
        ],
    )

    cfg = get_cfg_from_file("tests/test_files/expected_task8_1")
    res = cfpq(cfg, graph, {0}, {3})

    assert res == {(0, 3)}


def test_alternating():
    graph = build_graph(
        {0, 1, 2, 3},
        [
            (0, 1, {"label": "a"}),
            (1, 2, {"label": "a"}),
            (2, 0, {"label": "a"}),
            (2, 3, {"label": "b"}),
            (3, 2, {"label": "b"}),
        ],
    )

    cfg = get_cfg_from_file("tests/test_files/expected_task8_2")

    res = cfpq(cfg, graph, start_nodes={3})
    assert res == set()

    res = cfpq(cfg, graph, start_nodes={0}, final_nodes={2, 3})
    assert res == {(0, 2), (0, 3)}
