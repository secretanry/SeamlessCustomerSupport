import unittest
import FAQscript

class TestFAQscript(unittest.TestCase):
    def test_process_question(self):
        question_data = {
            'question': 'What is your app?',
            'processed': False
        }
        path = '/random_path/'

        result = FAQscript.process_question(question_data, path)
        
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()

