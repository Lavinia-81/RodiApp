import json


def read_config(path: str = "./utils/config.json"):
    with open(path, 'r') as f:
        data = json.loads(f.read())

    return data


config = read_config()

