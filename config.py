import json


def load_config(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def save_config(filename, config):
    with open(filename, 'w') as f:
        json.dump(config, f, indent=4)
