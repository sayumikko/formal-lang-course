from pyformlang.cfg import Variable

from project.ecfg import ECFG


class RSM:
    def __init__(self, start: Variable, boxes: dict):
        self.start = start
        self.boxes = boxes


def build_rsm_from_ecfg(ecfg: ECFG):
    boxes = {}
    for key, fa in ecfg.productions.items():
        boxes[key] = fa.to_epsilon_nfa()
    return RSM(start=ecfg.start_symbol, boxes=boxes)


def minimize_rsm(rsm: RSM):
    res = RSM(start=rsm.start, boxes={})
    for v, nfa in rsm.boxes.items():
        res.boxes[v] = nfa.minimize()
    return res
