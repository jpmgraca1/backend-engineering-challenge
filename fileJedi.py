import json
from pathlib import Path


def isCorrectFormat(fileName):
    path = Path(fileName)
    if path.exists():
        data = path.read_text()
        try:
            jsonObject = json.loads(data)
            return True
        except ValueError:
            print("The json file provided is not on the correct format.")
    return False


def getEvents(fileName):
    path = Path(fileName)
    data = path.read_text()
    jsonObject = json.loads(data)
    return jsonObject
