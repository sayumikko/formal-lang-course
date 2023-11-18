from networkx import MultiDiGraph
from pyformlang.cfg import CFG, Variable

from project.context_free_grammar_module import build_weak_chomsky_normal_form


def hellings_closure(cfg: CFG, graph: MultiDiGraph):
    wcnf = build_weak_chomsky_normal_form(cfg)

    eps_productions = set()
    term_productions = set()
    var_productions = set()

    for production in wcnf.productions:
        if len(production.body) == 1:
            term_productions.add(production)
        elif len(production.body) == 2:
            var_productions.add(production)
        else:
            eps_productions.add(production)

    result = []

    for u, v, label in graph.edges(data="label"):
        for production in term_productions:
            if label == production.body[0].value:
                result.append((u, production.head, v))

    for node in graph.nodes:
        for production in eps_productions:
            result.append((node, production.head, node))

    queue = result.copy()

    while len(queue) > 0:
        (v1, var, v2) = queue.pop(0)

        for x, y, z in result:
            if z == v1:
                for prod in var_productions:
                    new_triple = (x, prod.head, v2)
                    if (
                        prod.body[0] == y
                        and prod.body[1] == var
                        and new_triple not in result
                    ):
                        queue.append(new_triple)
                        result.append(new_triple)

            if x == v2:
                for prod in var_productions:
                    new_triple = (v1, prod.head, z)
                    if (
                        prod.body[0] == var
                        and prod.body[1] == y
                        and new_triple not in result
                    ):
                        queue.append(new_triple)
                        result.append(new_triple)

    return result


def cfpq(
    cfg: CFG,
    graph: MultiDiGraph,
    start_nodes: set = None,
    final_nodes: set = None,
    start_symbol: Variable = Variable("S"),
):
    if not start_nodes:
        start_nodes = set(graph.nodes)
    if not final_nodes:
        final_nodes = set(graph.nodes)

    hellings = hellings_closure(cfg, graph)

    res = set()
    for v1, var, v2 in hellings:
        if var == start_symbol and v1 in start_nodes and v2 in final_nodes:
            res.add((v1, v2))

    return res
