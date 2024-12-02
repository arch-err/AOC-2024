#!/usr/bin/env python


with open("../input/1/input", "r") as f:
    lines = f.readlines()

safe_reports = []
previous_level = 0


for line in lines:
    report_fail = False

    report = line.replace("\n", "").split(" ")
    report = [int(i) for i in report]

    sorted_report = sorted(report)
    if report != sorted_report and report != sorted_report[::-1]:
        continue

    for i in range(len(sorted_report)-1):
        diff = sorted_report[i+1] - sorted_report[i]
        if sorted_report[i] == 2:

        if diff > 3 or diff < 1:
            report_fail = True
            break

    if report_fail:
        continue

    safe_reports.append(report)

# for r in safe_reports:
#     print(r)
print(len(safe_reports))
