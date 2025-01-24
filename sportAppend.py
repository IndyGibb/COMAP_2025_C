

sports = {}
with open('2025_Problem_C_Data/summerOly_programs.csv', 'r') as f:
    for line in f:
        line = line.strip()
        data = line.split(',')
        sports[data[2]] = data[0]
    f.close()

with open('sportCode.csv', 'r') as f:
    with open('sportCode2.csv', 'w') as g:
        for line in f:
            line = line.strip()
            data = line.split(',')
            data.insert(1, sports.get(data[1]))
            for i in range(len(data)):
                g.write(data[i])
                if i!= len(data) - 1:
                    g.write(',')
            g.write('\n')
        g.close()
    f.close()
        