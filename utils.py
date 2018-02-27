import exercise as ex
import json

def load_json_as_string():
    filepath = 'data/winequality-red.json'
    with open(filepath) as jsonfile:
        ob = json.load(jsonfile)
        return json.dumps(ob)
