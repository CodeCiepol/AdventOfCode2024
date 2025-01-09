input_file_location = "input_1"
first_column = []
second_column = []
distance = 0

f = open(input_file_location, "r")
for line in f.readlines():
    x,y = line.split('   ')
    first_column.append(int(x))
    second_column.append(int(y))

first_column.sort()
second_column.sort()

for x,y in zip(first_column,second_column):
    distance += abs(x-y)

print(distance)