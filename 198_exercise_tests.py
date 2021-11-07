import unittest
from files import test_exercise_random_answer

class TestClass(unittest.TestCase):
    def test_correct_input(self):
        user_choice = 1
        answer = 1
        result = test_exercise_random_answer.continue_input(user_choice, answer)
        self.assertFalse(result)
    
    
    def test_none_input(self):
        user_choice = 5
        answer = 1
        result = test_exercise_random_answer.continue_input(user_choice, answer)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
