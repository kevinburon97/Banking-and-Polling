import os
import csv 
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath) as budgetdata:
    csvreader = csv.reader(budgetdata, delimiter=",")
   
    next(budgetdata) #skip header
    rowcount = 0
    totalprofit = 0
    totalchange = 0
    monthlychange = 0
    for row in csvreader: 
        rowcount = rowcount + 1  #Total months included in dataset
        totalprofit = totalprofit + int(row[1]) # net amount of profit/losses
        for x in range(rowcount):
            monthlychange = x+1(int(row[1])) - x(int(row[1]))
            print(monthlychange) 
        





#print("Total Months: " + str(rowcount))
#print("Total is $" + str(totalprofit))
    
budgetdata.close()
