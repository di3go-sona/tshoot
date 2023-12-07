import unittest
from tshoot.config_helper import get_settings_fields, OpenAIKeyValidator, OPENAI_MODELS, PROMPTS

class TestConfigHelper(unittest.TestCase):
    def test_get_settings_fields(self):
        # Test with default values
        defaults = {
            "openai_api_key": "default_key",
            "model": "default_model",
            "prompt": "default_prompt",
            "user_icon": "default_user_icon",
            "assistant_icon": "default_assistant_icon",
            "verbose": True
        }
        expected_questions = [
            {
                "type": "input",
                "name": "openai_api_key",
                "message": "Insert the OpenAI API key",
                "validate": OpenAIKeyValidator,
                "default": "default_key",
            },
            {
                "type": "list",
                "name": "openai_model",
                "message": "Select the model you want to use",
                "choices": [
                    {
                        "name": f"{model_name}",
                        "value": model_name,
                    }
                    for model_name in OPENAI_MODELS
                ],
                "default": "default_model",
            },
            {
                "type": "list",
                "name": "prompt",
                "message": "Select the prompt you want to use",
                "choices": [
                    {
                        "key": prompt_name.lower()[0],
                        "name": f"{prompt_name}",
                        "value": prompt_name,
                        "description": prompt,
                    }
                    for prompt_name, prompt in PROMPTS.items()
                ],
                "default": "default_prompt",
            },
            {
                "type": "input",
                "name": "user_icon",
                "message": "What should the user terminal block look like?",
                "default": "default_user_icon",
            },
            {
                "type": "input",
                "name": "assistant_icon",
                "message": "What should the assistant terminal block look like?",
                "default": "default_assistant_icon",
            },
            {
                "type": "confirm",
                "name": "verbose",
                "message": "Do you want to print debug information?",
                "default": True,
            },
        ]

        result = get_settings_fields(defaults)
        self.assertEqual(result, expected_questions)

if __name__ == '__main__':
    unittest.main()