# import NumPy as np
from collections import defaultdict
from stringToIntList import *

if __name__ == "__main__":
    inputFilePath = "2025_Problem_C_Data\summerOly_programs.csv"
    outputFilePath = "sportCode.csv"
    data = stringToInt(inputFilePath, 2)
    printToFile(outputFilePath, data, printToScreen=True)
        
        