from pyformlang.finite_automaton import Symbol
from pyformlang.regular_expression import Regex

from project.dfa import build_min_dfa_for_regex
from project.context_free_grammar_module import get_cfg_from_file
from project.ecfg import *
from project.rsm import *


def test_empty_ecfg_and_rsm():
    ecfg = build_ecfg_from_text("")
    rsm = build_rsm_from_ecfg(ecfg)

    expected_productions = {}

    assert all(
        rsm.boxes[var].is_equivalent_to(expected_productions[var].to_epsilon_nfa())
        for var in expected_productions.keys()
    )


def test_rsm_from_ecfg():
    ecfg = get_ecfg_from_file("tests/test_files/expected_task7_1")
    rsm = build_rsm_from_ecfg(ecfg)

    expected_productions = {
        Variable("S"): Regex("A B C"),
        Variable("A"): Regex("a"),
        Variable("B"): Regex("b"),
        Variable("C"): Regex("(c | S)"),
    }

    assert rsm.start == Variable("S")

    assert all(
        rsm.boxes[var].is_equivalent_to(expected_productions[var].to_epsilon_nfa())
        for var in expected_productions.keys()
    )


def test_minimize_rsm():
    ecfg = get_ecfg_from_file("tests/test_files/expected_task7_1")
    rsm = build_rsm_from_ecfg(ecfg)

    assert all(
        minimize_rsm(rsm).boxes[var] == build_min_dfa_for_regex(ecfg.productions[var])
        for var in ecfg.productions.keys()
    )


def test_ecfg_and_cfg():
    cfg = get_cfg_from_file("tests/test_files/expected_task7_2")
    ecfg = build_ecfg_from_cfg(cfg)

    expected_ecfg = ECFG(
        variables={Variable("S"), Variable("A")},
        productions={
            Variable("S"): Regex("A"),
            Variable("A"): Regex("(($|b?)|(S.S))"),
        },
    )

    assert ecfg.variables == expected_ecfg.variables
    assert ecfg.start_symbol == expected_ecfg.start_symbol

    assert all(
        build_min_dfa_for_regex(ecfg.productions[var]).is_equivalent_to(
            build_min_dfa_for_regex(expected_ecfg.productions[var])
        )
        for var in expected_ecfg.productions.keys()
    )


def test_ecfg_from_text():
    ecfg = build_ecfg_from_text(
        """
        S -> A B C* | a b
        A -> a*
        B -> b
        C -> c | b
        """
    )

    expected_ecfg = ECFG(
        variables={Variable("S"), Variable("A"), Variable("B"), Variable("C")},
        productions={
            Variable("S"): Regex("((A.(B.(C)*))|(a.b))"),
            Variable("A"): Regex("(a)*"),
            Variable("B"): Regex("b"),
            Variable("C"): Regex("(c|b)"),
        },
    )

    assert ecfg.variables == expected_ecfg.variables
    assert ecfg.start_symbol == expected_ecfg.start_symbol

    assert all(
        build_min_dfa_for_regex(ecfg.productions[var]).is_equivalent_to(
            build_min_dfa_for_regex(expected_ecfg.productions[var])
        )
        for var in expected_ecfg.productions.keys()
    )


def test_same_start_symbols():
    ecfg = build_ecfg_from_text(
        """
        S -> A B
        S -> $
        A -> A a
        B -> A
        B -> B
        B -> $"""
    )

    expected_ecfg = ECFG(
        variables={Variable("S"), Variable("A"), Variable("B")},
        productions={
            Variable("S"): Regex("$"),
            Variable("A"): Regex("A.a"),
            Variable("B"): Regex("$"),
        },
    )

    assert ecfg.variables == expected_ecfg.variables
    assert ecfg.start_symbol == expected_ecfg.start_symbol

    assert all(
        build_min_dfa_for_regex(ecfg.productions[var]).is_equivalent_to(
            build_min_dfa_for_regex(expected_ecfg.productions[var])
        )
        for var in expected_ecfg.productions.keys()
    )


def test_equialent_languages():
    ecfg = build_ecfg_from_text(
        """
        S -> A B C* | a b
        A -> a*
        B -> b
        C -> c | b
        """
    )

    rsm = build_rsm_from_ecfg(ecfg)

    assert len(rsm.boxes) == len(ecfg.productions)
    assert rsm.start == ecfg.start_symbol

    for var in ecfg.productions:
        actual = rsm.boxes[var]
        expected = ecfg.productions[var].to_epsilon_nfa()
        assert actual.is_equivalent_to(expected)
