from collections import defaultdict
import string

def dictGet(filePath: string, keyLocation: int = 1, valueLocation: int = 0, fileDelim: string = ','):
    dictionary = defaultdict(int);
    with open(filePath, 'r') as f:
        for line in f:
            data = line.split(fileDelim);
            data = [v.strip() for v in data];
            dictionary[data[keyLocation]] = int(data[valueLocation]);
        f.close();
    return dictionary;

def sportsGet(filePath: string, keyLocation: int = 4, fileDelim: string = ','):
    sports = defaultdict(int);
    with open(filePath, 'r') as f:
        for line in f:
            data = line.split(fileDelim);
            data = [v.strip() for v in data];
            sports[data[keyLocation]] = data;
        f.close();
    return sports;

def ensure_dict_structure(medals_dict, country, sport, sportCode, sex, year):
    if country not in medals_dict:
        medals_dict[country] = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int)))))
    if sport not in medals_dict[country]:
        medals_dict[country][sport] = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int))))
    if sportCode not in medals_dict[country][sport]:
        medals_dict[country][sport][sportCode] = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    if sex not in medals_dict[country][sport][sportCode]:
        medals_dict[country][sport][sportCode][sex] = defaultdict(lambda: defaultdict(int))
    if year not in medals_dict[country][sport][sportCode][sex]:
        medals_dict[country][sport][sportCode][sex][year] = defaultdict(int)



# End file header:
# country code, year, sex, sport, sport code, gold in sport, silver in sport, bronze in sport, gold in sport + sport code, silver in sport + sport code, bronze in sport + sport code, gold in sport + code + sex, silver in sport + code + sex, bronze in sport + code + sex, athletes this year, athletes in code this year, athletes in sex this year, athletes in code + sex this year, athletes last year, athletes in code last year, athletes in sex last year, athletes in code + sex last year, gold this year, silver this year, bronze this year

