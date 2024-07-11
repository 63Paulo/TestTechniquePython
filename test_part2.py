def findSimilarBoxes(ids_box):
    # Get the total number of box IDs
    n = len(ids_box)
    
    # Iterate through each pair of box IDs
    for i in range(n):
        for j in range(i + 1, n):
            cpt_diff = 0
            index_diff = -1
            diff_letters = [] # List to store the differing characters

            # Iterate through each character of the box IDs
            for k in range(len(ids_box[i])):
                if ids_box[i][k] != ids_box[j][k]:
                    cpt_diff += 1
                    index_diff = k
                    diff_letters.append((ids_box[i][k], ids_box[j][k]))
                if cpt_diff > 1:
                    break
            if cpt_diff == 1:
                box1 = ids_box[i]
                box2 = ids_box[j]
                common_letters = box1[:index_diff] + box1[index_diff +1:]
                return box1, box2, diff_letters, common_letters

# Reading box IDs from the file
with open('input.txt', 'r') as file:
    box_ids = file.read().splitlines()

# Find and display the similar boxes and the letters that are different
box1, box2, diff_letters, common_letters = findSimilarBoxes(box_ids)
print(f"Similar boxes : {box1} and {box2}")
print(f"Letters that differ : {diff_letters}")
print(f"Common_letters : {common_letters}")