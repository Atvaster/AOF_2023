import numpy; import sys; lineLst = open(sys.argv[1:][0]).read().splitlines()

resultSum1 = sum([ind + 1 if all(([max([int(show[1]) for show in [tuple(cube.split(" ")[::-1]) for gameSet in line.split(": ")[1].split("; ") for cube in gameSet.split(", ")] if show[0] == color]) <= {"red":12, "green":13, "blue":14}[color] for color in {"red", "blue", "green"}])) else 0 for ind, line in enumerate(lineLst)])
resultSum2 = sum([numpy.prod(([max([int(show[1]) for show in [tuple(cube.split(" ")[::-1]) for gameSet in line.split(": ")[1].split("; ") for cube in gameSet.split(", ")] if show[0] == color]) for color in {"red", "blue", "green"}])) for ind, line in enumerate(lineLst)])
print(resultSum1, resultSum2)