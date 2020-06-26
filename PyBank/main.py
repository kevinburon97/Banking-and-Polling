import os
import csv 
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath) as budgetdata:
    csvreader = csv.reader(budgetdata, delimiter=",")
   
    next(budgetdata) #skip header
    rowcount = []
    totalprofit = 0
    totalchange = 0
    prevvalue = 0
    totalrev = 0
    monthlyrev = []
    for row in csvreader: 
        rowcount.append(row[1])  #add values to list rowcount
        monthlyvalue=int(row[1])
        totalprofit = totalprofit + monthlyvalue # net amount of profit/losses
    for x in range(1,len(rowcount)):
            monthlyrev.append(int(rowcount[x])-int(rowcount[x-1]))                      
       
print("Total Months: " + str(len(rowcount)))
print("Total is $" + str(totalprofit))
print("$"+str(round(sum(monthlyrev)/(len(rowcount)-1),2)))    
budgetdata.close()
