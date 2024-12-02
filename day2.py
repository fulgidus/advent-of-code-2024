# Reading data from file and checking if the reports are safe
safe_reports = 0
safe_reports_dampened = 0

def is_safe(levels: list) -> bool:
    differences = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    if all(1 <= d <= 3 for d in differences):
        return True
    elif all(-3 <= d <= -1 for d in differences):
        return True
    else:
        return False

with open("day2.txt", "r") as file:
    for line in file:
        levels = list(map(int, line.strip().split()))
        if (is_safe(levels)):
            safe_reports += 1

with open("day2.txt", "r") as file:
    for line in file:
        levels = list(map(int, line.strip().split()))
        if is_safe(levels):
            safe_reports_dampened += 1
        else:
            for i in range(len(levels)):
                new_levels = levels[:i] + levels[i+1:]
                if len(new_levels) >= 2 and is_safe(new_levels):
                    safe_reports_dampened += 1
                    break  # Found safe version of report

print("Safe reports: ", safe_reports)
print("Safe dampened reports: ",safe_reports_dampened)