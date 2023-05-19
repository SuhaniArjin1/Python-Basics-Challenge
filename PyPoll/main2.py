#import modules
import csv
import os
#create file path
csvpath = os.path.join('PyPoll', 'Resources2', 'election_data.csv')
#create lists
candidates = []
Votes_Charles = []
Votes_Diana = []
Votes_Raymon = []
#make it readable
with open(csvpath, encoding= 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    #skip header
    csv_header = next(csvreader)
    #find total number of ballot ID's to find total number of votes
    totalvotes = 0
    distinct_inputs = list(set())
    for row in csvreader:
        #getting sum of votes
        totalvotes += 1
        #getting the unique inputs from column 3
        if row[2] not in distinct_inputs:
            distinct_inputs.append(row[2])
    #Getting vote count for each candidate
        if row[2] == "Charles Casper Stockham":
            Votes_Charles.append(row[0])
        if row[2] == "Diana DeGette":
            Votes_Diana.append(row[0])
        if row[2] == "Raymon Anthony Doane":
            Votes_Raymon.append(row[0])
    
    Running_Candidates = distinct_inputs
    
#Put vote counts for each candidate into a list in order
Vote_count = [(len(Votes_Charles)), (len(Votes_Diana)),(len(Votes_Raymon))]

def percent(x):
    return f"{round(((x/totalvotes)*100),3)}%"
charles_Percent =(percent(len(Votes_Charles)))
Diana_Percent = (percent(len(Votes_Diana)))
Raymon_Percent = (percent(len(Votes_Raymon)))
#Put each candidates percent of votes into a list in order
Percent_Vote = [charles_Percent, Diana_Percent, Raymon_Percent]

election_results = list(zip(Running_Candidates, Percent_Vote, Vote_count))
#Finding Winner 
max_row = None
max_value = 0

for result in election_results:
    if result[2] > max_value:
        max_value = result[2]
        max_row = result

output_path = os.path.join('PyPoll','Analysis2','PyPoll_Results.csv')
with open(output_path, 'w') as file:
    file.write(f"Election Results\n")
    file.write("-----------------------------\n")
    file.write(f"Total Votes: {totalvotes}\n")
    file.write("-----------------------------\n")
    for result in election_results:
        file.write(f"{result[0]}: {result[1]} ({result[2]})\n")
    file.write("-----------------------------\n")
    file.write(f"Winner: {max_row[0]}")