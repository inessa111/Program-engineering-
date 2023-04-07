import matplotlib.pyplot as plt
import networkx as nx
import typing


def draw(nodes: typing.List[int], edges: typing.List[typing.Tuple[int]]) -> None:
    plt.clf()
    G = nx.Graph()  # создаём объект графа
    # добавляем информацию в объект графа
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    # рисуем граф и отображаем его
    nx.draw(G, with_labels=True, font_weight="bold")
    plt.show(block=False)


if __name__ == "__main__":
    from graph import Graph
    from generator import GenNPPS

    g = Graph()
    attachRule = lambda x: float(x)
    probEdgesToAttach = [
       0.0,
       0.0,
       1
    ]  # плотность вероятности дискретной случайной величины, описывающей кол-во ребер у вновь добавленной вершины
    gen = GenNPPS(probEdgesToAttach, attachRule)
    #while True:
    gen.evolve(step=10000, graph=g)
    draw(g.vertices, g.edges)
    plt.show()
        #input()
