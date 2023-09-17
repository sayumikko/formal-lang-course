from pyformlang.regular_expression import Regex
from pyformlang.finite_automaton import *

import project.dfa as dfam
import project.graph_module as gm
import project.nfa as nfam
import networkx as nx
import cfpq_data


def test_empty_min_dfa():
    dfa = dfam.build_min_dfa_for_regex(Regex(""))
    assert dfa.is_deterministic()
    assert dfa.is_empty()


def test_for_alternative_regex():
    dfa = dfam.build_min_dfa_for_regex(Regex("1|42"))
    assert dfa.accepts([Symbol("42")])
    assert dfa.accepts([Symbol("1")])
    assert not dfa.accepts([Symbol("2")])


def test_for_asterisk():
    dfa = dfam.build_min_dfa_for_regex(Regex("1*"))
    assert dfa.accepts([Symbol("1")])
    assert dfa.accepts([Symbol("1"), Symbol("1")])


def test_for_space():
    dfa = dfam.build_min_dfa_for_regex(Regex("1 2"))
    assert dfa.accepts([Symbol("1"), Symbol("2")])
    assert not dfa.accepts([Symbol("12")])


def test_create_nfa_for_empty_graph():
    nfa = nfam.build_nfa_for_graph(nx.Graph())
    assert nfa.is_empty()


def test_build_nfa_for_two_cycles_graph():
    graph = cfpq_data.labeled_two_cycles_graph(1, 1, labels=("a", "b"))
    nfa = nfam.build_nfa_for_graph(graph, {0}, {1})

    test_nfa = NondeterministicFiniteAutomaton()
    test_nfa.add_start_state(State(0))
    test_nfa.add_final_state(State(1))

    for fr, to, label in graph.edges(data="label"):
        test_nfa.add_transition(State(fr), Symbol(label), State(to))

    assert nfa == test_nfa
