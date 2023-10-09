from pyformlang.finite_automaton import NondeterministicFiniteAutomaton
from scipy import sparse


class BooleanFiniteAutomaton:
    number_of_states: int
    states: set
    start_states: set
    final_states: set
    states_indices: dict
    bool_matrices: dict

    def __init__(self, nfa: NondeterministicFiniteAutomaton = None):
        if nfa is None:
            self.number_of_states = 0
            self.states = set()
            self.start_states = set()
            self.final_states = set()
            self.states_indices = {}
            self.bool_matrices = {}

        else:
            self.number_of_states = len(nfa.states)
            self.states = nfa.states
            self.start_states = nfa.start_states
            self.final_states = nfa.final_states
            self.states_indices = {
                state: index for (index, state) in enumerate(nfa.states)
            }
            self.bool_matrices = self.build_bool_matrix_for_nfa(nfa)

    def build_bool_matrix_for_nfa(self, nfa: NondeterministicFiniteAutomaton):
        matrix = {}
        for first_state, transition in nfa.to_dict().items():
            for label, target_states in transition.items():
                if not isinstance(target_states, set):
                    target_states = {target_states}

                for state in target_states:
                    if label not in matrix:
                        matrix[label] = sparse.dok_matrix(
                            (self.number_of_states, self.number_of_states), dtype=bool
                        )
                    f = self.states_indices.get(first_state)
                    s = self.states_indices.get(state)
                    matrix[label][f, s] = True

        return matrix

    def intersect(self, second_automaton: "BooleanFiniteAutomaton"):
        bool_fa = BooleanFiniteAutomaton()
        labels = self.bool_matrices.keys() & second_automaton.bool_matrices.keys()

        for label in labels:
            bool_fa.bool_matrices[label] = sparse.kron(
                self.bool_matrices[label], second_automaton.bool_matrices[label]
            )

        for first_state, first_index in self.states_indices.items():
            for second_state, second_index in second_automaton.states_indices.items():
                state_index = (
                    first_index * second_automaton.number_of_states + second_index
                )

                bool_fa.states_indices[state_index] = state_index

                if (
                    first_state in self.start_states
                    and second_state in second_automaton.start_states
                ):
                    bool_fa.start_states.add(state_index)
                if (
                    first_state in self.final_states
                    and second_state in second_automaton.final_states
                ):
                    bool_fa.final_states.add(state_index)

        bool_fa.number_of_states = (
            self.number_of_states * second_automaton.number_of_states
        )

        return bool_fa

    def get_transitive_closure(self):
        if len(self.bool_matrices) == 0:
            return sparse.dok_matrix((0, 0), dtype=bool)

        transitive_closure = sum(self.bool_matrices.values())
        prev = transitive_closure.nnz
        curr = 0

        while prev != curr:
            transitive_closure += transitive_closure @ transitive_closure
            prev = curr
            curr = transitive_closure.nnz

        return transitive_closure

    def get_start_states(self):
        return self.start_states

    def get_final_states(self):
        return self.final_states
