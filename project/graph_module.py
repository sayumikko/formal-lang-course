import cfpq_data as cd
import networkx as nkx


def get_graph_from_csv(name: str):
    path = cd.download(name)
    return cd.graph_from_csv(path)


def get_graph_info(name: str):
    info = []
    labels = []

    graph = get_graph_from_csv(name=name)

    info.append(name)
    info.append(graph.number_of_nodes())
    info.append(graph.number_of_edges())

    for edge in graph.edges(data=True):
        labels.append(edge[2]["label"])

    info.append(labels)

    return info


def save_graph_in_file(filename: str, graph: nkx.Graph):
    pydot_graph = nkx.drawing.nx_pydot.to_pydot(graph)
    pydot_graph.write(filename)
    return


def make_two_cycle_graph(frst_nodes: int, scnd_nodes: int, labels: tuple):
    return cd.labeled_two_cycles_graph(frst_nodes, scnd_nodes, labels=labels)
