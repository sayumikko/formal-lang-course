from pyformlang.finite_automaton import State
from scipy import sparse
from scipy.sparse import (
    block_diag,
    vstack,
    csr_matrix,
    dok_matrix,
    lil_matrix,
    csc_matrix,
)
import numpy

from project.nfa_bool_matrices import *


def constraint_bfs(
    graph: BooleanFiniteAutomaton,
    regex: BooleanFiniteAutomaton,
    for_each_node: bool = False,
    matrix_type=csr_matrix,
):
    direct_sum = {}

    for label in graph.bool_matrices.keys() & regex.bool_matrices.keys():
        direct_sum[label] = block_diag(
            (regex.bool_matrices[label], graph.bool_matrices[label])
        )

    front = (
        vstack([create_front(graph, regex, matrix_type) for st in graph.start_states])
        if for_each_node
        else create_front(graph, regex, matrix_type)
    )

    visited = matrix_type(front.shape, dtype=bool)
    first_step = True

    while True:
        old_visited_nnz = visited.nnz

        for mtx in direct_sum.values():
            if first_step:
                step = numpy.dot(front, mtx)
            else:
                step = numpy.dot(visited, mtx)
            visited += transform_front(step, regex, for_each_node, matrix_type)
        first_step = False

        if old_visited_nnz == visited.nnz:
            break

    result = set()
    regex_states = list(regex.states_indices.keys())
    graph_states = list(graph.states_indices.keys())

    for row, col in zip(*visited.nonzero()):
        if (
            not col < regex.number_of_states
            and regex_states[row % regex.number_of_states] in regex.final_states
        ):
            state_index = col - regex.number_of_states
            if graph_states[state_index] in graph.final_states:
                if for_each_node:
                    result.add(
                        (State(row // regex.number_of_states), State(state_index))
                    )
                else:
                    result.add(State(state_index))

    return result


def create_front(graph, regex: BooleanFiniteAutomaton, matrix_type):
    n = graph.number_of_states
    k = regex.number_of_states

    front = matrix_type((k, n + k))

    right_part = matrix_type([[state in graph.start_states for state in graph.states]])

    for _, index in regex.states_indices.items():
        front[index, index] = True
        front[index, k:] = right_part

    return front


def transform_front(step, regex, is_for_each_node, matrix_type):
    result = matrix_type(step.shape, dtype=bool)
    for row, col in zip(*step.nonzero()):
        if col < regex.number_of_states:
            right_row_part = step[row, regex.number_of_states :]
            if right_row_part.nnz != 0:
                if not is_for_each_node:
                    result[col, col] = True
                    result[col, regex.number_of_states :] += right_row_part
                else:
                    node_number = row // regex.number_of_states
                    result[node_number * regex.number_of_states + col, col] = True
                    result[
                        node_number * regex.number_of_states + col,
                        regex.number_of_states :,
                    ] += right_row_part
    return result
