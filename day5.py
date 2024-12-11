import collections


def parse_input(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    rules_section, updates_section = content.strip().split('\n\n')
    rules = []
    for line in rules_section.strip().split('\n'):
        if line:
            x, y = map(int, line.strip().split('|'))
            rules.append((x, y))
    updates = []
    for line in updates_section.strip().split('\n'):
        if line:
            update = list(map(int, line.strip().split(',')))
            updates.append(update)
    return rules, updates

def is_update_valid(update, rules):
    index_map = {page: idx for idx, page in enumerate(update)}
    update_set = set(update)
    for x, y in rules:
        if x in update_set and y in update_set:
            if index_map[x] > index_map[y]:
                return False
    return True

def reorder_update(update, rules):
    update_set = set(update)
    graph = {page: set() for page in update}
    in_degree = {page: 0 for page in update}
    for x, y in rules:
        if x in update_set and y in update_set:
            graph[x].add(y)
            in_degree[y] += 1
    queue = collections.deque([node for node in update if in_degree[node] == 0])
    sorted_update = []
    while queue:
        node = queue.popleft()
        sorted_update.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    if len(sorted_update) != len(update):
        return None  # Ciclo trovato, impossibile ordinare
    return sorted_update

rules, updates = parse_input('day5.txt')
total = 0
for update in updates:
    if is_update_valid(update, rules):
        middle_index = len(update) // 2
        middle_page = update[middle_index]
        total += middle_page
print("Sum of pages with correct update:", total)
total2 = 0
for update in updates:
    if not is_update_valid(update, rules):
        reordered_update = reorder_update(update, rules)
        if reordered_update:
            middle_index = len(reordered_update) // 2
            middle_page = reordered_update[middle_index]
            total2 += middle_page
print("Sum of ordered pages with correct update:", total2)
