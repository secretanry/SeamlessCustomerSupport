from unittest import TestCase, mock
import FAQscript

class FAQScriptTests(TestCase):

    @mock.patch('FAQscript.Event', autospec=True)
    def test_process_question(self, mock_event):
        mock_event.data = {
            'question': 'What is your app?',
            'user_id': '123',
            'processed': False,
        }
        mock_event.path = '/123'

        result = FAQscript.process_question(mock_event)

        # Проверка результатов
        self.assertIsNone(result)
