#!/usr/bin/env python


with open("../input/2/input_test", "r") as f:
    lines = f.readlines()

reports = [[int(level) for level in i.replace("\n", "").split(" ")] for i in lines]
# print(reports)

good_reports = []

def check_report(report):
    freepass_used = False

    sorted_report = sorted(report)

    if report != sorted_report[::-1] and report != sorted_report:
        return False

    for i in range(len(report)-1):
        diff = sorted_report[i+1] - sorted_report[i]
        if 0 < diff < 4:
            continue
        if not freepass_used:
            freepass_used = True
            check_report(sorted_report[:i+1] + sorted_report[:i+2])

    return False


for report in reports:
    if check_report(report):
        good_reports.append(reports)

print("----")
for i in good_reports:
    print(i)
