class InputGrid:
    def __init__(self, input_data):
        self.data = input_data
        self.height = len(input_data)
        self.width = len(input_data[0]) - 1
        self.grid_dict = {(y, x): input_data[y][x] for y in range(self.height) for x in range(self.width)}
        self.positions = [(py, px) for py in [-1, 0, 1] for px in [-1, 0, 1] if (px != 0 or py != 0)]


def getSolutionPart1(input_data):
    input_grid = InputGrid(input_data)
    count = 0
    for y, x in input_grid.grid_dict:
        for py, px in input_grid.positions:
            possible_match = "".join(input_grid.grid_dict.get((y + py * i, x + px * i), "") for i in range(len('XMAS')))
            if possible_match == "XMAS":
                count += 1
    print("XMAS count:", count)


def getSolutionPart2(input_data):
    input_grid = InputGrid(input_data)
    count = 0
    for y, x in input_grid.grid_dict:
        if input_grid.grid_dict[y, x] == "A":
            lr = input_grid.grid_dict.get((y - 1, x - 1), "") + input_grid.grid_dict.get((y + 1, x + 1), "")
            rl = input_grid.grid_dict.get((y - 1, x + 1), "") + input_grid.grid_dict.get((y + 1, x - 1), "")
            count += {lr, rl} <= {"MS", "SM"}
    print("X-MAS:", count)


def start(input_file, part) -> None:
    with open(input_file, mode="r") as f:
        file_input = f.readlines()

    print(f'Running solution for part {part}')

    if part == 'part1':
        print(getSolutionPart1(file_input))
    else:
        print(getSolutionPart2(file_input))
