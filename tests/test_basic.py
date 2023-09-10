import pytest
import project.graph_module as gm
import os


def setup_module(module):
    print("basic setup module")


def teardown_module(module):
    print("basic teardown module")


def test_1():
    assert 1 + 1 == 2


def test_2():
    assert "1" + "1" == "11"
