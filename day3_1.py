from pathlib import Path
import re
import operator

filepath = "input_3"


def get_digits(input_string: str) -> list[list[int]]:
    return [
        [int(string_a), int(string_b)]
        for string_a, string_b in (re.findall(r"mul\((\d+),(\d+)\)", input_string))
    ]


def sum_up_digits(digits_list: list[list[int]]) -> int:
    result = 0
    for digit_a, digit_b in digits_list:
        result += operator.mul(digit_a, digit_b)
    return result


reports = Path(filepath).read_text()
digits_list = get_digits(reports)
print(sum_up_digits(digits_list))
