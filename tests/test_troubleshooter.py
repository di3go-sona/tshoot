import unittest
from unittest.mock import patch
from tshoot.troubleshooter import Troubleshooter

class TestTroubleshooter(unittest.TestCase):
    def setUp(self):
        self.troubleshooter = Troubleshooter()

    def test_add_new_message(self):
        self.troubleshooter._add_new_message("user", "Hello")
        self.assertEqual(len(self.troubleshooter.messages), 2)
        self.assertEqual(self.troubleshooter.messages[-1]["role"], "user")
        self.assertEqual(self.troubleshooter.messages[-1]["content"], "Hello")

    def test_add_message_part(self):
        self.troubleshooter._add_new_message("assistant", "How can I help you?")
        self.troubleshooter._add_message_part("I'm experiencing an issue.")
        self.assertEqual(len(self.troubleshooter.messages), 2)
        self.assertEqual(self.troubleshooter.messages[-1]["role"], "assistant")
        self.assertEqual(self.troubleshooter.messages[-1]["content"], "How can I help you?I'm experiencing an issue.")

    @patch("tshoot.troubleshooter.OpenAI")
    def test_run(self, mock_openai):
        # Mock the OpenAI client
        mock_client = mock_openai.return_value
        mock_completion = mock_client.chat.completions.create.return_value
        mock_completion.choices = [{"delta": {"content": "Sure, I can help with that."}}]

        # Add user message
        self.troubleshooter._add_new_message("user", "Can you troubleshoot my problem?")
        
        # Call the _run method and get the response
        response = list(self.troubleshooter._run())

        # Assert the response
        self.assertGreater(len(response), 1)

    def test_ask(self):
        # Add user message
        self.troubleshooter._add_new_message("user", "Can you troubleshoot my problem?")
        
        # Call the ask method and get the response
        response = self.troubleshooter.ask("What seems to be the issue?")

        # Assert the response
        self.assertGreater(len(list(response)), 1)

if __name__ == '__main__':
    unittest.main()