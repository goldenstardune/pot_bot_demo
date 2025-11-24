import random
from typing import Tuple

#captcha matematyczna
_captcha_storage = {}

def generate_captcha(tg_id: int) -> Tuple[str, int]:
    a = random.randint(10, 50)
    b = random.randint(10, 50)
    answer = a + b
    question = f"Prove you're not a robot:\n{a} + {b} = ?"
    
    _captcha_storage[tg_id] = answer
    return question, answer

def verify_captcha(tg_id: int, user_answer: str) -> bool:
    try:
        correct = _captcha_storage.get(tg_id)
        if correct is None:
            return False
        return correct == int(user_answer)
    except ValueError:
        return False
    finally:
        _captcha_storage.pop(tg_id, None)