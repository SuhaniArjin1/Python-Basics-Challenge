#import modules
import csv
import os
#Create file path
csvpath = os.path.join('PyBank','Resources1', 'budget_data.csv')
#Create lists
date = []
NetAmount = []
MonthlyChange = []
#Create a CSV file reader
with open (csvpath, encoding = 'UTF-8') as csvfile:
    csvreader = csv.reader (csvfile, delimiter= ',')
    #Skip header
    csv_header = next(csvreader)
    #loop through and add the months to a list
    for row in csvreader:
        date.append(row[0]) #has every month in every year
        NetAmount.append(row[1])#has all the gains and losses for each month
    #Find out length of the list for total number of months since each month is only mentioned once
    total_months = len(date)
    print("Total Months:", total_months) 
#Since Gain stored as positive number an dloss stored as negative number I can simply take the sum of the list to find net gain/loss
#Average chnage is the change over each month over the total number of months -1 (exculding the first one)
Net = 0
previousprofit = float(NetAmount[0])
#Loop through the rows and add the amounts to get the sum of items in the NetAmount list
#Loops through the amounts and get the monthly change by subtracting the previous month by the current month and add it to the list
for Amount in NetAmount:
    Net += float(Amount)
    Currentprofit = float(Amount)
    CurrentChange = Currentprofit - previousprofit
    MonthlyChange.append(CurrentChange)
    #Set previous profit amount for next loop
    previousprofit = float(Amount)
#Calculate average change
averageChange = sum(MonthlyChange)/(total_months-1)
print("Total: $",Net)
print("Average Change $",averageChange)

