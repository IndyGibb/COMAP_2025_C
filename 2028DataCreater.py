from dataCreate import dictGet

sports = dictGet('sport.csv');
sportCodes = dictGet('sportCode2.csv', keyLocation=3, valueLocation=2);
countries = dictGet('countryCode.csv')
newLine = "";
with open('2028 Sports and Countries.csv', 'r') as f:
    with open('2028 Sports and Countries2.csv', 'w') as g:
        header = f.readline()
        print(header, file=g)
        for line in f:
            data = [v.strip() for v in line.split(',')]
            data[1] = sports[data[0]];
            data[3] = sportCodes[data[2]];
            print(data);
            newLine = "";
            for i in range(len(data)):
                if i < len(data) - 1:
                    newLine += str(data[i]) + ",";
                else:
                    newLine += str(data[i]);
            print(newLine, file=g)
            print(newLine)