import unittest
import unittest.mock as mock
import FAQscript

class TestFAQScript(unittest.TestCase):

    @mock.patch('FAQscript.ref_question_log')
    @mock.patch('FAQscript.ref_history')
    @mock.patch('FAQscript.check_FAQ', return_value=(True, 'Customer support'))
    def test_process_question(self, mock_check_FAQ, mock_ref_history, mock_ref_question_log):
        # Mock event object
        class Event:
            def __init__(self, data, path):
                self.data = data
                self.path = path

        event = Event({
            'FAQ_status': 'FAQ',
            'processed': True,
            'question': 'What is the functionality of app?',
            'user_id': '0002'
        }, '/some_path')

        FAQscript.process_question(event.data, event.path)

        # Assert that the update function was called on ref_question_log
        mock_ref_question_log.child().update.assert_called()

        # Assert that the push function was called on ref_history
        mock_ref_history.child().push.assert_called()


if __name__ == "__main__":
    unittest.main()
