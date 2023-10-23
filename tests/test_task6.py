from project.context_free_grammar_module import *
from pyformlang.cfg import Terminal, Variable

path = "tests/test_files"


def test_cfg():
    cfg = get_cfg_from_file(f"{path}/expected_task6_1")

    assert cfg.variables == {
        Variable("A"),
        Variable("B"),
        Variable("C"),
        Variable("S"),
    }
    assert cfg.terminals == {Terminal("a"), Terminal("b"), Terminal("c")}

    assert cfg.start_symbol == Variable("S")


def test_clear_unused():
    cfg = get_cfg_from_file(f"{path}/expected_task6_1")
    wcnf = build_weak_chomsky_normal_form(cfg)

    assert Variable("C") in cfg.variables
    assert Variable("C") not in wcnf.variables


def test_wcnf():
    cfg = get_cfg_from_file(f"{path}/expected_task6_2")
    wcnf = build_weak_chomsky_normal_form(cfg)

    for production in wcnf.productions:
        assert len(production.body) <= 2


def test_cfg_words():
    cfg = get_cfg_from_file(f"{path}/expected_task6_2")
    weak_cfg = build_weak_chomsky_normal_form(cfg)

    assert cfg.contains("abc")
    assert weak_cfg.contains("abc")


def test_empty_cfg_from_file():
    cfg = get_cfg_from_file("tests/test_files/expected_task6_3")
    assert cfg.is_empty()
