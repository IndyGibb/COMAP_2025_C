from stringToIntList import *

if __name__ == "__main__":
    inputFilePath = "2025_Problem_C_Data\summerOly_athletes.csv"
    outputFilePath = "yearsChanger.csv"
    data = stringToInt(inputFilePath, 4)
    printToFile(outputFilePath, data, printToScreen=True)
        
        