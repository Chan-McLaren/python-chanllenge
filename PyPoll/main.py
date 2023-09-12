# modules import os so all systems can run
import os
import csv
# set path for file
csvpath = os.path.join("Resources", "election_data copy test.csv")
print(csvpath)
# open csv file and read the file
with open(csvpath, encoding='UTF-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
#read header and skip to the next line
    csv_header = next(csvfile)
#set variables to lists and dictionaries 
    Total_votes = []
    Candidates_votes = {}
    Winner = ""
 #read rows   
    for row in csv_reader:
#append the rows to total_votes
        Total_votes.append(row[0])
#look through coloumn 3 for candidates names and split them 
        Candidates_name = row[2]
        Candidates_name = Candidates_name.split(",")
#loop through candidates names       
        for name in Candidates_name:
#remove leading and trailing space from candidates name and set variable 
            Candidates = name.strip()
            if Candidates in Candidates_votes:
#add votes for the current candidate
                Candidates_votes[Candidates] = Candidates_votes[Candidates] + 1
#move to the next candidate
            else:
                Candidates_votes[Candidates] = 1
#calculate total_votes with length function   
    Total_votes = len(Total_votes)  
#Print out results of the election to terminal 
    print('Election Results')
    print('-----------------------------')
    print('Total Votes:', Total_votes)  
    print('-----------------------------')
#loop through candidates_vote dictionary and calculate percentage
    for Candidates, votes in Candidates_votes.items():
        percentage = (votes / Total_votes) * 100
#look to see if current candidate has more votes then current winner
        if Winner == "" or votes > Candidates_votes[Winner]:
            Winner = Candidates
        print(f'{Candidates}: {round(percentage, 3)}% ({votes})')
    print('-----------------------------')
    print('Winner:', Winner)
#Make a file in PyPoll, Analysis and record the results there   
output_path = os.path.join("Analysis","Election Results.text")
with open(output_path, 'w') as f:
    print('Election Results', file=f)
    print('-----------------------------', file=f)
    print('Total Votes:', Total_votes, file=f)  
    print('-----------------------------', file=f)
#same loop as above code lines: "40-45"
    for Candidates, votes in Candidates_votes.items():
        percentage = (votes / Total_votes) * 100
        if Winner == "" or votes > Candidates_votes[Winner]:
            Winner = Candidates
        print(f'{Candidates}: {round(percentage, 3)}% ({votes})', file=f)
    print('-----------------------------', file=f)
    print('Winner:', Winner, file=f)