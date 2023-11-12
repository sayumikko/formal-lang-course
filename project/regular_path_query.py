from networkx import MultiDiGraph
from pyformlang.regular_expression import Regex

from project.nfa import build_nfa_for_graph
from project.dfa import build_min_dfa_for_regex
from project.nfa_bool_matrices import BooleanFiniteAutomaton
from project.reachability_function import *

from scipy.sparse import lil_matrix


def tensor_rpq(
    graph: MultiDiGraph,
    regex: Regex,
    start_nodes: set = None,
    final_nodes: set = None,
    for_each_node: bool = False,
    matrix_type=lil_matrix,
):
    nfa = build_nfa_for_graph(graph, start_nodes, final_nodes)
    dfa = build_min_dfa_for_regex(regex)

    bool_matrix_for_graph = BooleanFiniteAutomaton(nfa)
    bool_matrix_for_query = BooleanFiniteAutomaton(dfa)

    bool_matrix_intersected = bool_matrix_for_graph.intersect(bool_matrix_for_query)

    start_states = bool_matrix_intersected.get_start_states()
    final_states = bool_matrix_intersected.get_final_states()

    transitive = bool_matrix_intersected.get_transitive_closure(matrix_type)

    result = set()

    for first_state, second_state in zip(*transitive.nonzero()):
        if first_state in start_states and second_state in final_states:
            result.add(
                (
                    first_state // bool_matrix_for_query.number_of_states,
                    second_state // bool_matrix_for_query.number_of_states,
                )
            )

    return result


def bfs_rpq(
    graph: MultiDiGraph,
    regex: Regex,
    start_nodes: set = None,
    final_nodes: set = None,
    for_each_node: bool = False,
    matrix_type=lil_matrix,
):
    graph_bool_matrix = BooleanFiniteAutomaton(
        build_nfa_for_graph(graph, start_nodes, final_nodes)
    )

    regex_bool_matrix = BooleanFiniteAutomaton(build_min_dfa_for_regex(regex))

    return constraint_bfs(
        graph_bool_matrix, regex_bool_matrix, for_each_node, matrix_type
    )
