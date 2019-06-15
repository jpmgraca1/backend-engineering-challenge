import fileJedi
from datetime import datetime, timedelta


def calculateAverageTimes(events, windowSize):
    # Sort the events by timeStamp
    events = sorted(events, key=lambda k: k['timestamp'])

    # Build Output List
    outputList = buildOutputList(events, windowSize)

    # Get the average times
    outputList = fillAverageTimes(events, windowSize, outputList)

    return outputList


def fillAverageTimes(events, windowSize, outputList):

    for result in outputList:
        result = getMinuteAverage(result, events, windowSize)

    return outputList


def getMinuteAverage(minuteResult, events, windowSize):
    # More info in the README.md file
    avg = 0.0
    avgWords = 0.0
    numberOfEvents = 0
    toRemove = []

    for event in events:
        eventTime = datetime.strptime(
            event['timestamp'], '%Y-%m-%d %H:%M:%S.%f')

        if eventTime >= minuteResult['date'] - timedelta(0, 60 * windowSize) and eventTime <= minuteResult['date']:
            avg = avg + event['duration']
            avgWords = avgWords + event['nr_words']
            numberOfEvents = numberOfEvents + 1
        elif eventTime < minuteResult['date'] - timedelta(0, 60 * windowSize):
            toRemove.append(events.index(event))

        elif eventTime > minuteResult['date']:
            break

    for index in toRemove:
        del events[index]

    if numberOfEvents > 0:
        minuteResult['average_delivery_time'] = (avg / numberOfEvents)
        minuteResult['average_words_translated'] = (avgWords / numberOfEvents)
        minuteResult['average_words_per_second'] = (avgWords / avg)

    return minuteResult


def buildOutputList(events, windowSize):
    # Get first minute to show
    firstMinute = getFirstMinute(events[0]['timestamp'])

    # Get last minute to show
    lastMinute = getLastMinute(
        events[len(events) - 1]['timestamp'], windowSize)

    # Build output list
    outputList = getOutputList(firstMinute, lastMinute)
    return outputList


def getOutputList(firstMinute, lastMinute):
    outputList = []
    index = 0

    while lastMinute >= firstMinute:
        outputList.insert(
            index, {'date': firstMinute, 'average_delivery_time': 0.0, 'average_words_translated': 0.0, 'average_words_per_second': 0.0})
        firstMinute = firstMinute + timedelta(0, 60)
        index = index + 1

    return outputList


def getFirstMinute(timeStamp):
    datetimeObject = datetime.strptime(timeStamp, '%Y-%m-%d %H:%M:%S.%f')
    datetimeObject = datetimeObject.replace(second=0, microsecond=0)
    return datetimeObject


def getLastMinute(timeStamp, windowSize):
    datetimeObject = datetime.strptime(timeStamp, '%Y-%m-%d %H:%M:%S.%f')
    datetimeObject = datetimeObject.replace(second=0, microsecond=0)
    datetimeObject = datetimeObject + timedelta(0, 60 * windowSize)
    return datetimeObject
