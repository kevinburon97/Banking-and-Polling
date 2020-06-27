import os
import csv 
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join("Resources","budget_data.csv")
outputpath = os.path.join("Analysis", "Analysis.csv")
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
         #add values to list rowcount
        rowcount.append(row[1]) 
        monthlyvalue = int(row[1])
        # net amount of profit/losses
        totalprofit = totalprofit + monthlyvalue 
    for x in range(1,len(rowcount)):
        #Add to the list monthly rev the monthly change for each row
        monthlyrev.append(int(rowcount[x])-int(rowcount[x-1]))                      
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with open(outputpath) as output:
        csvwriter = csv.writer(output)
        budgetdata.write("Financial Analysis")
print("Financial Analysis")
print( "---------------------------------")
print("Total Months: " + str(len(rowcount)))
print("Total is $" + str(totalprofit))
print("Average Change: $"+str(round(sum(monthlyrev)/(len(rowcount)-1),2)))    
print("Greatest increase in PRofits: $"+ str(max(monthlyrev)))      
print("Greatest Decrease in Profits: $"+ str(min(monthlyrev)))


