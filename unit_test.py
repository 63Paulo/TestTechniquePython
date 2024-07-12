import unittest # Import the unit test framework
import test_part2 # Import the similar boxes function
import test_part1 # Import the count boxes function

# Test class for the first part
class TestCountBoxes(unittest.TestCase):

    # Initialize the example list
    def testExemple(self):
        ids_box = [
            "abcdef",
            "bababc",
            "abbcde",
            "abcccd",
            "aabcdd",
            "abcdee",
            "ababab"
        ]

        # Initialize the excepted variables
        excepted_cpt_two = 4
        excepted_cpt_three = 3
        excepted_checksum = 12

        # Using the count boxes functon
        cpt_two_letters, cpt_three_letters, checksum = test_part1.countBoxes(ids_box)

        # Test if the excepted values are equal to the values find by the function
        self.assertEqual(cpt_two_letters, excepted_cpt_two)
        self.assertEqual(cpt_three_letters, excepted_cpt_three)
        self.assertEqual(excepted_checksum, checksum)

    # Test function if no boxes contains two or three letters
    def noBoxes(self):
        ids_box = [
            "abcdef",
            "ghijkl",
            "mnopqr"
        ]
        excepted_cpt_two = 0
        excepted_cpt_three = 0
        excepted_checksum  = 0
        cpt_two_letters, cpt_three_letters, checksum = test_part1.countBoxes(ids_box)
        self.assertEqual(cpt_two_letters, excepted_cpt_two)
        self.assertEqual(cpt_three_letters, excepted_cpt_three)
        self.assertEqual(checksum,  excepted_checksum)


    # Test function to verify if a box which contains several two or three letters only count once 
    def coutOnce(self):
        ids_box = [
            "aabbcc",
            "ddeeff",
            "ggghhh",
            "iiijjj"
        ]
        excepted_cpt_two = 2
        excepted_cpt_three = 2
        excepted_checksum = 4
        cpt_two_letters, cpt_three_letters, checksum = test_part1.countBoxes(ids_box)
        self.assertEqual(cpt_two_letters, excepted_cpt_two)
        self.assertEqual(cpt_three_letters,  excepted_cpt_three)
        self.assertEqual(checksum, excepted_checksum)

    # Test function if there is boxes that contain only two or only three similar letters
    def onlyThreeOrTwoLetters(self):
        ids_box = [
            "aabbcc",
            "ddeeff",
            "gghhii",
            "jjkkll"
        ]
        excepted_cpt_two  = 4
        excepted_cpt_three = 0
        excepted_checksum = 0
        cpt_two_letters, cpt_three_letters, checksum = test_part1.countBoxes(ids_box)
        self.assertEqual(cpt_two_letters, excepted_cpt_two)
        self.assertEqual(cpt_three_letters, excepted_cpt_three)
        self.assertEqual(checksum,  excepted_checksum)


# Test class for the second part
class TestFindSimilarBoxes(unittest.TestCase):

    # Initialize the example list
    def testExemple(self):
        ids_box = [
            "abcde",
            "fghij",
            "klmno",
            "pqrst",
            "fguij",
            "axcye",
            "wvxyz"
        ]

        # Initialize the excepted variables
        excepted_box1 = "fghij"
        excepted_box2 = "fguij"
        diff_letters_excepted = [('h', 'u')]
        common_letters_excepted = "fgij"

        # Using the find similar boxes functon
        box1, box2, diff_letters, common_letters = test_part2.findSimilarBoxes(ids_box)

        # Test if the excepted values are equal to the values find by the function
        self.assertEqual(box1, excepted_box1)
        self.assertEqual(box2, excepted_box2)
        self.assertEqual(diff_letters, diff_letters_excepted)
        self.assertEqual(common_letters, common_letters_excepted)

    # Test function if no boxes are similar 
    def noSimilarBoxes(self):
        ids_box = [
            "abcde",
            "fghij",
            "klmno",
            "pqrst",
            "axcye",
            "wvxyz"
        ]
        result = test_part2.findSimilarBoxes(ids_box)

        # Verify that no boxes are similar
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()