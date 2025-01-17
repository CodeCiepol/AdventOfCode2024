from pathlib import Path

filepath = "input_2"
reports = Path(filepath).read_text().splitlines()


def check_increasing(val, next_val, is_increasing):
    return (val < next_val) == is_increasing


def check_nb_diff(val, next_val):
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
        report_del_prev_index = report.copy()
        report_del_prev_index.pop(index-1)
        report_del_next_index = report.copy()
        report_del_next_index.pop(index+1)
        report.pop(index)
        index=0
        return check_report_rec(report, index) or check_report_rec(report_del_next_index, index) or check_report_rec(report_del_prev_index, index) 


    def check_report_rec(report, index=0, is_increasing=None):
        
        if is_increasing is None:
            is_increasing = report[index] < report[index + 1]
        
        if index >= len(report) - 1:
            return True

        if not check_increasing(report[index], report[index + 1], is_increasing):
            return notice_error(report,index)

        if not check_nb_diff(report[index], report[index + 1]):
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
