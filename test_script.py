import unittest
import FAQscript

class TestScript(unittest.TestCase):

    def test_check_FAQ(self):
        question = "Тестовый вопрос"
        result = FAQscript.check_FAQ(question)
        self.assertIsInstance(result, tuple) # проверка, что функция возвращает кортеж
        self.assertEqual(len(result), 2) # проверка, что кортеж содержит два элемента

    def test_process_question(self):
        event = {'data': {'question': 'Тестовый вопрос', 'processed': False}}
        self.assertIsNone(FAQscript.process_question(event))

if __name__ == '__main__':
    unittest.FAQscript()
