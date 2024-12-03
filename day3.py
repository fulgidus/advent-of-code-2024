import re

def extract_and_multiply(text):
    pattern = re.compile(r'''
        (?P<do>do\(\))             |
        (?P<dont>don't\(\))        |
        (?P<mul>mul\((\d+),(\d+)\))
    ''', re.VERBOSE)
    total = 0
    enabled = True
    for match in pattern.finditer(text):
        if match.group('do'):
            enabled = True
        elif match.group('dont'):
            enabled = False
        elif match.group('mul') and enabled:
            x = int(match.group(2))
            y = int(match.group(3))
            total += x * y
    return total

# Esempio di utilizzo
with open('day3.txt', 'r') as file:
    data = file.read()

result = extract_and_multiply(data)
print("Result: ", result)
