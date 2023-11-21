"""Troubleshooter class to troubleshoot a problem with a given prompt and model"""
from typing import Optional

from openai import OpenAI

from .config import settings
from .prompts import SimplePrompt


class Troubleshooter:
    def __init__(
        self, prompt: Optional[SimplePrompt] = None, model: Optional[str] = None
    ):
        self.prompt = prompt or SimplePrompt
        self.model = model or "gpt-3.5-turbo"
        self.client = OpenAI(
            # defaults to os.environ.get("OPENAI_API_KEY")
            api_key=settings.OPENAI_API_KEY,
        )
        self.messages: list[dict[str, str]] = []

    def _run(self):
        chat_completion = self.client.chat.completions.create(
            messages=self.messages,
            model=self.model,
        )
        answer = chat_completion.choices[0]
        answer_text = answer.message.content
        self.messages.append(
            {
                "role": "assistant",
                "content": answer_text,
            }
        )
        return answer_text

    def troubleshoot(self, problem: str):
        """Troubleshoot a problem with the given prompt and model"""
        self.messages = [
            {
                "role": "system",
                "content": self.prompt.system,
            },
            {
                "role": "user",
                "content": self.prompt.user.format(problem=problem),
            },
        ]
        return self._run()

    def ask(self, question: str):
        """Ask a question to help troubleshoot the problem with the given prompt and model"""
        self.messages.append(
            {
                "role": "user",
                "content": question,
            }
        )
        return self._run()
