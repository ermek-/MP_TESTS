import json
import random
import string
from pathlib import Path


def _generate_value(token: str):
    if token == "{{randomNumber}}":
        return ''.join(random.choices(string.digits, k=8))
    if token == "{{randomInt}}":
        return random.randint(0, 1000)
    if token == "{{randomUserName}}":
        return 'user_' + ''.join(random.choices(string.ascii_lowercase, k=8))
    if token == "{{randomStreetAddress}}":
        street = random.choice(['Main', 'Oak', 'Elm', 'Pine'])
        return f"{random.randint(1, 9999)} {street} St"
    if token == "{{randomLastName}}":
        return random.choice(['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'])
    return token


def _fill_placeholders(obj):
    if isinstance(obj, dict):
        return {k: _fill_placeholders(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_fill_placeholders(v) for v in obj]
    if isinstance(obj, str) and obj.startswith('{{') and obj.endswith('}}'):
        return _generate_value(obj)
    return obj


def load_payload(path):
    path = Path(path)
    with path.open() as f:
        data = json.load(f)
    return _fill_placeholders(data)