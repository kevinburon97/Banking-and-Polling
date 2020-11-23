import os
import csv 
os.chdir(os.path.dirname(os.path.abspath(__file__)))
csvpath = os.path.join("Resources","budget_data.csv")

#Read the csv file
with open(csvpath) as budgetdata:
    csvreader = csv.reader(budgetdata, delimiter=",")
#Once it is read, I created variables for all things I am interested in   
    next(budgetdata) #skip header
    rowcount = []
    totalprofit = 0
    totalchange = 0
    prevvalue = 0
    totalrev = 0
    monthlyrev = []
#Go through each of the rows in the dataframe and perform various operations
    for row in csvreader: 
         #add values to list rowcount
        rowcount.append(row[1]) 
        monthlyvalue = int(row[1])
        # net amount of profit/losses
        totalprofit = totalprofit + monthlyvalue 
    for x in range(1,len(rowcount)):
        #Add to the list monthly rev the monthly change for each row
        monthlyrev.append(int(rowcount[x])-int(rowcount[x-1]))                      

# create a variable that contains all the information processed above
output=(       
f"Financial Analysis\n"
f"---------------------------------\n"
f"Total Months:{(len(rowcount))}\n"
f"Total is $ {(totalprofit)}\n"
f"Average Change: ${(round(sum(monthlyrev)/(len(rowcount)-1),2))}\n"    
f"Greatest increase in Profits: ${(max(monthlyrev))}\n"      
f"Greatest Decrease in Profits: ${(min(monthlyrev))}\n")

outputpath = os.path.join("Analysis", "Analysis.txt")
#Print output
print(output)
#Create a csv file with all the output
with open(outputpath, "w") as txt_file:
    txt_file.write(output)