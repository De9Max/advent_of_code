from typing import Tuple

import config


class Maze:
    def __init__(self, maze_string: str):
        self.maze = [list(line) for line in maze_string.splitlines()]
        self.start = self.find_start()
        self.stack = [self.start]
        self.visited = {self.start}
        self.tracker = {self.start: None}
        self.cycle = []
        self.find_cycle()

    def find_start(self) -> Tuple[int, int]:
        """ Function to find the starting position of maze """
        for i, row in enumerate(self.maze):
            for j, cell in enumerate(row):
                if cell == 'S':
                    return i, j
        return -1, -1

    def find_cycle(self):
        """ Find cycle in maze """
        while self.stack:
            x, y = self.stack.pop()  # Get current coordinates
            for direction in config.PIPE_DIRECTIONS[self.maze[x][y]]:
                nx, ny = x + direction.value[0], y + direction.value[1]
                # Check if we can move to new position
                if self.can_move((nx, ny), direction):

                    # If next position is not visited, update variables and continue search
                    if (nx, ny) not in self.visited:
                        self.update_vars(
                            (x, y), (nx, ny)
                        )
                        break

                    # if next position is visited, generate cycle
                    elif self.tracker[(x, y)] != (nx, ny):
                        self.generate_cycle((x, y), (nx, ny))
                        return

        raise ValueError("No cycle found")

    def can_move(self, new_pos: Tuple[int, int], direction: Tuple[Tuple[int, int], Tuple[int, int]]) -> bool:
        """ Check if we can move to new position """

        x, y = new_pos
        maze_height = len(self.maze)
        maze_width = len(self.maze[0]) if maze_height > 0 else 0

        # Check new position is NOT greater then maze
        if 0 <= x < maze_height and 0 <= y < maze_width:
            # Check if cell in allowed directions
            if self.maze[x][y] in config.PIPE_DIRECTIONS:
                # Check reverse direction
                if config.REVERSE_MAP[direction] in config.PIPE_DIRECTIONS[self.maze[x][y]]:
                    return True
        return False

    def update_vars(self, pos: Tuple[int, int] | None, new_pos: Tuple[int, int]):
        """ Function to update variables"""

        self.stack.append(new_pos)
        self.visited.add(new_pos)
        self.tracker[new_pos] = pos

    def generate_cycle(self, pos: Tuple[int, int], new_pos: Tuple[int, int]):
        """ Generate cycle to move from pos to new_pos """

        self.cycle = [new_pos]
        while pos != new_pos:
            self.cycle.append(pos)
            pos = self.tracker[pos]

    def get_steps_count(self) -> int:
        """ Returns number of steps to exit maze """

        return len(self.cycle) // 2

    def display(self) -> str:
        """ Display maze by print function and return string """

        for i, row in enumerate(self.maze):
            for j, cell in enumerate(row):
                if (i, j) not in self.cycle:
                    self.maze[i][j] = "·"

        display_string = ""
        for row in self.maze:
            display_string += "".join(row) + "\n"
        print(display_string)
        return display_string

    def get_area(self) -> int:
        """
        Shoelace area formula

        j = i + 1

        area = abs((∑ (x[i] * y[j]) - (x[j] * y[i])) / 2)

        - x[i] = x-coordinate of i vertex,
        - x[j] = x-coordinate of j vertex,
        - y[i] = y-coordinate of i vertex,
        - y[j] = y-coordinate of j vertex,

        """

        area = 0
        n = len(self.cycle)
        # SUM loop
        for i in range(n):
            j = (i + 1) % n  # Using this we will never go beyond the list
            area += (self.cycle[i][0] * self.cycle[j][1]) - (self.cycle[j][0] * self.cycle[i][1])  # formula
        area = abs(area) // 2
        return area - n // 2 + 1  # Adjust the calculated area interior holes
