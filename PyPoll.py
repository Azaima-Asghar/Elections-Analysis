# The data we need to retrieve for the elections analysis 

# 1 The total number of votes casted
# 2 Complete list of candidates who recevied votes 
# 3 The percentage of votes casted to each candidate 
# 4 The total number of votes each canadidate recevied 
# 5 The winner of the elections based on the most number of votes (popular vote)

# import csv and os modules to read and manipulate data from the election_results.csv
import csv

import os

# Assign a variable to load a file from a path.
file_to_load = ('Elections-Analysis/Resources/election_results.csv')

# Assign a variable to save the file to a path.
file_to_save = ('Elections-Analysis/Analysis/Election_Analysis.txt')

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the heeader row of election_results.csv
    headers = next(file_reader)
    print (headers)
