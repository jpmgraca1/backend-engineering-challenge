import sys


def verifyArgumentsNumber(numberOfArguments):
    if numberOfArguments != 3:
        print("USAGE: python skywalker_cli.py <input_file.json> <window size>")
        return False
    return True


def extractFileName(fileName):
    if not fileName.endswith(".json"):
        print("WARNING: The provided file name was not in the expected format")
        return None
    return fileName


def extractWindowSize(windowSize):
    try:
        value = int(windowSize)
        return value
    except ValueError:
        print("WARNING: The window size must be an int (number of minutes)")
        return None
