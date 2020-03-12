# The data we need to retrieve for the elections analysis 


# 4 The percentage of votes casted to each candidate 
# 5 The winner of the elections based on the most number of votes (popular vote)

# import csv and os modules to read and manipulate data from the election_results.csv
import csv

import os

# Assign a variable to load a file from a path.
file_to_load = ('Elections-Analysis/Resources/election_results.csv')

# Assign a variable to save the file to a path.
file_to_save = ('Elections-Analysis/Analysis/Election_Analysis.txt')

# 1 The total number of votes casted
# Initialize a total vote counter.
total_vote_count = 0

# Initialize a empty list for candidates. 
Candidate_list = []

# Initialize a empty dictionary for candidates and the respective votes they received in total.
Candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the heeader row of election_results.csv.
    headers = next(file_reader)
    print (headers)
    
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

# iterate through the candidates list to get each candidate name.
# iterate through the candidate dictonary to get the total number of votes for each candidate.
for candidate in Candidate_votes:
    votes = Candidate_votes[candidate]
    # the percentage of total votes for each candidate.
    vote_percentage = int(votes) / int(total_vote_count) * 100
    print (f"{candidate} : recieved {vote_percentage} % of the vote.")

# print the total number of votes.
print (total_vote_count)

# print the candidate list. 
print (Candidate_list)

# print the total number of votes for each candidate.
print(Candidate_votes)    
   
