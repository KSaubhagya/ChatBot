import unittest
from nltk.chat.util import Chat
from chatbot import pairs, reflections  # Import chatbot logic

class TestChatbot(unittest.TestCase):

    def setUp(self):
        # Prepare chatbot for testing
        self.chat = Chat(pairs, reflections)

    def test_greeting(self):
        # Test input
        user_input = "hello"
        
        # Get chatbot response
        response = self.chat.respond(user_input)

        # Possible expected responses
        expected_responses = [
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?"
        ]

        # Assertion
        self.assertIn(response, expected_responses)

if __name__ == "__main__":
    unittest.main()
