import re

def process_instructions(text):
    pattern = re.compile(r'''
        (?P<do>do\(\))                      |
        (?P<dont>don't\(\))                 |
        (?P<mul>mul\((?P<x>\d+),(?P<y>\d+)\))
    ''', re.VERBOSE)
    total = 0
    enabled = True
    for match in pattern.finditer(text):
        if match.group('do'):
            enabled = True
        elif match.group('dont'):
            enabled = False
        elif match.group('mul') and enabled:
            x = int(match.group('x'))
            y = int(match.group('y'))
            total += x * y
    return total

def extract_and_multiply(text):
    return process_instructions(text)

def extract_and_multiply_all(text):
    pattern = re.compile(r'mul\((\d+),(\d+)\)')
    matches = pattern.findall(text)
    total = sum(int(x) * int(y) for x, y in matches)
    return total

# Esempio di utilizzo
with open('day3.txt', 'r') as file:
    data = file.read()

result_part1 = extract_and_multiply_all(data)
print("Result Part 1: ", result_part1)

result_part2 = process_instructions(data)
print("Result Part 2: ", result_part2)
