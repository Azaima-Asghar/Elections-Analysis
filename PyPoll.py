# The data we need to retrieve for the elections analysis 

# 1 The total number of votes casted
# 2 Complete list of candidates who recevied votes 
# 3 The percentage of votes casted to each candidate 
# 4 The total number of votes each canadidate recevied 
# 5 The winner of the elections based on the most number of votes (popular vote)

# import csv module to read and manipulate data from the election_results.csv
import csv

# import radom module 

import random

# import numpy module

# Assign a varialbe to the path of election_results.csv file to load 

# direct way to get the file path 

file_to_load = 'Elections-Analysis/Resources/election_results.csv'

# indirect way to get the file path 

# import os
# file_to_load = os.path.join("Resources", "election_results.csv")

# open the election data file and read it 

with open(file_to_load) as election_data:
    print (election_data)

# create a file name variable to the path of the file 

file_to_save = "Elections-Analysis/Analysis/Election_analysis.txt"

open(file_to_save,'w')

# perform analysis on the election data 



