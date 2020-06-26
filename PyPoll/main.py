import os
import csv
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join("Resources/election_data.csv")

with open(csvpath) as electiondata: 
    csvreader = csv.reader(electiondata,delimiter=",")

    next(electiondata)
    totalrows = []
    Khan = []
    Li = []
    Correy = []
    OTooley = []
    for row in csvreader:
        totalrows.append(row[0])
        if row[2]=="Khan":
            Khan.append(row[2])
        elif row[2]=="Li":
            Li.append(row[2])
        elif row[2]=="Correy":
            Correy.append(row[2])
        else:
            OTooley.append(row[2])
    

print(len(totalrows))
print(format(len(Khan)/len(totalrows),..0%)
print(len(Li)/len(totalrows))
print(len(Correy)/len(totalrows))
print(len(OTooley)/len(totalrows))
