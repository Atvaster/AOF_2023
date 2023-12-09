def find_next(row):
    return 0 if all(num == 0 for num in row) else row[0] - find_next([b - a for a, b in zip(row, row[1:])])


with open("Day_9/Data/input.txt") as file:
    rows = [list(map(int, row.split())) for row in file.read().split("\n")]
total = 0

for row in rows:
    print(find_next(row))
    total += find_next(row)
print(total)