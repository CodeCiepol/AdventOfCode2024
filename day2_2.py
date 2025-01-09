from pathlib import Path

filepath = "input_2"
reports = Path(filepath).read_text().splitlines()


def is_const_increasing(val, next_val, is_increasing):
    return (val < next_val) == is_increasing


def is_diff_lower_than_three(val, next_val):
    return 0 < abs(val - next_val) < 4


def create_checker(toleration=1):
    failed_bad_level = 0 

    def notice_error(report, index):
        nonlocal failed_bad_level
        failed_bad_level += 1
        if failed_bad_level > toleration:
            return False
        else:
            return reset_report(report, index)
        

    def reset_report(report, index):
        report_witbehind = report.copy()
        report_witbehind.pop(index-1)
        report_witahead = report.copy()
        report_witahead.pop(index+1)
        report.pop(index)
        index=index-1
        # try with other index, maybe delete previous
        return check_report_rec(report, index) or check_report_rec(report_witbehind, index) or check_report_rec(report_witahead, index)


    def check_report_rec(report, index=0, is_increasing=None):
        
        if is_increasing is None:
            is_increasing = report[index] < report[index + 1]
        
        if index >= len(report) - 1:
            return True

        if not is_const_increasing(report[index], report[index + 1], is_increasing):
            return notice_error(report,index)

        if not is_diff_lower_than_three(report[index], report[index + 1]):
            return notice_error(report,index)
        
        return check_report_rec(report, index + 1, is_increasing)

    return check_report_rec


nb_correct_reports = 0
for report in reports:
    report = [int(x) for x in report.split()]
    check_report_rec = create_checker()
    if check_report_rec(report):
        nb_correct_reports += 1
print(nb_correct_reports)
