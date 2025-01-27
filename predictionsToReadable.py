from dataCreate import dictGet
from collections import defaultdict
from defaultlist import defaultlist

sexValues = {0 : 'M/Both', 1: 'F'};
countryCodes = dictGet("countryCode.csv", keyLocation = 0, valueLocation = 1, valueType = 'string');
yearCodes = dictGet("yearsChanger.csv", keyLocation = 0, valueLocation = 1, valueType = 'string');
sports = dictGet("sportCode2.csv", keyLocation = 0, valueLocation = 1, valueType = 'string');
sportCodes = dictGet("sportCode2.csv", keyLocation = 2, valueLocation = 3, valueType = 'string');

countryMedals = defaultdict(lambda: defaultlist(lambda: 0));

with open("2028Predictions.csv", 'r') as f:
    with open("2028Predictions_ReadableFull.csv", 'w') as g:
        next(f);
        print("Country,Year,Sex,Sport,Discipline,Gold,Silver,Bronze", file=g);
        for line in f:
            data = line.split(',');
            data = [v.strip() for v in data];
            country = countryCodes[data[1]];
            year = yearCodes[data[2]];
            sex = sexValues[int(data[3])];
            sport = sports[data[4]];
            discipline = sportCodes[data[5]];
            gold = data[23];
            silver = data[24];
            bronze = data[25];
            countryMedals[country][0] += int(gold);
            countryMedals[country][1] += int(silver);
            countryMedals[country][2] += int(bronze);
            print(f"{country},{year},{sex},{sport},{discipline},{gold},{silver},{bronze}", file=g);

with open("2028Predictions_ReadableSimple.csv", 'w') as h:
    print("Country,Gold,Silver,Bronze", file=h);
    for country, medals in countryMedals.items():
        print(f"{country},{medals[0]},{medals[1]},{medals[2]}", file=h);
