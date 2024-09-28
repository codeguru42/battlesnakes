import networkx as nx

from models import GameState, Position
from move import make_graph


def evaluate(state: GameState) -> int:
    head = state.you.head
    food = state.board.food
    graph = make_graph(state)
    return -min_dist(food, head, graph)


def min_dist(ps: list[Position], x: Position, graph: nx.DiGraph):
    return min(all_dist(ps, x, graph))


def all_dist(ps: list[Position], x: Position, graph: nx.DiGraph):
    for p in ps:
        try:
            yield nx.shortest_path_length(graph, x, p)
        except (nx.NetworkXNoPath, nx.NodeNotFound):
            yield 1000000
