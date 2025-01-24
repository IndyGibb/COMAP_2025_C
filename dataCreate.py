from collections import defaultdict

def dictGet(filePath: str, keyLocation: int = 1, valueLocation: int = 0, fileDelim: str = ','):
    dictionary = {}
    with open(filePath, 'r') as f:
        for line in f:
            data = line.strip().split(fileDelim)
            dictionary[data[keyLocation]] = data[valueLocation]
        f.close()
    return dictionary

def sportsGet(filePath: str, keyLocation: int = 1, fileDelim: str = ','):
    sports = {}
    with open(filePath, 'r') as f:
        for line in f:
            data = line.strip().split(fileDelim)
            sports[data[keyLocation]] = data
        f.close()
    return sports


# End file header:
# country code, year, sex, sport, sport code, gold in sport, silver in sport, bronze in sport, gold in sport + sport code, silver in sport + sport code, bronze in sport + sport code, gold in sport + code + sex, silver in sport + code + sex, bronze in sport + code + sex, athletes this year, athletes in code this year, athletes in sex this year, athletes in code + sex this year, athletes last year, athletes in code last year, athletes in sex last year, athletes in code + sex last year, gold this year, silver this year, bronze this year

if __name__ == "__main__":
    goldMedals = {} # multi-level dictionary with first level being country, second being sport, third being sport code, fourth being sex, key being an integer representing the number of medals
    silverMedals = {}
    bronzeMedals = {}
    athletes = {}
    countryCodes = dictGet('countryCode.csv')
    years = dictGet('yearsChanger.csv')
    sportCodes = sportsGet('sportCode2.csv')
    with open('2025_Problem_C_Data\summerOly_athletes.csv', 'r') as f:
        next(f)  # Skip header line
        for line in f:
            data = line.strip().split(',')
            if "Gold" in data[8]:
                if not goldMedals.get(countryCodes[data[3]]):
                    goldMedals[countryCodes[data[3]]] = {}
                if not goldMedals[countryCodes[data[3]]].get():
                    

            
