# Parse json and make a list of all coordinates attached to type geo objects
# We don't need to check if type == "geo" to attach coords. That's why we just collect all "coords" in input data.
import json
data = '{"foo": {"type": "geo", "coords": [2, 3], "children": [{"type": "geo", "coords": [4, 1], "children": [{"type": "bar", "children": [{"type": "geo", "coords": [8, 4]}]}, {"type": "geo", "coords": [3, 2]}]}]}}'
parsed_json = json.loads(data)


def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == key:
                    arr.append(v)
                elif isinstance(v, (dict, list)):
                    extract(v, arr, key)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values


print(json_extract(parsed_json, "coords"))
