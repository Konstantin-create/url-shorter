import json


def get_content() -> dict:
    """Function to get content"""

    return json.load(open('data/content.json', 'r'))
