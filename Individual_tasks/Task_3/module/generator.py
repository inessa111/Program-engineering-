from graph import Graph
import typing
import random


class GenNPPS:
    def __init__(
        self,
        probEdgesToAttach: typing.Tuple[float],
        attachRule: typing.Callable[[int], float],
    ):
        self.map = dict()  # Структура для хранения слоев вершин
        self.attachRule = attachRule  # Правило предпочтительного связывания
        self.numEdgesToAttach = (
            probEdgesToAttach  # Вероятности задающие распределение для приращения
        )
        random.seed(10)

    def evolve(self, step: int, graph: Graph) -> Graph:  # функция генерации
        for v in graph.vertices:  # Заполняем слои
            self.addToLayer(v, graph.degree(v))
        # итерационный процесс добавления приращений
        for i in range(step):
            new_n = graph.generate_vertex()  # создаем узел приращения
            lst = []  # вспомогательный список для хранения выбранных вершин
            # разыгрываю случайную число ребер приращения по распределению numEdgesToAttach
            s = 0.0
            r = random.random()
            addEd = 0
            for j in range(len(self.numEdgesToAttach)):
                s += self.numEdgesToAttach[j]
                if s >= r:
                    addEd = j
                    break

            while len(lst) != addEd:  # пока не выбрано added вершин для присоединения
                k = self.getLayer()  # разыгрываю слой, после чего выбираю вершину
                n = self.map[k][
                    random.randrange(len(self.map[k]))
                ]  # из слоя - равновероятно
                lst.append(n)  # добавляю в вспомогательный список

            graph.addVertex(new_n)  # добавление новой вершины к графу
            for n in lst:  # добавляю ребра и корректирую список слоев
                tec = graph.degree(n)
                graph.addEdge(new_n, n)
                if n in self.map[tec]:
                    self.map[tec].remove(n)
                    if len(self.map[tec]) == 0:
                        self.map.pop(tec)
                self.addToLayer(n, tec + 1)
            self.addToLayer(new_n, addEd)
        return graph

    def addToLayer(self, n: int, i: int) -> None:  # добавляю вершины в список слоев
        if i not in self.map:
            self.map[i] = []
        lst = self.map[i]
        if n not in lst:
            lst.append(n)

    def getLayer(self) -> int:  # разыгрываю номер слоя
        k = 0
        rand = random.random()
        tr = 0
        sum = 0.0001
        for op in self.map.keys():
            sum = sum + self.attachRule(op) * len(self.map[op])
            for l in self.map.keys():
                A = len(self.map[l])
                tr = tr + (A * self.attachRule(l)) / sum
                if rand < tr:
                    k = l
                    break
        return k
