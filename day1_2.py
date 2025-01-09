from pathlib import Path

file = Path("input_1")

def get_columns(file):
    first_column = []
    second_column = []
    for line in file.read_text().strip().splitlines():
        x, y = line.split('   ')
        first_column.append(int(x))
        second_column.append(int(y))
    return first_column, second_column

def calc_similarity_score(first_column, second_column):
    similarity_score = 0
    for number in first_column:
        nb_count = second_column.count(number)
        similarity_score += number*nb_count
    return similarity_score 

def calc_similarity_score_memo(first_column, second_column):
    similarity_score = 0
    memo ={}
    for number in first_column:
        if number in memo:
            nb_count = memo[number]
        else:
            nb_count = second_column.count(number)
            memo[number] = nb_count
        similarity_score += number * nb_count
    return similarity_score 
    

first_column, second_column = get_columns(file)

print(calc_similarity_score(first_column, second_column) == calc_similarity_score_memo(first_column, second_column))
