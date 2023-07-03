import json


def load_json(file_path: str) -> list[dict]:
    """
    Load data from json file
    :param file_path: str - path to json file
    :return: list[dict] - list of dictionaries with data
    """

    with open(file_path, 'r') as json_file:
        data: list[dict] = json.load(json_file)
    return data
