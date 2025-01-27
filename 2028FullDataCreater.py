import numpy as np
from dataCreate import dictGet
from typing import List
from collections import defaultdict

def listGet(filePath: str, location: int, fileDelimiter: str = ',', header: bool = True) -> List[int]:
    list = [];
    with open(filePath, 'r') as f:
        if header:
            next(f) # Skip header line
        for line in f:
            data = line.split(fileDelimiter);
            data = [v.strip() for v in data];
            list.append(int(data[location]));
        f.close()
    return list;

def dictListGet(filePath: str, keyLocation: int, valuesLocation: int, fileDelimiter: str = ',', header: bool = True):
    dictionary = defaultdict(list);
    with open(filePath, 'r') as f:
        if header:
            next(f) # Skip header line
            for line in f:
                data = line.split(fileDelimiter);
                data = [v.strip() for v in data];
                dictionary[int(data[keyLocation])].append(int(data[valuesLocation]));
        f.close()
    return dictionary;

lineNum = 0;

goldMedals = np.empty((234, 48, 69, 2, 32), dtype=int);
silverMedals = np.empty((234, 48, 69, 2, 32), dtype=int);
bronzeMedals = np.empty((234, 48, 69, 2, 32), dtype=int);
goldMedals[:] = 0;
silverMedals[:] = 0;
bronzeMedals[:] = 0;

athletesBase = np.empty((234, 32), dtype=int);
athletesCode = np.empty((234, 32, 69), dtype=int);
athletesSex = np.empty((234, 32, 2), dtype=int);
athletesBoth = np.empty((234, 32, 69, 2), dtype=int);
athletesBase[:] = 0;
athletesCode[:] = 0;
athletesSex[:] = 0;
athletesBoth[:] = 0;

countryCodes = dictGet("countryCode.csv");
years = dictGet("yearsChanger.csv");

countryCodesList = listGet("countryCode.csv", 0);
sportsList = listGet("2028 Sports and Countries2.csv", 1)
sportCodesList = dictListGet("2028 Sports and Countries2.csv", 1, 3)

