# Reading data from file and checking if the reports are safe
safe_reports = 0
safe_reports_dampened = 0

def is_safe(levels: list) -> bool:
    differences = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    if all(1 <= d <= 3 for d in differences) or all(-3 <= d <= -1 for d in differences):
        return True
    return False

def count_safe_reports(lines):
    safe_reports = 0
    for line in lines:
        levels = list(map(int, line.strip().split()))
        if is_safe(levels):
            safe_reports += 1
    return safe_reports

def count_safe_dampened_reports(lines):
    safe_reports_dampened = 0
    for line in lines:
        levels = list(map(int, line.strip().split()))
        if is_safe(levels):
            safe_reports_dampened += 1
        else:
            for i in range(len(levels)):
                new_levels = levels[:i] + levels[i+1:]
                if len(new_levels) >= 2 and is_safe(new_levels):
                    safe_reports_dampened += 1
                    break
    return safe_reports_dampened

with open("day2.txt", "r") as file:
    lines = file.readlines()
    safe_reports = count_safe_reports(lines)
    safe_reports_dampened = count_safe_dampened_reports(lines)

print("Safe reports: ", safe_reports)
print("Safe dampened reports: ", safe_reports_dampened)