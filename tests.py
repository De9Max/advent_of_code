from typing import Callable
from maze import Maze


def test(test_name: str, maze_string: str, option: Callable[[Maze], int], value: int, display_maze: bool = False):
    solve = Maze(maze_string)
    point = option(solve)
    assert point == value, "{}. Expected {} , got {}\n".format(test_name, value, point)
    success_string = "{} passed" if not display_maze else "{} passed.\nVisualization👇"
    print(success_string.format(test_name))
    if display_maze:
        solve.display()
    print("\n")


def task_one():
    maze_string = """.....\n.S-7.\n.|.|.\n.L-J.\n....."""
    test("First complex loop", maze_string, Maze.get_steps_count, 4, True)

    maze_string = """..F7.\n.FJ|.\nSJ.L7\n|F--J\nLJ..."""
    test("Second complex loop", maze_string, Maze.get_steps_count, 8, True)


def task_two():
    maze_string = """..........\n.S------7.\n.|F----7|.\n.||OOOO||.\n.||OOOO||.\n.|L-7F-J|.\n.|II||II|.\n.L--JL--J.\n.........."""
    test("First tiles test", maze_string, Maze.get_area, 4, False)

    maze_string = """.F----7F7F7F7F-7....\n.|F--7||||||||FJ....\n.||.FJ||||||||L7....\nFJL7L7LJLJ||LJ.L-7..\nL--J.L7...LJS7F-7L7.\n....F-J..F7FJ|L7L7L7\n....L7.F7||L7|.L7L7|\n.....|FJLJ|FJ|F7|.LJ\n....FJL-7.||.||||...\n....L---J.LJ.LJLJ..."""
    test("Second tiles test", maze_string, Maze.get_area, 8, False)

    maze_string = """FF7FSF7F7F7F7F7F---7\nL|LJ||||||||||||F--J\nFL-7LJLJ||||||LJL-77\nF--JF--7||LJLJ7F7FJ-\nL---JF-JLJ.||-FJLJJ7\n|F|F-JF---7F7-L7L|7|\n|FFJF7L7F-JF7|JL---7\n7-L-JL7||F7|L7F-7F7|\nL.L7LFJ|||||FJL7||LJ\nL7JLJL-JLJLJL--JLJ.L"""
    test("Third tiles test", maze_string, Maze.get_area, 10, False)


if __name__ == "__main__":
    task_one()
    task_two()
