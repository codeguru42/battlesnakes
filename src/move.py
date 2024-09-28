from collections.abc import Iterator
from typing import Tuple

import networkx as nx

from evaluate import min_dist
from models import GameState, MoveEnum, Position, Battlesnake


class InvalidMove(BaseException):
    pass


def dist(p1: Position, p2: Position) -> int:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def make_move(state: GameState) -> MoveEnum:
    head = state.you.head
    food = state.board.food
    snakes = state.board.snakes
    used = set().union(*(s.body[:-1] for s in snakes))
    choices = {}
    other_snakes = set(snakes) - {state.you}
    for m, new_pos in neighbors(head):
        if (
            is_in_bounds(new_pos, state.board.width, state.board.height)
            and not is_occupied(new_pos, used)
            and will_win_head_to_head(new_pos, state.you, other_snakes)
        ):
            choices[m] = new_pos
    graph = make_graph(state)
    md = {m: min_dist(food, c, graph) for m, c in choices.items()}

    return min(md.keys(), key=lambda m: md[m])


def is_in_bounds(pos: Position, width: int, height: int) -> bool:
    return 0 <= pos.x < width and 0 <= pos.y < height


def is_occupied(pos: Position, used: set[Position]) -> bool:
    return pos in used


def move_snake(snake: Battlesnake, move: MoveEnum) -> Position:
    head = snake.head
    delta = move.delta()
    new_head = Position(x=head.x + delta.x, y=head.y + delta.y)

    if new_head == snake.body[1]:
        raise InvalidMove

    snake.head = new_head
    snake.body.insert(0, new_head)
    return snake.body.pop()


def unmove_snake(snake: Battlesnake, prev_tail: Position):
    snake.body.pop(0)
    snake.head = snake.body[0]
    snake.body.append(prev_tail)


def all_moves(snake: Battlesnake) -> Iterator[Battlesnake]:
    for m in MoveEnum:
        try:
            prev_tail = move_snake(snake, MoveEnum(m))
            yield snake
            unmove_snake(snake, prev_tail)
        except InvalidMove:
            pass


def is_head_neighbor(snake: Battlesnake, pos: Position) -> bool:
    return dist(snake.head, pos) == 1


def is_longer(snake: Battlesnake, other: Battlesnake) -> bool:
    return snake.length > other.length


def will_win_head_to_head(
    pos: Position, you: Battlesnake, other_snakes: set[Battlesnake]
) -> bool:
    return all(
        not is_head_neighbor(other, pos) or is_longer(you, other)
        for other in other_snakes
    )


def neighbors(pos: Position) -> Iterator[Tuple[MoveEnum, Position]]:
    for m in MoveEnum:
        yield m, Position(
            x=pos.x + MoveEnum(m).delta().x, y=pos.y + MoveEnum(m).delta().y
        )


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
