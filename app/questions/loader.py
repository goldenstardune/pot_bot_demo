import json
import random
from pathlib import Path

QUESTIONS_FILE = Path(__file__).parent / "cyber_questions.json"

_questions = None

def load_questions():
    global _questions
    if _questions is None:
        with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
            _questions = json.load(f)
    return _questions

def get_random_question():
    questions = load_questions()
    return random.choice(questions)
