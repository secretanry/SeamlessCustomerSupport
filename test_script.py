from unittest import TestCase
import FAQscript

class FAQScriptTests(TestCase):
    def test_process_question(self):
        # Создание словаря данных для тестирования
        question_data = {
            'question': 'What is your app?',
            'user_id': '123',
            'processed': False,
        }
        path = '/123'

        # Вызов функции с тестовыми данными
        result = FAQscript.process_question(question_data, path)

        # Проверка результатов
        self.assertIsNone(result)

