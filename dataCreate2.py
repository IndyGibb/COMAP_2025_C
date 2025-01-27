import numpy as np
from dataCreate import dictGet


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

with open('2025_Problem_C_Data\\summerOly_athletes.csv', 'r') as f:
    next(f); # Skip header line
    for line in f:
        data = [v.strip() for v in line.split(',')]
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

    # End file header:
    # country code, year, sex, sport, sport code, gold in sport, silver in sport, bronze in sport, gold in sport + sport code, silver in sport + sport code, bronze in sport + sport code, gold in sport + code + sex, silver in sport + code + sex, bronze in sport + code + sex, athletes this year, athletes in code this year, athletes in sex this year, athletes in code + sex this year, athletes last year, athletes in code last year, athletes in sex last year, athletes in code + sex last year, gold this year, silver this year, bronze this year
        newLine = str(country) + "," + str(year) + "," + str(sex) + "," + str(sport) + "," + str(sportCode) + ",";
        goldInSport = 0;
        for codeIter in range(0, 69):
            for sexIter in range(0, 2):
                goldInSport += goldMedals[country, sport, codeIter, sexIter, year];
        goldInSportCode = 0;
        for sexIter in range(0, 2):
            goldInSportCode += goldMedals[country, sport, sportCode, sexIter, year];
        goldInSportCodeSex = 0;
        goldInSportCodeSex += goldMedals[country, sport, sportCode, sex, year];
        silverInSport = 0;
        for codeIter in range(0, 69):
            for sexIter in range(0, 2):
                silverInSport += silverMedals[country, sport, codeIter, sexIter, year];
        silverInSportCode = 0;
        for sexIter in range(0, 2):
            silverInSportCode += silverMedals[country, sport, sportCode, sexIter, year];
        silverInSportCodeSex = 0;
        silverInSportCodeSex += silverMedals[country, sport, sportCode, sex, year];
        bronzeInSport = 0;
        for codeIter in range(0, 69):
            for sexIter in range(0, 2):
                bronzeInSport += bronzeMedals[country, sport, codeIter, sexIter, year];
        bronzeInSportCode = 0;
        for sexIter in range(0, 2):
            bronzeInSportCode += bronzeMedals[country, sport, sportCode, sexIter, year];
        bronzeInSportCodeSex = 0;
        bronzeInSportCodeSex += bronzeMedals[country, sport, sportCode, sex, year];
        athletesBaseThisYear = athletesBase[country, year];
        athletesCodeThisYear = athletesCode[country, year, sportCode];
        athletesSexThisYear = athletesSex[country, year, sex];
        athletesBothThisYear = athletesBoth[country, year, sportCode, sex];

        if year > 0:
            athletesLastYear = athletesBase[country, year - 1];
            athletesCodeLastYear = athletesCode[country, year - 1, sportCode];
            athletesSexLastYear = athletesSex[country, year - 1, sex];
            athletesBothLastYear = athletesBoth[country, year - 1, sportCode, sex];
            goldThisYear = goldMedals[country, sport, sportCode, sex, year] - goldMedals[country, sport, sportCode, sex, year - 1];
            silverThisYear = silverMedals[country, sport, sportCode, sex, year] - silverMedals[country, sport, sportCode, sex, year - 1];
            bronzeThisYear = bronzeMedals[country, sport, sportCode, sex, year] - bronzeMedals[country, sport, sportCode, sex, year - 1];   
        else:
            athletesLastYear = 0;
            athletesCodeLastYear = 0;
            athletesSexLastYear = 0;
            athletesBothLastYear = 0;
            goldThisYear = goldMedals[country, sport, sportCode, sex, 0];
            silverThisYear = silverMedals[country, sport, sportCode, sex, 0];
            bronzeThisYear = bronzeMedals[country, sport, sportCode, sex, 0];

        newLine += str(goldInSport) + "," + str(silverInSport) + "," + str(bronzeInSport) + "," + str(goldInSportCode) + "," + str(silverInSportCode) + "," + str(bronzeInSportCode) + "," + str(goldInSportCodeSex) + "," + str(silverInSportCodeSex) + "," + str(bronzeInSportCodeSex) + "," + str(athletesBaseThisYear) + "," + str(athletesCodeThisYear) + "," + str(athletesSexThisYear) + "," + str(athletesBothThisYear) + "," + str(athletesLastYear) + "," + str(athletesCodeLastYear) + "," + str(athletesSexLastYear) + "," + str(athletesBothLastYear) + "," + str(goldThisYear) + "," + str(silverThisYear) + "," + str(bronzeThisYear);
        lines.append(str(lineNum) + "," + newLine);
        lineNum += 1;

        if (lineNum % 100 == 0):
            print(f"Processed {lineNum} lines");
    
    with open("dataFile.csv", "w") as f:
        print("lineNum,countryCode,year,sex,sport,sportcode,goldInSport,silverInSport,bronzeInSport,goldInSportCode,silverInSportCode,bronzeInSportCode,goldInSportCodeSex,silverInSportCodeSex,bronzeInSportCodeSex,athletesBaseThisYear,athletesCodeThisYear,athletesSexThisYear,athletesBothThisYear,athletesLastYear,athletesCodeLastYear,athletesSexLastYear,athletesBothLastYear,goldThisYear,silverThisYear,bronzeThisYear", file=f);
        for line in lines:
            print(line, file=f);
            print(line);