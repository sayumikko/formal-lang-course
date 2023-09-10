import pytest
import project.graph_module as gm
import filecmp
import os


def test_get_graph_from_csv_test():
    graph = gm.get_graph_from_csv("pizza")
    assert graph.number_of_nodes() == 671
    assert graph.number_of_edges() == 1980


def test_get_graph_info():
    info = gm.get_graph_info("pizza")
    assert info[0] == "pizza"
    assert info[1] == 671
    assert info[2] == 1980
    assert len(info[3]) == 1980

    assert info[3][3] == "type"


def test_save_graph_in_file():
    graph = gm.make_two_cycle_graph(3, 3, ("1", "2"))
    gm.save_graph_in_file("tests/GraphFile.dot", graph)

    assert filecmp.cmp(
        "tests/GraphFile.dot",
        "tests/expected_task1.dot",
        shallow=False,
    )

    os.remove("tests/GraphFile.dot")


def test_make_two_cycle_graph_test():
    graph = gm.make_two_cycle_graph(3, 3, ("1", "2"))
    assert graph.number_of_nodes() == 7
    assert graph.number_of_edges() == 8
