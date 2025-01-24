from stringToIntList import *

if __name__ == "__main__":
    inputFilePath = "sportCode2.csv"
    outputFilePath = "sport.csv"
    data = stringToInt(inputFilePath, 1)
    printToFile(outputFilePath, data, printToScreen=True)