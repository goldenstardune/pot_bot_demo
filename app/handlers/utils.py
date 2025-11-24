import re

def is_valid_name(text: str) -> bool:
    if not text or len(text.strip()) < 2:
        return False
    pattern = r"[A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż\s\-'’]+"
    return bool(re.fullmatch(pattern, text.strip()))