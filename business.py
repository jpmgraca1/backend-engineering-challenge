import fileJedi
from datetime import datetime, timedelta


def calculateAverageTimes(inputFileName, windowSize):
    events = fileJedi.getEvents(inputFileName)

    # Sort the events by timeStamp
    events = sorted(events, key=lambda k: k['timestamp'])

    # Build Output List
    outputList = buildOutputList(events, windowSize)
    # print(events)


def buildOutputList(events, windowSize):
    # Get first minute to show
    getFirstMinute(events[0]['timestamp'])

    # Get last minute to show
    getLastMinute(events[len(events) - 1]['timestamp'], windowSize)

    # Build output list
    return None


def getFirstMinute(timeStamp):
    datetimeObject = datetime.strptime(timeStamp, '%Y-%m-%d %H:%M:%S.%f')
    datetimeObject = datetimeObject.replace(second=0, microsecond=0)
    return datetimeObject


def getLastMinute(timeStamp, windowSize):
    datetimeObject = datetime.strptime(timeStamp, '%Y-%m-%d %H:%M:%S.%f')
    datetimeObject = datetimeObject.replace(second=0, microsecond=0)
    datetimeObject = datetimeObject + timedelta(0, 60 * windowSize)
    return datetimeObject