sport = 0;
sportCode = 0;
sex = 0;
lineNum = 0;
lines = [];
checkIter = 0;
with open('2025_Problem_C_Data\\summerOly_athletes.csv', 'r') as f:
    next(f); # Skip header line
    print("File loaded");
    for line in f:
        data = line.split(',');
        data = [v.strip() for v in data];
        year = int(years[data[4]]);
        country = int(countryCodes[data[3]]);
        if "Women" in data[7]:
            sex = 1;
        else:
            sex = 0;
        with open("sportCode2.csv", "r") as g:
            for sportLine in g:
                sportData = [v.strip() for v in sportLine.split(',')]
                sportFound = False;
                if sportData[5] != "":
                    if (sportData[4] in data[6]) and (sportData[5] in data[7]):
                        sport = int(sportData[0]);
                        sportcode = int(sportData[2]);
                        sportFound = True;
                elif sportData[6] != "":
                    if (sportData[4] in data[6]) and (sportData[6] not in data[6]) and (sportData[6] not in data[7]):
                        sport = int(sportData[0]);
                        sportCode = int(sportData[2]);
                        sportFound = True;
                else:
                    if (sportData[4] in data[6]):
                        sport = int(sportData[0]);
                        sportCode = int(sportData[2]);
                        sportFound = True;
                if sportFound:
                    sportFound = False;
                    break;
        if "Gold" in data[8]:
            for i in range(year, 32):
                goldMedals[country, sport, sportCode, sex, i] += 1;
        if "Silver" in data[8]:
            for i in range(year, 32):
                silverMedals[country, sport, sportCode, sex, i] += 1;
        if "Bronze" in data[8]:
            for i in range(year, 32):
                bronzeMedals[country, sport, sportCode, sex, i] += 1;
        
        athletesBase[country, year] += 1;
        athletesCode[country, year, sportCode] += 1;
        athletesSex[country, year, sex] += 1;
        athletesBoth[country, year, sportCode, sex] += 1;

        checkIter += 1;
        if checkIter % 100 == 0:
            print(f"Processed {checkIter} lines");

    # End file header:
    # country code, year, sex, sport, sport code, gold in sport, silver in sport, bronze in sport, gold in sport + sport code, silver in sport + sport code, bronze in sport + sport code, gold in sport + code + sex, silver in sport + code + sex, bronze in sport + code + sex, athletes this year, athletes in code this year, athletes in sex this year, athletes in code + sex this year, athletes last year, athletes in code last year, athletes in sex last year, athletes in code + sex last year,
    with open('2028FullData.csv', 'w') as f:
        f.write("lineNum,countryCode,year,sex,sport,sportcode,goldInSport,silverInSport,bronzeInSport,goldInSportCode,silverInSportCode,bronzeInSportCode,goldInSportCodeSex,silverInSportCodeSex,bronzeInSportCodeSex,athletesBaseThisYear,athletesCodeThisYear,athletesSexThisYear,athletesBothThisYear,athletesLastYear,athletesCodeLastYear,athletesSexLastYear,athletesBothLastYear\n");
        for country in range(0, len(countryCodesList)):
                with open(f"2028 Sports and Countries2.csv", "r") as g:
                    next(g);
                    for line in g:
                        print(line);
                        sportData = line.split(',');
                        print(sportData);
                        sportData = [v.strip() for v in sportData];
                        print(sportData);
                        if int(sportData[4]) == 1:
                            for sex in range(0, 2):
                                goldMedalsPrior = 0;
                                silverMedalsPrior = 0;
                                bronzeMedalsPrior = 0;
                                goldMedalsCodePrior = 0;
                                silverMedalsCodePrior = 0;
                                bronzeMedalsCodePrior = 0;
                                goldMedalsCodeSexPrior = 0;
                                silverMedalsCodeSexPrior = 0;
                                bronzeInCodeSexPrior = 0;
                                for codeIter in sportCodesList[int(sportData[1])]:
                                    for sexIter in range(0, 2):
                                        goldMedalsPrior += goldMedals[country, int(sportData[1]), codeIter, sex, 31];
                                        silverMedalsPrior += silverMedals[country, int(sportData[1]), codeIter, sex, 31];
                                        bronzeMedalsPrior += bronzeMedals[country, int(sportData[1]), codeIter, sex, 31];
                                for sexIter in range(0, 2):
                                    goldMedalsCodePrior += goldMedals[country, int(sportData[1]), int(sportData[3]), sexIter, 31];
                                    silverMedalsCodePrior += silverMedals[country, int(sportData[1]), int(sportData[3]), sexIter, 31];
                                    bronzeMedalsCodePrior += bronzeMedals[country, int(sportData[1]), int(sportData[3]), sexIter, 31];
                                goldMedalsCodeSexPrior += goldMedals[country, int(sportData[1]), int(sportData[3]), sex, 31];
                                silverMedalsCodeSexPrior += silverMedals[country, int(sportData[1]), int(sportData[3]), sex, 31];
                                bronzeInCodeSexPrior += bronzeMedals[country, int(sportData[1]), int(sportData[3]), sex, 31];
                        else:
                            sex = 0;
                            goldMedalsPrior = 0;
                            silverMedalsPrior = 0
                            bronzeMedalsPrior = 0;
                            goldMedalsCodePrior = 0;
                            silverMedalsCodePrior = 0;
                            bronzeMedalsCodePrior = 0;
                            for codeIter in sportCodesList[int(int(sportData[1]))]:
                                goldMedalsPrior += goldMedals[country, int(sportData[1]), codeIter, 0, 31];
                                silverMedalsPrior += silverMedals[country, int(sportData[1]), codeIter, 0, 31];
                                bronzeMedalsPrior += bronzeMedals[country, int(sportData[1]), codeIter, 0, 31];
                            goldMedalsCodePrior += goldMedals[country, int(sportData[1]), int(sportData[3]), 0, 31];
                            silverMedalsCodePrior += silverMedals[country, int(sportData[1]), int(sportData[3]), 0, 31];
                            bronzeMedalsCodePrior += bronzeMedals[country, int(sportData[1]), int(sportData[3]), 0, 31];
                            goldMedalsCodeSexPrior = goldMedalsCodePrior;
                            silverMedalsCodeSexPrior = silverMedalsCodePrior;
                            bronzeMedalsCodePrior = bronzeMedalsCodePrior;
                        print(f"{lineNum},{countryCodesList[country]},31,{sex},{int(sportData[1])},{int(sportData[3])},{goldMedalsPrior},{silverMedalsPrior},{bronzeMedalsPrior},{goldMedalsCodePrior},{silverMedalsCodePrior},{bronzeMedalsCodePrior},{goldMedalsCodeSexPrior},{silverMedalsCodeSexPrior},{bronzeMedalsCodePrior},{athletesBase[country, 31]},{athletesCode[country, 31, int(sportData[3])]},{athletesSex[country, 31, sex]},{athletesBoth[country, 31, int(sportData[3]), sex]},{athletesBase[country, 30]},{athletesCode[country, 30, int(sportData[3])]},{athletesSex[country, 30, sex]},{athletesBoth[country, 30, int(sportData[3]), sex]}", file=f);
                        lineNum += 1;