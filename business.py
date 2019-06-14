import fileJedi


def CalculateAverageTimes(inputFileName, windowSize):
    events = fileJedi.getEvents(inputFileName)

    # Build Output List
    print(events)
