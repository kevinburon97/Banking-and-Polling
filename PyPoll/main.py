import os
import csv
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join("Resources/election_data.csv")

with open(csvpath) as electiondata: 
    csvreader = csv.reader(electiondata,delimiter=",")
    #Skip header
    next(electiondata)
    
    totalrows = []
    Khan = []
    Li = []
    Correy = []
    OTooley = []
    #Go through each row to find which vote went to which candidate and add it to their respective list
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
    
    #The % of votes each candidate had  
    pctgKhan = len(Khan)/len(totalrows)
    pctgLi =  len(Li)/len(totalrows)
    pctgCorrey =  len(Correy)/len(totalrows)
    pctgOTooley =  len(OTooley)/len(totalrows)
print("Election Results:")
print( "---------------------------------")
print("Total Votes:" + str(len(totalrows)))
print( "---------------------------------")
print("Candidates:")
print("Khan: " + format(pctgKhan,".2%") + " total votes: ("+ str(len(Khan)) + ")")
print("Li: " + format(pctgLi,".2%") + " total votes: ("+ str(len(Li)) + ")")
print("Correy: " + format(pctgCorrey,".2%")+ " total votes: ("+ str(len(Correy)) + ")")
print("O'Tooley: " + format(pctgOTooley,".2%") + " total votes: ("+ str(len(OTooley)) + ")")
print( "---------------------------------")
#Find which candidate had the most votes and keep the # of votes under winner
winner = max(len(Khan),len(Li),len(Correy),len(OTooley))
#Create a dictionary listing the votes of each candidate with their name as a value
biglist = {len(Khan): "Khan", len(Li): "Li", len(Correy): "Correy", len(OTooley): "O'Tooley"}
#Go through the dictionary and print the one that matches winner
for x in biglist:
    if winner == x:
       print("And the winner is: " +biglist.get(x))    
print("---------------------------------")
