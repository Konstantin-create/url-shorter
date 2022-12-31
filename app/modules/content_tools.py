import json


def get_content() -> dict:
    """Function to get content"""

    return json.load(open('app/data/content.json', 'r'))
