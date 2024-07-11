def countBoxes(ids_box):

    # Counter inisialisation
    cpt_two_letters = 0
    cpt_three_letters = 0

    # Creation of a dictionary to count the frequency of each letter
    for id_box in ids_box:
        cpt_letters = {}
        for letter in id_box:
            if letter in cpt_letters:
                cpt_letters[letter] += 1
            else : 
                cpt_letters[letter] = 1
 
        # Initializing Boolean variables
        two_letters = False
        three_letters = False

        # Checking the conditions of two or three letters
        for count in cpt_letters.values():
            if count == 2:
                two_letters = True
            if count == 3 :
                three_letters = True

        # Counting the number of boxes with 2 or 3 similar letters
        if two_letters :
            cpt_two_letters += 1
        if three_letters :
            cpt_three_letters += 1
    
    # Checksum calculation
    checksum = cpt_two_letters * cpt_three_letters
    return cpt_two_letters, cpt_three_letters, checksum

# Reading box IDs from the file
with open('input.txt', 'r') as file:
    ids_box = file.read().splitlines()

# Calculating and displaying the results 
cpt_two, cpt_three, checksum = countBoxes(ids_box)
print(f"Box that contains exatcly two same letters : {cpt_two}")
print(f"Box that contains exatcly three same letters : {cpt_three}")
print(f"Checksum : {checksum}")


