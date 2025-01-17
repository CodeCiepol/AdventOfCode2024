from pathlib import Path

filepath = "input_2"
reports = Path(filepath).read_text().splitlines()


def check_report(report):
    if report[0] < report[1]:
        operation = "inc"
    else:
        operation = "dec"

    for index, value in enumerate(report):
        if index + 1 == len(report):
            return True

        if report[index] < report[index + 1]:
            next_operation = "inc"
        else:
            next_operation = "dec"

        if abs(report[index] - report[index + 1]) > 3:
            return False

        if abs(report[index] - report[index + 1]) == 0:
            return False

        if next_operation != operation:
            return False


def check_increasing(val, next_val, is_increasing):
    return (val < next_val) == is_increasing


def check_nb_diff(val, next_val):
    return 0 < abs(val - next_val) < 4


def check_report_rec(report, index=0, is_increasing=None):
    if is_increasing is None:
        is_increasing = report[index] < report[index + 1]

    if index >= len(report) - 1:
        return True

    if not (check_increasing(report[index], report[index + 1], is_increasing)):
        return False

    if not (check_nb_diff(report[index], report[index + 1])):
        return False

    return check_report_rec(report, index + 1, is_increasing)


nb_correct_reports = 0
for report in reports:
    report = [int(x) for x in report.split()]
    if check_report_rec(report):
        nb_correct_reports += 1
print(nb_correct_reports)
