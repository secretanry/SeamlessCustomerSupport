import unittest
import FAQscript  # убедитесь, что ваш скрипт называется FAQscript.py

class TestFAQscript(unittest.TestCase):
    def test_process_question(self):
        question_data = {
            'question': 'What is your app?',
            'processed': False
        }
        path = '/random_path/'

        # функция process_question теперь возвращает результат
        result = FAQscript.process_question(question_data, path)
        
        # в этом примере мы просто проверяем, что результат - None, т.к. функция не предусматривает возвращаемого значения
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()

