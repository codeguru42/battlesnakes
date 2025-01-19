import sys
from typing import Iterator, Tuple

import networkx as nx

from models import GameState, Position, MoveEnum, Battlesnake


def evaluate(move: MoveEnum, state: GameState) -> int:
    head = state.you.head
    food = state.board.food
    snakes = state.board.snakes
    other_snakes = set(snakes) - {state.you}
    used = set().union(*(s.body[:-1] for s in snakes))
    graph = make_graph(state)
    new_pos = head + move
    if is_occupied(new_pos, used):
        if will_win_head_to_head(new_pos, state.you, other_snakes):
            return sys.maxsize
        return -sys.maxsize
    return -min_dist(food, new_pos, graph)


def min_dist(ps: list[Position], x: Position, graph: nx.DiGraph):
    return min(all_dist(ps, x, graph))


def all_dist(ps: list[Position], x: Position, graph: nx.DiGraph):
    for p in ps:
        try:
            yield nx.shortest_path_length(graph, x, p)
        except (nx.NetworkXNoPath, nx.NodeNotFound):
            yield 1000000


def make_graph(state: GameState) -> nx.DiGraph:
    graph: nx.DiGraph = nx.DiGraph()
    used = set().union(*(s.body[:-1] for s in state.board.snakes))
    to_visit = [state.you.head]
    visited = set()
    while len(to_visit) > 0:
        curr = to_visit.pop()
        visited.add(curr)
        for _, neighbor in neighbors(curr):
            if is_in_bounds(
                neighbor, state.board.width, state.board.height
            ) and not is_occupied(neighbor, used):
                graph.add_edge(curr, neighbor)
                if neighbor not in visited:
                    to_visit.append(neighbor)
    return graph


def neighbors(pos: Position) -> Iterator[Tuple[MoveEnum, Position]]:
    for m in MoveEnum:
        yield m, Position(
            x=pos.x + MoveEnum(m).delta().x, y=pos.y + MoveEnum(m).delta().y
        )


def is_in_bounds(pos: Position, width: int, height: int) -> bool:
    return 0 <= pos.x < width and 0 <= pos.y < height


def is_occupied(pos: Position, used: set[Position]) -> bool:
    return pos in used


def will_win_head_to_head(
    pos: Position, you: Battlesnake, other_snakes: set[Battlesnake]
) -> bool:
    return all(
        is_head_neighbor(other, pos) and is_longer(you, other) for other in other_snakes
    )


def is_head_neighbor(snake: Battlesnake, pos: Position) -> bool:
    return dist(snake.head, pos) == 1


def is_longer(snake: Battlesnake, other: Battlesnake) -> bool:
    return snake.length > other.length


def dist(p1: Position, p2: Position) -> int:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)
