from pathlib import Path
import re
import operator
from typing import Generator, Tuple, Optional

filepath = "input_3"


def filter_input(
    input_string: str,
) -> Generator[
    Tuple[Optional[str], Optional[str], Optional[int], Optional[int]], None, None
]:
    return (
        (
            disable_keyword or None,
            enable_keyword or None,
            int(number_1) if number_1 else None,
            int(number_2) if number_2 else None,
        )
        for disable_keyword, enable_keyword, number_1, number_2 in re.findall(
            r"(don\'t\(\))|(do\(\))|mul\((\d+),(\d+)\)", input_string
        )
    )


def sum_up_digits(
    filtered_text: Generator[
        Tuple[Optional[str], Optional[str], Optional[int], Optional[int]], None, None
    ],
) -> int:
    result = 0
    enable = True
    for disable_keyword, enable_keyword, number_a, number_b in filtered_text:
        if disable_keyword:
            enable = False
        if enable_keyword:
            enable = True
        if enable and number_a and number_b:
            result += operator.mul(number_a, number_b)
    return result


reports: str = Path(filepath).read_text()
filtered_reports = filter_input(reports)
print(sum_up_digits(filtered_reports))
