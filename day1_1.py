from pathlib import Path

file = Path("input_1")
first_column = []
second_column = []
distance = 0

for line in file.read_text().strip().splitlines():
    x, y = line.split("   ")
    first_column.append(int(x))
    second_column.append(int(y))

first_column.sort()
second_column.sort()

for x, y in zip(first_column, second_column):
    distance += abs(x - y)

print(distance)
