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
#Since Gain stored as positive number an loss stored as negative, simply take the sum of the list to find net gain/loss
#Average chnage is the change over each month over the total number of months -1 (exculding the first one)
Net = 0
previousprofit = float(NetAmount[0])
#Loop through the rows to get the sum of items in the NetAmount list
#Loops through the amounts and get the monthly change 
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

#zip date and monthly change and find greatest increase
DateNChange = zip(date, MonthlyChange)
#for finding max
max_row = None
max_value = 0
#for finding min
min_row = None
min_value = 1862002
for change in DateNChange:
    if change[1] > max_value:
        max_value = change[1]
        max_row = change
    if change[1] < min_value:
        min_value = change[1]
        min_row = change
print("Greatest Increase in Profits:",max_row)
print("Greatest Decrease in Profits:",min_row)
