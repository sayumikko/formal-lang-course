from pyformlang.finite_automaton import *


def build_nfa_for_graph(graph, start_states: set = None, final_states: set = None):
    nfa = NondeterministicFiniteAutomaton()

    for edge in graph.edges(data=True):
        nfa.add_transition(edge[0], edge[2]["label"], edge[1])

    if not start_states:
        start_states = graph.nodes
    if not final_states:
        final_states = graph.nodes

    for node in start_states:
        nfa.add_start_state(State(node))

    for node in final_states:
        nfa.add_final_state(State(node))

    return nfa
