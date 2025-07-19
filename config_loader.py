import json
import os


def load_rules(config_path: str = None) -> dict:
    base_dir = os.path.dirname(__file__)
    if config_path:
        path = os.path.abspath(config_path)
        if os.path.isfile(path):
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
    # Load default_rules.json
    default_path = os.path.join(base_dir, 'rules', 'default_rules.json')
    with open(default_path, 'r', encoding='utf-8') as file:
        return json.load(file)