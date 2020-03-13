# The data we need to retrieve for the elections analysis 

# import csv and os modules to read and manipulate data from the election_results.csv
import csv

import os

# Assign a variable to load a file from a path.
#file_to_load = ('Elections-Analysis/Resources/election_results.csv')
file_to_load = 'Resources/election_results.csv'

# Assign a variable to save the file to a path.
#file_to_save = ('Elections-Analysis/Analysis/Election_Analysis.txt')
file_to_save = ('Analysis/Election_Analysis.txt')
# open the file to save and make a text file called election analysis.
text_file = open(file_to_save,'w')

# 1 The total number of votes casted

# Initialize a total vote counter.
total_vote_count = 0

# Initialize a empty list for candidates. 
Candidate_list = []

# Initialize a empty dictionary for candidates and the respective votes they received in total.
Candidate_votes = {}

# Initialize a variable to hold an empty string value for the winning candidate.
winnng_candidate = " "

# Initialize a variable for the winning count.
winning_count = 0

# Initialize a variable for the winning percentage.
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the heeader row of election_results.csv.
    headers = next(file_reader)
    # print (headers)
    
    for row in file_reader:
        total_vote_count += 1

        # 2 Complete list of candidates who recevied votes.
        candidate_name = row[2]
        if candidate_name not in Candidate_list:
            Candidate_list.append(candidate_name)
            # 3 The total number of votes each canadidate recevied.
            # set the number of votes for each canadidate to be zero initially.
            Candidate_votes[candidate_name] = 0
            # increment the candidates votes to get the total number of votes for each candidate. 
        # this needs to be outside the if statement so that we can get the count of every vote for each candidate.
        Candidate_votes[candidate_name] += 1

# save results to the text file.        
election_results = (
        f"\n Election Results\n"
        f"---------------------------\n"
        f"Total Votes: {total_vote_count:,}\n"
        f"---------------------------\n")
print(election_results, end= "")
    # save the final vote count to the text file.
text_file.write(election_results)

# 4 The percentage of votes casted to each candidate 

# iterate through the candidates list to get each candidate name.
# iterate through the candidate dictonary to get the total number of votes for each candidate.

for candidate in Candidate_votes:
    votes = Candidate_votes[candidate]
    #print(votes)
    # the percentage of total votes for each candidate.
    vote_percentage = float(votes) / float(total_vote_count) * 100
    #print(vote_percentage)

    # 5 The winner of the elections based on the most number of votes (popular vote).

    # calculate if the vote count is greater than the winning count and if vote percentage is greater than the winning percentage.
    if (total_vote_count > winning_count) and (vote_percentage > winning_percentage):
        # if conditions true than make the winning count to be the votes.
        winning_count = votes
        # make winning percentage equal to vote percentage.
        winning_percentage = vote_percentage
        # set the winning candidate to be the candidate's name.
        winnng_candidate = candidate

    # print the winning canadidate, vote count and percentage.
    # print (f" {candidate}: {winning_percentage: .1f}% ({votes:,})\n")

    # save candidate results to the text file.
    candidate_results = (f"{candidate}: {vote_percentage: .1f}% ({votes:,})\n")
    print(candidate_results)
    # Add to the text file.
    text_file.write(candidate_results)

# print the total number of votes.
# print (total_vote_count)

# print the candidate list. 
# print (Candidate_list)

# print the total number of votes for each candidate.
# print(Candidate_votes) 

# printing candidate summary of votes.
winning_candidate_summary = (
f"---------------------------\n"
f"Winner: {winnng_candidate}\n"
f"Winning Vote Count: {winning_count}\n"
f"Winning Percentage: {winning_percentage:.1f}%\n"
f"---------------------------\n")

print(winning_candidate_summary)
# adding the winning summary to the text file.
text_file.write(winning_candidate_summary)
