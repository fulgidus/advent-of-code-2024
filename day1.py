# Reading data from file and checking if the reports are safe
with open('day1.txt', 'r') as file:
    lines = file.readlines()

def calculate_distance_and_similarity(lines):
    left_list = []
    right_list = []
    for line in lines:
        if not line.strip():
            continue
        parts = line.strip().split()
        if len(parts) != 2:
            continue
        left_num = int(parts[0])
        right_num = int(parts[1])
        left_list.append(left_num)
        right_list.append(right_num)
    left_list.sort()
    right_list.sort()
    total_distance = sum(abs(a - b) for a, b in zip(left_list, right_list))
    from collections import Counter
    right_counts = Counter(right_list)
    similarity_score = 0
    for num in left_list:
        count_in_right = right_counts.get(num, 0)
        similarity_score += num * count_in_right
    return total_distance, similarity_score

# Calcola la distanza totale e il punteggio di similarità
total_distance, similarity_score = calculate_distance_and_similarity(lines)

print("Distance: ", total_distance)
print("Similarity: ", similarity_score)