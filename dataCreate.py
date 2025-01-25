from collections import defaultdict

def dictGet(filePath: str, keyLocation: int = 1, valueLocation: int = 0, fileDelim: str = ','):
    dictionary = {};
    with open(filePath, 'r') as f:
        for line in f:
            data = line.strip().split(fileDelim);
            dictionary[data[keyLocation]] = data[valueLocation];
        f.close();
    return dictionary;

def sportsGet(filePath: str, keyLocation: int = 1, fileDelim: str = ','):
    sports = {};
    with open(filePath, 'r') as f:
        for line in f:
            data = line.strip().split(fileDelim);
            sports[data[keyLocation]] = data;
        f.close();
    return sports;


# End file header:
# country code, year, sex, sport, sport code, gold in sport, silver in sport, bronze in sport, gold in sport + sport code, silver in sport + sport code, bronze in sport + sport code, gold in sport + code + sex, silver in sport + code + sex, bronze in sport + code + sex, athletes this year, athletes in code this year, athletes in sex this year, athletes in code + sex this year, athletes last year, athletes in code last year, athletes in sex last year, athletes in code + sex last year, gold this year, silver this year, bronze this year

if __name__ == "__main__":
    goldMedals = {}; # multi-level dictionary with first key being country, second being sport, third being sport code, fourth being sex, fifth being year, value being an integer representing the number of medals in the previous years
    silverMedals = {}; # same but for silver
    bronzeMedals = {}; # same but for bronze
    athletesBase = {}; # multi-level dictionary with first key being country, second being year, value being the number of athletes from that country that year
    athletesCode = {}; # multi-level dictionary for number of athletes with first key being country, second being year, third being sport code, value being the number of athletes
    athletesSex = {}; # multi-level dictionary for number of athletes with first key being country, second being year, third being sex, value being the number of athletes
    athletesBoth = {}; #multi-level dictionary for number of athletes with first key being country, second being year, third being sport code, fourth being sex, value being the number of athletes
    sport = "";
    sportCode = "";
    sex = 0;
    lineNum = 0;
    lines = {};
    countryCodes = dictGet('countryCode.csv');
    years = dictGet('yearsChanger.csv');
    sportCodes = sportsGet('sportCode2.csv');
    with open('2025_Problem_C_Data\summerOly_athletes.csv', 'r') as f:
        next(f);  # Skip header line
        for line in f:
            data = line.strip().split(',');
            year = years[data[4]];
            country = countryCodes[data[3]];
            if "Women" in data[7]:
                sex = 1;
            else:
                sex = 0;
            if not goldMedals.get(country):
                goldMedals[country] = {};
            with open("sportCode2.csv", "r") as g:
                sport = "";
                for sportLine in g:
                    sportData = sportLine.strip().split(',');
                    if sportData[5] != "":
                        if (sportData[4] in data[6]) and (sportData[5] in data[7]):
                            sport = sportData[1];
                            sportCode = sportData[0];
                    elif sportData[6] != "":
                        if (sportData[4] in data[6]) and (sportData[6] not in data[6]) and (sportData[6] not in data[7]):
                            sport = sportData[1];
                            sportCode = sportData[0];
                    else:
                        if (sportData[4] in data[6]):
                            sport = sportData[1];
                            sportCode = sportData[0];
                    if sport != "":
                        break;
            sport = sportCodes[sport];
            if not goldMedals[country].get(sport):
                goldMedals[country][sport] = {};
            if not goldMedals[country][sport].get(sportCode):
                goldMedals[country][sport][sportCode] = {};
            if not goldMedals[country][sport][sportCode].get(sex):
                goldMedals[country][sport][sportCode][sex] = {};
            if not goldMedals[country][sport][sportCode][sex].get(year):
                goldMedals[country][sport][sportCode][sex][year] = defaultdict(int);
            
            if not silverMedals.get(country):
                silverMedals[country] = {};
            with open("sportCode2.csv", "r") as g:
                sport = "";
                for sportLine in g:
                    sportData = sportLine.strip().split(',');
                    if sportData[5] != "":
                        if (sportData[4] in data[6]) and (sportData[5] in data[7]):
                            sport = sportData[1];
                            sportCode = sportData[0];
                    elif sportData[6] != "":
                        if (sportData[4] in data[6]) and (sportData[6] not in data[6]) and (sportData[6] not in data[7]):
                            sport = sportData[1];
                            sportCode = sportData[0];
                    else:
                        if (sportData[4] in data[6]):
                            sport = sportData[1];
                            sportCode = sportData[0];
                    if sport != "":
                        break;
            sport = sportCodes[sport];
            if not silverMedals[country].get(sport):
                silverMedals[country][sport] = {};
            if not silverMedals[country][sport].get(sportCode):
                silverMedals[country][sport][sportCode] = {};
            if not silverMedals[country][sport][sportCode].get(sex):
                silverMedals[country][sport][sportCode][sex] = {};
            if not silverMedals[country][sport][sportCode][sex].get(year):
                silverMedals[country][sport][sportCode][sex][year] = defaultdict(int);
            
            if not bronzeMedals.get(country):
                bronzeMedals[country] = {};
            with open("sportCode2.csv", "r") as g:
                sport = "";
                for sportLine in g:
                    sportData = sportLine.strip().split(',');
                    if sportData[5] != "":
                        if (sportData[4] in data[6]) and (sportData[5] in data[7]):
                            sport = sportData[1];
                            sportCode = sportData[0];
                    elif sportData[6] != "":
                        if (sportData[4] in data[6]) and (sportData[6] not in data[6]) and (sportData[6] not in data[7]):
                            sport = sportData[1];
                            sportCode = sportData[0];
                    else:
                        if (sportData[4] in data[6]):
                            sport = sportData[1];
                            sportCode = sportData[0];
                    if sport != "":
                        break;
            sport = sportCodes[sport];
            if not bronzeMedals[country].get(sport):
                bronzeMedals[country][sport] = {};
            if not bronzeMedals[country][sport].get(sportCode):
                bronzeMedals[country][sport][sportCode] = {};
            if not bronzeMedals[country][sport][sportCode].get(sex):
                bronzeMedals[country][sport][sportCode][sex] = {};
            if not bronzeMedals[country][sport][sportCode][sex].get(year):
                bronzeMedals[country][sport][sportCode][sex][year] = defaultdict(int);
            
            if "Gold" in data[8]:
                for i in range(year, 32):
                    if not goldMedals.get(country):
                        goldMedals[country] = {};
                    if not goldMedals[country].get(sport):
                        goldMedals[country][sport] = {};
                    if not goldMedals[country][sport].get(sportCode):
                        goldMedals[country][sport][sportCode] = {};
                    if not goldMedals[country][sport][sportCode].get(sex):
                        goldMedals[country][sport][sportCode][sex] = {};
                    if not goldMedals[country][sport][sportCode][sex].get(i):
                        goldMedals[country][sport][sportCode][sex][i] = defaultdict(int);
                    
                    goldMedals[country][sport][sportCode][sex][i] += 1;

            if "Silver" in data[8]:
                for i in range(year, 32):
                    if not silverMedals.get(country):
                        silverMedals[country] = {};
                    if not silverMedals[country].get(sport):
                        silverMedals[country][sport] = {};
                    if not silverMedals[country][sport].get(sportCode):
                        silverMedals[country][sport][sportCode] = {};
                    if not silverMedals[country][sport][sportCode].get(sex):
                        silverMedals[country][sport][sportCode][sex] = {};
                    if not silverMedals[country][sport][sportCode][sex].get(i):
                        silverMedals[country][sport][sportCode][sex][i] = defaultdict(int);
                    
                    silverMedals[country][sport][sportCode][sex][i] += 1;
                
            if "Bronze" in data[8]:
                for i in range(year, 32):
                    if not bronzeMedals.get(country):
                        bronzeMedals[country] = {};
                    if not bronzeMedals[country].get(sport):
                        bronzeMedals[country][sport] = {};
                    if not bronzeMedals[country][sport].get(sportCode):
                        bronzeMedals[country][sport][sportCode] = {};
                    if not bronzeMedals[country][sport][sportCode].get(sex):
                        bronzeMedals[country][sport][sportCode][sex] = {};
                    if not bronzeMedals[country][sport][sportCode][sex].get(i):
                        bronzeMedals[country][sport][sportCode][sex][i] = defaultdict(int);
                    
                    bronzeMedals[country][sport][sportCode][sex][i] += 1;


            if not athletesBase[country].get(year):
                athletesBase[country][year] = defaultdict(int);
            athletesBase[country][year] += 1;
            if not athletesCode[country].get(year):
                athletesCode[country][year] = {};
            if not athletesCode[country][year].get(sportCode):
                athletesCode[country][year][sportCode] = defaultdict(int);
            athletesCode[country][year][sportCode] += 1;
            if not athletesSex[country].get(year):
                athletesSex[country][year] = {};
            if not athletesSex[country][year].get(sex):
                athletesSex[country][year][sex] = defaultdict(int);
            athletesSex[country][year][sex] += 1;
            if not athletesBoth[country].get(year):
                athletesBoth[country][year] = {};
            if not athletesBoth[country][year].get(sportCode):
                athletesBoth[country][year][sportCode] = {};
            if not athletesBoth[country][year][sportCode].get(sex):
                athletesBoth[country][year][sportCode][sex] = defaultdict(int);
            athletesBoth[country][year][sportCode][sex] += 1;


    with open('2025_Problem_C_Data\summerOly_athletes.csv', 'r') as f:
        for line in f:
            data = line.strip().split(',');
            year = years[data[4]];
            country = countryCodes[data[3]];
            if "Women" in data[7]:
                sex = 1;
            else:
                sex = 0;
            with open("sportCode2.csv", "r") as g:
                sport = "";
                for sportLine in g:
                    sportData = sportLine.strip().split(',');
                    if sportData[5] != "":
                        if (sportData[4] in data[6]) and (sportData[5] in data[7]):
                            sport = sportData[1];
                            sportCode = sportData[0];
                    elif sportData[6] != "":
                        if (sportData[4] in data[6]) and (sportData[6] not in data[6]) and (sportData[6] not in data[7]):
                            sport = sportData[1];
                            sportCode = sportData[0];
                    else:
                        if (sportData[4] in data[6]):
                            sport = sportData[1];
                            sportCode = sportData[0];
                    if sport != "":
                        break;
            sport = sportCodes[sport];


    # End file header:
    # country code, year, sex, sport, sport code, gold in sport, silver in sport, bronze in sport, gold in sport + sport code, silver in sport + sport code, bronze in sport + sport code, gold in sport + code + sex, silver in sport + code + sex, bronze in sport + code + sex, athletes this year, athletes in code this year, athletes in sex this year, athletes in code + sex this year, athletes last year, athletes in code last year, athletes in sex last year, athletes in code + sex last year, gold this year, silver this year, bronze this year
            newLine = country + "," + year + "," + sex + "," + sport + "," + sportCode + ",";
            goldInSport = 0;
            for key in goldMedals[country][sport]:
                for keyb in goldMedals[country][sport][key]:
                    for i in range(year, 32):
                        goldInSport += goldMedals[country][sport][key][keyb][i];
            goldInSportCode = 0;
            for key in goldMedals[country][sport][sportCode]:
                for i in range(year, 32):
                    goldInSportCode += goldMedals[country][sport][sportCode][key][year];
            for i in range(year, 32):
                goldInSportCodeSex = goldMedals[country][sport][sportCode][sex][year];
            
            silverInSport = 0;
            for key in silverMedals[country][sport]:
                for keyb in silverMedals[country][sport][key]:
                    for i in range(year, 32):
                        silverInSport += silverMedals[country][sport][key][keyb][i];
            silverInSportCode = 0;
            for key in silverMedals[country][sport][sportCode]:
                for i in range(year, 32):
                    silverInSportCode += silverMedals[country][sport][sportCode][key][year];
            for i in range(year, 32):
                silverInSportCodeSex = silverMedals[country][sport][sportCode][sex][year];

            bronzeInSport = 0;
            for key in bronzeMedals[country][sport]:
                for keyb in bronzeMedals[country][sport][key]:
                    for i in range(year, 32):
                        bronzeInSport += bronzeMedals[country][sport][key][keyb][i];
            bronzeInSportCode = 0;
            for key in bronzeMedals[country][sport][sportCode]:
                for i in range(year, 32):
                    bronzeInSportCode += bronzeMedals[country][sport][sportCode][key][year];
            for i in range(year, 32):
                bronzeInSportCodeSex = bronzeMedals[country][sport][sportCode][sex][year];

            athletesBaseThisYear = athletesBase[country][year];
            athletesCodeThisYear = athletesCode[country][year][sportCode];
            athletesSexThisYear = athletesSex[country][year][sex];
            athletesBothThisYear = athletesBoth[country][year][sportCode][sex];

            athletesBaseLastYear = athletesBase[country][year-1] if (year-1) in athletesBase[country] else 0;
            athletesCodeLastYear = athletesCode[country][year-1][sportCode] if (year-1) in athletesCode[country] and sportCode in athletesCode[country][year-1] else 0;
            athletesSexLastYear = athletesSex[country][year-1][sex] if (year-1) in athletesSex[country] and sex in athletesSex[country][year-1] else 0;
            athletesBothLastYear = athletesBoth[country][year-1][sportCode][sex] if (year-1) in athletesBoth[country] and sportCode in athletesBoth[country][year-1] and sex in athletesBoth[country][year-1][sportCode] else 0;

            goldThisYear = goldMedals[country][sport][sportCode][sex][year];
            silverThisYear = silverMedals[country][sport][sportCode][sex][year];
            bronzeThisYear = bronzeMedals[country][sport][sportCode][sex][year];
            
            newLine.append(str(goldInSport) + "," + str(silverInSport) + "," + str(bronzeInSport) + str(goldInSportCode) + "," + str(silverInSportCode) + "," + str(bronzeInSportCodeSex) + "," + str(goldInSportCodeSex) + "," + str(silverInSportCodeSex) + "," + str(bronzeInSportCodeSex) + "," + str(athletesBaseThisYear) + "," + str(athletesCodeThisYear) + "," + str(athletesSexThisYear) + "," + str(athletesBothThisYear) + "," + str(athletesBaseLastYear) + "," + str(athletesCodeLastYear) + "," + str(athletesSexLastYear) + "," + str(athletesBothLastYear) + "," + str(goldThisYear) + "," + str(silverThisYear) + "," + str(bronzeThisYear) + "\n");
            lines[lineNum] = newLine;
            lineNum += 1;

            if (lineNum % 100 == 0):
                print(f"Processed {lineNum} lines");
            

        
        with open("dataFile.csv", 'w') as f:
            for line in lines:
                print(line, file=f);
                print(line);