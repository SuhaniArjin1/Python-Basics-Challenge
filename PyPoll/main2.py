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
    distinct_inputs = set()
    for row in csvreader:
        #getting sum of votes
        totalvotes += 1
        #getting the unique inputs from column 3
        distinct_inputs.add(row[2])
    #Getting vote count for each candidate
        if row[2] == "Charles Casper Stockham":
            Votes_Charles.append(row[0])
        if row[2] == "Diana DeGette":
            Votes_Diana.append(row[0])
        if row[2] == "Raymon Anthony Doane":
            Votes_Raymon.append(row[0])
    print("Total Votes:",totalvotes)
    Running_Candidates = distinct_inputs
    print (Running_Candidates)
#Put vote counts for each candidate into a list in order
Vote_count = [(len(Votes_Charles)), (len(Votes_Diana)),(len(Votes_Raymon))]
print(Vote_count)
def percent(x):
    return f"{round(((x/totalvotes)*100),3)}%"
charles_Percent =(percent(len(Votes_Charles)))
Diana_Percent = (percent(len(Votes_Diana)))
Raymon_Percent = (percent(len(Votes_Raymon)))
#Put each candidates percent of votes into a list in order
Percent_Vote = [charles_Percent, Diana_Percent, Raymon_Percent]
#Put all the voting values into a dictionary
Election_Outcome = {"Candidate": Running_Candidates,
                    "Percent_of_Votes" : Percent_Vote,
                    "Number_of_Votes": Vote_count}
print(Election_Outcome)