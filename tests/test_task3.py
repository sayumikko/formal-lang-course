import cfpq_data

from project.nfa_bool_matrices import BooleanFiniteAutomaton
from project.regular_path_query import regular_path_querying

from pyformlang.finite_automaton import NondeterministicFiniteAutomaton
from pyformlang.regular_expression import Regex


def test_bfa_for_empty_nfa():
    nfa = NondeterministicFiniteAutomaton()
    decomposition = BooleanFiniteAutomaton(nfa)
    assert decomposition.number_of_states == 0
    assert not decomposition.start_states
    assert not decomposition.final_states
    assert not decomposition.states_indices
    assert not decomposition.bool_matrices


def test_bfa_for_non_empty_nfa():
    nfa = NondeterministicFiniteAutomaton()

    nfa.add_start_state(0)
    nfa.add_final_state(2)
    nfa.add_transition(0, "a", 1)
    nfa.add_transition(1, "b", 2)
    nfa.add_transition(0, "c", 0)

    decomposition = BooleanFiniteAutomaton(nfa)

    assert decomposition.start_states == {0}
    assert decomposition.final_states == {2}
    assert decomposition.states_indices == {1: 1, 2: 2, 0: 0}
    assert decomposition.number_of_states == 3


def test_transitive_closure():
    nfa = NondeterministicFiniteAutomaton()

    nfa.add_transitions(
        [
            (0, "l1", 1),
            (1, "l2", 2),
        ]
    )

    bool_matrix = BooleanFiniteAutomaton(nfa)
    transitive_closure = bool_matrix.get_transitive_closure()
    assert transitive_closure.sum() == transitive_closure.size


def test_intersect():
    nfa1 = NondeterministicFiniteAutomaton()
    nfa1.add_start_state(0)
    nfa1.add_final_state(1)
    nfa1.add_transition(0, "b", 1)
    nfa1.add_transition(1, "a", 1)
    boolean_nfa1 = BooleanFiniteAutomaton(nfa1)

    nfa2 = NondeterministicFiniteAutomaton()
    nfa2.add_start_state(0)
    nfa2.add_final_state(2)
    nfa2.add_transition(0, "с", 0)
    nfa2.add_transition(0, "b", 1)
    nfa2.add_transition(1, "c", 1)
    nfa2.add_transition(1, "a", 2)
    boolean_nfa2 = BooleanFiniteAutomaton(nfa2)

    actual_intersection = BooleanFiniteAutomaton.intersect(boolean_nfa1, boolean_nfa2)

    expected_nfa = NondeterministicFiniteAutomaton()
    expected_nfa.add_start_state(0)
    expected_nfa.add_final_state(5)
    expected_nfa.add_transition(0, "b", 4)
    expected_nfa.add_transition(4, "a", 5)

    expected_intersection = BooleanFiniteAutomaton(expected_nfa)

    assert actual_intersection.number_of_states == len(nfa1.states) * len(nfa2.states)
    assert actual_intersection.start_states == expected_intersection.start_states
    assert actual_intersection.final_states == expected_intersection.final_states
    for label in actual_intersection.bool_matrices.keys():
        assert (
            actual_intersection.bool_matrices[label].nnz
            == expected_intersection.bool_matrices[label]
        ).nnz


def test_regular_path_query():
    graph = cfpq_data.labeled_two_cycles_graph(3, 3, labels=("a", "b"), common_node=0)
    regex = Regex("(a|b)(aa)*")
    result = regular_path_querying(graph, regex, {0}, {1})
    assert result == {(0, 1)}
