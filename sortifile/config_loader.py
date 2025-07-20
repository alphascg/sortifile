import json
import os
import importlib.resources

def get_default_rules_path():
    project_root = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(project_root, 'rules', 'default_rules.json')

def load_rules(config_path: str = None) -> dict:
    base_dir = os.path.dirname(__file__)
    if config_path:
        path = os.path.abspath(config_path)
        if os.path.isfile(path):
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)

    # Lade eingebettete Datei aus dem Paket
    with importlib.resources.files('sortifile.rules').joinpath('default_rules.json').open('r', encoding='utf-8') as f:
        return json.load(f)