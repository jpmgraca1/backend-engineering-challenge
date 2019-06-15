import sys
import utils
import fileJedi
import business

try:
    if not utils.verifyArgumentsNumber(len(sys.argv)):
        sys.exit()

    inputFileName = utils.extractFileName(sys.argv[1])
    windowSize = utils.extractWindowSize(sys.argv[2])

    if inputFileName is None or windowSize is None:
        sys.exit()

    if not fileJedi.isCorrectFormat(inputFileName):
        sys.exit()

    events = fileJedi.getEvents(inputFileName)

    outputList = business.calculateAverageTimes(events, windowSize)

    fileJedi.writeOutputFile(outputList, "Results.json")

except Exception as e:
    print("An unexpected error has occurred")
    print(e)