if __name__ == "__main__":
    goldMedals = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int)))))# multi-level dictionary with first key being country, second being sport, third being sport code, fourth being sex, fifth being year, value being an integer representing the number of medals in the previous years
    silverMedals = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int))))) # same but for silver
    bronzeMedals = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int))))) 
    athletesBase = defaultdict(lambda: defaultdict(int)) # silverMedals{country : {sport : {sportCode : {sex: {year: 0}}}}}
    athletesCode = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    athletesSex = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    athletesBoth = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int))))

    sport = "";
    sportCode = "";
    sex = 0;
    lineNum = 0;
    lines = defaultdict(int);
    countryCodes = dictGet('countryCode.csv');
    years = dictGet('yearsChanger.csv');
    sportCodes = sportsGet('sportCode2.csv');
    checkIter = 0
    with open('2025_Problem_C_Data\summerOly_athletes.csv', 'r') as f:
        next(f);  # Skip header line
        print("File loaded");
        for line in f:
            data = line.split(',');
            data = [v.strip() for v in data];
            year = years[data[4]];
            country = countryCodes[data[3]];
            if "Women" in data[7]:
                sex = 1;
            else:
                sex = 0;
            if not goldMedals.get(country):
                goldMedals[country] = defaultdict(int);
            with open("sportCode2.csv", "r") as g:
                sport = "";
                for sportLine in g:
                    sportData = sportLine.split(',');
                    sportData = [v.strip() for v in sportData];
                    if sportData[5] != "":
                        if (sportData[4] in data[6]) and (sportData[5] in data[7]):
                            sport = sportData[0];
                            sportCode = sportData[2];
                    elif sportData[6] != "":
                        if (sportData[4] in data[6]) and (sportData[6] not in data[6]) and (sportData[6] not in data[7]):
                            sport = sportData[0];
                            sportCode = sportData[2];
                    else:
                        if (sportData[4] in data[6]):
                            sport = sportData[0];
                            sportCode = sportData[2];
                    if sport != "":
                        break;
            '''if not goldMedals[country].get(sport):
                goldMedals[country][sport] = defaultdict(int);
            if not goldMedals[country][sport].get(sportCode):
                goldMedals[country][sport][sportCode] = defaultdict(int);
            if not goldMedals[country][sport][sportCode].get(sex):
                goldMedals[country][sport][sportCode][sex] = defaultdict(int);
            if not goldMedals[country][sport][sportCode][sex].get(year):
                goldMedals[country][sport][sportCode][sex][year] = defaultdict(int);'''
            
            if not silverMedals.get(country):
                silverMedals[country] = defaultdict(int);
            with open("sportCode2.csv", "r") as g:
                sport = "";
                for sportLine in g:
                    sportData = sportLine.split(',');
                    sportData = [v.strip() for v in sportData];
                    if sportData[5] != "":
                        if (sportData[4] in data[6]) and (sportData[5] in data[7]):
                            sport = sportData[0];
                            sportCode = sportData[2];
                    elif sportData[6] != "":
                        if (sportData[4] in data[6]) and (sportData[6] not in data[6]) and (sportData[6] not in data[7]):
                            sport = sportData[0];
                            sportCode = sportData[2];
                    else:
                        if (sportData[4] in data[6]):
                            sport = sportData[0];
                            sportCode = sportData[2];
                    if sport != "":
                        break;
            '''if not silverMedals[country].get(sport):
                silverMedals[country][sport] = defaultdict(int);
            if not silverMedals[country][sport].get(sportCode):
                silverMedals[country][sport][sportCode] = defaultdict(int);
            if not silverMedals[country][sport][sportCode].get(sex):
                silverMedals[country][sport][sportCode][sex] = defaultdict(int);
            if not silverMedals[country][sport][sportCode][sex].get(year):
                silverMedals[country][sport][sportCode][sex][year] = defaultdict(int);'''
            
            if not bronzeMedals.get(country):
                bronzeMedals[country] = defaultdict(int);
            with open("sportCode2.csv", "r") as g:
                sport = "";
                for sportLine in g:
                    sportData = sportLine.split(',');
                    sportData = [v.strip() for v in sportData];
                    if sportData[5] != "":
                        if (sportData[4] in data[6]) and (sportData[5] in data[7]):
                            sport = sportData[0];
                            sportCode = sportData[2];
                    elif sportData[6] != "":
                        if (sportData[4] in data[6]) and (sportData[6] not in data[6]) and (sportData[6] not in data[7]):
                            sport = sportData[0];
                            sportCode = sportData[2];
                    else:
                        if (sportData[4] in data[6]):
                            sport = sportData[0];
                            sportCode = sportData[2];
                    if sport != "":
                        break;
            '''if not bronzeMedals[country].get(sport):
                bronzeMedals[country][sport] = defaultdict(int);
            if not bronzeMedals[country][sport].get(sportCode):
                bronzeMedals[country][sport][sportCode] = defaultdict(int);
            if not bronzeMedals[country][sport][sportCode].get(sex):
                bronzeMedals[country][sport][sportCode][sex] = defaultdict(int);
            if not bronzeMedals[country][sport][sportCode][sex].get(year):
                bronzeMedals[country][sport][sportCode][sex][year] = defaultdict(int);'''
            
            if "Gold" in data[8]:
                ensure_dict_structure(goldMedals, country, sport, sportCode, sex, year);
                for i in range(int(year), 32):
                    '''if not goldMedals.get(country):
                        goldMedals[country] = defaultdict(int);
                    if not goldMedals[country].get(sport):
                        goldMedals[country][sport] = defaultdict(int);
                    if not goldMedals[country][sport].get(sportCode):
                        goldMedals[country][sport][sportCode] = defaultdict(int);
                    if not goldMedals[country][sport][sportCode].get(sex):
                        goldMedals[country][sport][sportCode][sex] = defaultdict(int);'''
                    gold = goldMedals[country][sport][sportCode][sex].get(i, 0);
                    goldMedals[country][sport][sportCode][sex][i] = gold + 1;

            if "Silver" in data[8]:
                ensure_dict_structure(silverMedals, country, sport, sportCode, sex, year);
                for i in range(int(year), 32):
                    '''if not silverMedals.get(country):
                        silverMedals[country] = defaultdict(int);
                    if not silverMedals[country].get(sport):
                        silverMedals[country][sport] = defaultdict(int);
                    if not silverMedals[country][sport].get(sportCode):
                        silverMedals[country][sport][sportCode] = defaultdict(int);
                    if not silverMedals[country][sport][sportCode].get(sex):
                        silverMedals[country][sport][sportCode][sex] = defaultdict(int);'''
                    silver = silverMedals[country][sport][sportCode][sex].get(i, 0);
                    silverMedals[country][sport][sportCode][sex][i] = silver + 1; # silverMedals{country : {sport : {sportCode : {sex: {year: 0}}}}}
                
            if "Bronze" in data[8]:
                ensure_dict_structure(bronzeMedals, country, sport, sportCode, sex, year);
                for i in range(int(year), 32):
                    '''if not bronzeMedals.get(country):
                        bronzeMedals[country] = defaultdict(int);
                    if not bronzeMedals[country].get(sport):
                        bronzeMedals[country][sport] = defaultdict(int);
                    if not bronzeMedals[country][sport].get(sportCode):
                        bronzeMedals[country][sport][sportCode] = defaultdict(int);
                    if not bronzeMedals[country][sport][sportCode].get(sex):
                        bronzeMedals[country][sport][sportCode][sex] = defaultdict(int);'''
                    bronze = bronzeMedals[country][sport][sportCode][sex].get(i, 0);
                    bronzeMedals[country][sport][sportCode][sex][i] = bronze + 1;

            '''if not athletesBase.get(country):
                athletesBase[country] = defaultdict(int);'''
            athletesBase[country][year] += 1;
            '''if not athletesCode.get(country):
                athletesCode[country] = defaultdict(int);
            if not athletesCode[country].get(year):
                athletesCode[country][year] = defaultdict(int);'''
            athletesCode[country][year][sportCode] += 1;
            '''if not athletesSex.get(country):
                athletesSex[country] = defaultdict(int);
            if not athletesSex[country].get(year):
                athletesSex[country][year] = defaultdict(int);'''
            athletesSex[country][year][sex] += 1;
            '''if not athletesBoth.get(country):
                athletesBoth[country] = defaultdict(int);
            if not athletesBoth[country].get(year):
                athletesBoth[country][year] = defaultdict(int);
            if not athletesBoth[country][year].get(sportCode):
                athletesBoth[country][year][sportCode] = defaultdict(int);'''
            athletesBoth[country][year][sportCode][sex] += 1;
            checkIter += 1;
            if checkIter % 100 == 0:
                print(f"Processed {checkIter} athletes.");


    with open('2025_Problem_C_Data\summerOly_athletes.csv', 'r') as f:
        for line in f:
            data = line.split(',');
            data = [v.strip() for v in data];
            year = int(years[data[4]]);
            country = countryCodes[data[3]];
            if "Women" in data[7]:
                sex = 1;
            else:
                sex = 0;
            with open("sportCode2.csv", "r") as g:
                sport = "";
                for sportLine in g:
                    sportData = sportLine.split(',');
                    data = [v.strip() for v in data];
                    if sportData[5] != "":
                        if (sportData[4] in data[6]) and (sportData[5] in data[7]):
                            sport = sportData[0];
                            sportCode = sportData[2];
                    elif sportData[6] != "":
                        if (sportData[4] in data[6]) and (sportData[6] not in data[6]) and (sportData[6] not in data[7]):
                            sport = sportData[0];
                            sportCode = sportData[2];
                    else:
                        if (sportData[4] in data[6]):
                            sport = sportData[0];
                            sportCode = sportData[2];
                    if sport != "":
                        break;


    # End file header:
    # country code, year, sex, sport, sport code, gold in sport, silver in sport, bronze in sport, gold in sport + sport code, silver in sport + sport code, bronze in sport + sport code, gold in sport + code + sex, silver in sport + code + sex, bronze in sport + code + sex, athletes this year, athletes in code this year, athletes in sex this year, athletes in code + sex this year, athletes last year, athletes in code last year, athletes in sex last year, athletes in code + sex last year, gold this year, silver this year, bronze this year
            newLine = str(country) + "," + str(year) + "," + str(sex) + "," + str(sport) + "," + str(sportCode) + ",";
            goldInSport = 0;
            for key in goldMedals[country][sport]:
                for keyb in goldMedals[country][sport][key]:
                    for i in range(0, int(year)):
                        goldInSport += goldMedals[country][sport][key][keyb][i];
            goldInSportCode = 0;
            for key in goldMedals[country][sport][sportCode]:
                for i in range(0, int(year)):
                    gold = goldMedals[country][sport][sportCode][key].get(i, 0);
                    goldInSportCode += gold;
            goldInSportCodeSex = 0;
            for i in range(0, int(year)):
                goldInSportCodeSex = goldMedals[country][sport][sportCode][sex][i];
            
            silverInSport = 0;
            for key in silverMedals[country][sport]:
                for keyb in silverMedals[country][sport][key]:
                    for i in range(0, int(year)):
                        silverInSport += silverMedals[country][sport][key][keyb][i];
            silverInSportCode = 0;
            for key in silverMedals[country][sport][sportCode]:
                for i in range(0, int(year)):
                    silver = silverMedals[country][sport][sportCode][key].get(i, 0);
                    silverInSportCode += silver;
            silverInSportCodeSex = 0;
            for i in range(0, int(year)):
                silverInSportCodeSex = silverMedals[country][sport][sportCode][sex][i];

            bronzeInSport = 0;
            for key in bronzeMedals[country][sport]:
                for keyb in bronzeMedals[country][sport][key]:
                    for i in range(0, int(year)):
                        bronzeInSport += bronzeMedals[country][sport][key][keyb][i];
            bronzeInSportCode = 0;
            for key in bronzeMedals[country][sport][sportCode]:
                for i in range(0, int(year)):
                    bronze = bronzeMedals[country][sport][sportCode][key].get(i, 0);
                    bronzeInSportCode += bronze;
            bronzeInSportCodeSex = 0;
            for i in range(0, int(year)):
                bronzeInSportCodeSex = bronzeMedals[country][sport][sportCode][sex][i];

            athletesBaseThisYear = athletesBase[country][year];
            athletesCodeThisYear = athletesCode[country][year][sportCode];
            athletesSexThisYear = athletesSex[country][year][sex];
            athletesBothThisYear = athletesBoth[country][year][sportCode][sex];

            athletesBaseLastYear = athletesBase[country][year-1] if (int(year)-1) in athletesBase[country] else 0;
            athletesCodeLastYear = athletesCode[country][year-1][sportCode] if (year-1) in athletesCode[country] and sportCode in athletesCode[country][year-1] else 0;
            athletesSexLastYear = athletesSex[country][year-1][sex] if (year-1) in athletesSex[country] and sex in athletesSex[country][year-1] else 0;
            athletesBothLastYear = athletesBoth[country][year-1][sportCode][sex] if (year-1) in athletesBoth[country] and sportCode in athletesBoth[country][year-1] and sex in athletesBoth[country][year-1][sportCode] else 0;

            goldThisYear = goldMedals[country][sport][sportCode][sex][year];
            silverThisYear = silverMedals[country][sport][sportCode][sex][year];
            bronzeThisYear = bronzeMedals[country][sport][sportCode][sex][year];
            
            newLine += str(goldInSport) + "," + str(silverInSport) + "," + str(bronzeInSport) + str(goldInSportCode) + "," + str(silverInSportCode) + "," + str(bronzeInSportCode) + "," + str(goldInSportCodeSex) + "," + str(silverInSportCodeSex) + "," + str(bronzeInSportCodeSex) + "," + str(athletesBaseThisYear) + "," + str(athletesCodeThisYear) + "," + str(athletesSexThisYear) + "," + str(athletesBothThisYear) + "," + str(athletesBaseLastYear) + "," + str(athletesCodeLastYear) + "," + str(athletesSexLastYear) + "," + str(athletesBothLastYear) + "," + str(goldThisYear) + "," + str(silverThisYear) + "," + str(bronzeThisYear) + "\n";
            lines[lineNum] = str(lineNum) + "," + newLine;
            lineNum += 1;

            if (lineNum % 100 == 0):
                print(f"Processed {lineNum} lines");
            

        
        with open("dataFile.csv", 'w') as f:
            for line in lines:
                print(line, file=f);
                print(line);