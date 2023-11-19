from networkx import MultiDiGraph
from pyformlang.cfg import CFG, Variable
from scipy.sparse import lil_matrix

from project.context_free_grammar_module import build_weak_chomsky_normal_form


def matrix(cfg: CFG, graph: MultiDiGraph):
    wcnf = build_weak_chomsky_normal_form(cfg)

    eps_productions = set()
    term_productions = set()
    var_productions = set()

    for prod in wcnf.productions:
        if len(prod.body) == 1:
            term_productions.add(prod)
        elif len(prod.body) == 2:
            var_productions.add(prod)
        else:
            eps_productions.add(prod)

    n = graph.number_of_nodes()
    var_to_mtx = {}

    for var in wcnf.variables:
        var_to_mtx[var] = lil_matrix((n, n), dtype=bool)

    for u, v, label in graph.edges(data="label"):
        for prod in term_productions:
            if label == prod.body[0].value:
                var_to_mtx[prod.head][u, v] = True

    for node in graph.nodes:
        i = list(graph.nodes).index(node)
        for var in eps_productions:
            var_to_mtx[var][i, i] = True

    while True:
        flag = False
        for prod in var_productions:
            prev_nonzero = var_to_mtx[prod.head].count_nonzero()
            var_to_mtx[prod.head] += var_to_mtx[prod.body[0]] @ var_to_mtx[prod.body[1]]

            if not flag:
                flag = prev_nonzero != var_to_mtx[prod.head].count_nonzero()

        if not flag:
            break

    res = set()
    for variable, matrix in var_to_mtx.items():
        rows, cols = matrix.nonzero()
        for i in range(len(rows)):
            res.add((list(graph.nodes)[rows[i]], variable, list(graph.nodes)[cols[i]]))

    return res


def matrix_cfpq(
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

    matrix_cfpq = matrix(cfg, graph)

    res = set()
    for v1, var, v2 in matrix_cfpq:
        if var == start_symbol and v1 in start_nodes and v2 in final_nodes:
            res.add((v1, v2))

    return res
