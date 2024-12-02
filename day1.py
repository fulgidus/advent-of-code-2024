# Reading data from file and checking if the reports are safe
with open('day1.txt', 'r') as file:
    lines = file.readlines()

# Initialize two lists to store the left and right numbers
left_list = []
right_list = []

# For each line, split it into two parts and add them to the lists
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

# Order the lists
left_list.sort()
right_list.sort()

# Calculate the total distance
total_distance = sum(abs(a - b) for a, b in zip(left_list, right_list))

from collections import Counter

right_counts = Counter(right_list)

# Calculate the similarity score
similarity_score = 0

for num in left_list:
    count_in_right = right_counts.get(num, 0)
    similarity_score += num * count_in_right

print("Distance: ", total_distance)
print("Similarity: ", similarity_score)