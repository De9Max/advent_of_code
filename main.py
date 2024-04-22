import datetime

from maze import Maze


def main():

    with open("input.txt") as f:
        maze_string = f.read()

    start_time = datetime.datetime.now()
    solve = Maze(maze_string)
    print("Task1 answer:", solve.get_steps_count())
    print("Task2 answer:", solve.get_area())
    print(datetime.datetime.now() - start_time)

    with open("output.txt", "w") as f:
        f.write(solve.display())


if __name__ == '__main__':
    main()
