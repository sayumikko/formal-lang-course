from pyformlang.regular_expression import *


def build_min_dfa_for_regex(regex: Regex):
    return regex.to_epsilon_nfa().to_deterministic().minimize()
