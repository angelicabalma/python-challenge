import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

#The total number of votes cast
total_votes = 0
#A complete list of candidates who received votes
candidates_voted = []
#The total number of votes each candidate won
won_votes = []
#Names of Candidates
candidate_name = []
#Percent voted
percentage_votes = []
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
     

    for row in csvreader:

        #Adding total votes
        total_votes = total_votes + 1

        # Add Candidates
        candidates_voted.append(row[2])

        #Finding the specific names of candidates 
    for y in set(candidates_voted):
        candidate_name.append(y)

        #Counting their total votes
        candidates_total = candidates_voted.count(y)
        won_votes.append(candidates_total)

        #Finding the percentage of votes 
        candidates_percent = (candidates_total/ total_votes)*100
        percentage_votes.append(candidates_percent)
    
    winner_candidate = max(won_votes)
    the_winner = candidates_voted[won_votes.index(winner_candidate)]





print("Election Results")
print("------------------------")
print(f"Total Votes:  {total_votes}")
print("------------------------")
for i in range(len(candidate_name)):
    print(candidate_name[i] + ": " + str("{0:.2f}".format(percentage_votes[i]))+"% ("+ str(won_votes[i])+")")
print("------------------------")   
print(f"Winner: {the_winner}")

with open("election_analysis.txt", "w") as txt_file:
    
    txt_file.write("Election Results\n")
    txt_file.write("------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("------------------------\n")
    for i in range(len(candidate_name)):
        txt_file.write(candidate_name[i] + ": " + str("{0:.2f}".format(percentage_votes[i]))+"% ("+ str(won_votes[i])+")")
    txt_file.write("------------------------")
    txt_file.write(f"Winner: {the_winner}")

    txt_file.close()
    

    
