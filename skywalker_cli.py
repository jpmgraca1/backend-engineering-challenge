import sys
import utils
import fileJedi
import business

if not utils.verifyArgumentsNumber(len(sys.argv)):
    sys.exit()

inputFileName = utils.extractFileName(sys.argv[1])
windowSize = utils.extractWindowSize(sys.argv[2])

if inputFileName is None or windowSize is None:
    sys.exit()

if not fileJedi.isCorrectFormat(inputFileName):
    sys.exit()

business.CalculateAverageTimes(inputFileName, windowSize)
