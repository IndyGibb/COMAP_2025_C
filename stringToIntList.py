import os
from typing import List

def stringToInt(filePath: str, location: int, fileDelimiter: str = ',', header: bool = True) -> List[str]:
    
    strings = []
    i = 0;
    with open(filePath, 'r') as file:
        if header: 
                next(file) # Skip header line if present
        for line in file:
            line = line.strip()
            data = line.split(sep=fileDelimiter)
            if data[location] not in strings:
                strings.append(data[location])
                i += 1
        file.close()
    return strings



def printToFile(filePath: str, data: List[str], fileDelimiter: str = ',', printToScreen: bool = False):
    with open(filePath, 'w') as file:
        i = 0
        for item in data:
            file.write(str(i) + fileDelimiter + item + '\n')
            if printToScreen:
                print(str(i) + fileDelimiter + item)
            i += 1
        print("Data written to file successfully")
        file.close()
    return


if __name__ == "__main__":
    inputFilePath = "2025_Problem_C_Data\summerOly_athletes.csv"
    outputFilePath = "countryCode.csv"
    data = stringToInt(inputFilePath, 3)
    printToFile(outputFilePath, data, printToScreen=True)
        
        