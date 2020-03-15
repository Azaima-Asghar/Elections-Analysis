# The data we need to retrieve for the elections analysis.

# Import csv and os modules to read and manipulate data from the election_results.csv.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = 'Resources/election_results.csv'

# Assign a variable to save the file to a path.
file_to_save = ('Analysis/Election_Analysis.txt')
# Open the file to save and make a text file called election analysis.
text_file = open(file_to_save,'w')

# The total number of votes cast.

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

# Initialize a empty list to hold all the counties names.
counties_list = []

# Initialize a empty dictionary that will contain counties as keys and votes cast for counties as values.
counties_votes = {}

# Initialize a variable for the county with the largest votes turnover. 
county_with_largest_turnover = " "

# Initialize a variable for the county that gave the most votes.
most_voted_county = 0

# Initialize a variable for the county that voted the most.
most_voted_percentage_county = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the heeader row of election_results.csv.
    headers = next(file_reader)
    
    # Loop through the rows of the data.
    for row in file_reader:
        total_vote_count += 1
        
        # Complete list of candidates who recevied votes.
        candidate_name = row[2]

        # Complete list of counties present in the election data.
        county_name = row[1]

        # check if the candidate is present in the candidate list, if not then add that candidate to the list.
        if candidate_name not in Candidate_list:
            Candidate_list.append(candidate_name)

            # The total number of votes each canadidate recevied.
            # Set the number of votes for each canadidate to be zero initially.
            Candidate_votes[candidate_name] = 0

        # Check if the county id present in counties list, if not then add that county to the list. 
        if county_name not in counties_list:
            counties_list.append(county_name)

            # The total number of votes each county contributed in the election.
            # Set the number of votes for each county to be zero initially.

            counties_votes[county_name]=0

        # Increment the candidates votes to get the total number of votes for each candidate. 
        # This needs to be outside the if statement so that we can get the count of every vote for each candidate.
        Candidate_votes[candidate_name] += 1

        # Increment the counties votes to get the total number of votes for each county. 
        # This needs to be outside the if statement so that we can get the count of every vote for each county.
        counties_votes[county_name] += 1

# Save results to the text file.        
election_results = (
        f"\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes: {total_vote_count:,}\n"
        f"---------------------------\n"
        f"\nCounty Votes:\n")
print(election_results, end= "")

# Save the final vote count to the text file.
text_file.write(election_results)

# The percentage of votes cast for each county in the election.

# Iterate through the counties dictonary to get each county name.
# Then iterate through the counties dictonary to get the total number of votes for each county.

for counties in counties_votes:
    # Get the total votes for each county from the dictonary.  
    votes_for_county = counties_votes[counties]
    # The percentage of total votes for each county.
    vote_percentage_counties = float(votes_for_county) / float(total_vote_count) * 100
    
    #  The county with the largest turnover.

    # Calculate if the vote count is greater than the winning count and if vote percentage is greater than the winning percentage.
    if (total_vote_count > most_voted_county) and (vote_percentage_counties > most_voted_percentage_county):
        # If conditions true than make the county that voted the most to be the the votes for the county.
        most_voted_county = votes_for_county
        # Make most voted percentage of the conuty to be vote percentage of the county.
        most_voted_percentage_county = vote_percentage_counties
        # Set the largest turnout county name.
        Largest_turnout_county = counties
    
    # Save results.
    counties_vote_result = (
    f"{counties}: {vote_percentage_counties:.1f}% ({votes_for_county:,})\n")
    print(counties_vote_result)
    # Add to the text file.
    text_file.write(counties_vote_result)

counties_largest_turnout = ( 
    f"\n---------------------------\n"
    f"Largest County Turnout : {Largest_turnout_county}\n"
    f"---------------------------\n")
print(counties_largest_turnout)

# Add to the text file.
text_file.write(counties_largest_turnout)

#  The percentage of votes cast to each candidate 

# Iterate through the candidates list to get each candidate name.
# Then iterate through the candidate dictonary to get the total number of votes for each candidate.

for candidate in Candidate_votes:
    # Get the total votes for each candidate from the dictonary. 
    votes = Candidate_votes[candidate]
    # The percentage of total votes for each candidate.
    vote_percentage = float(votes) / float(total_vote_count) * 100

    # The winner of the elections based on the most number of votes (popular vote).

    # Calculate if the vote count is greater than the winning count and if vote percentage is greater than the winning percentage.
    if (total_vote_count > winning_count) and (vote_percentage > winning_percentage):
        # If conditions true than make the winning count to be the votes.
        winning_count = votes
        # Make winning percentage equal to vote percentage.
        winning_percentage = vote_percentage
        # Set the winning candidate to be the candidate's name.
        winnng_candidate = candidate

    # save candidate results to the text file.
    candidate_results = (f"{candidate}: {vote_percentage: .1f}% ({votes:,})\n")
    print(candidate_results)
    # Add to the text file.
    text_file.write(candidate_results)

winning_candidate_summary = (
f"---------------------------\n"
f"Winner: {winnng_candidate}\n"
f"Winning Vote Count: {winning_count:,}\n"
f"Winning Percentage: {winning_percentage:.1f}%\n"
f"---------------------------\n")

print(winning_candidate_summary)
# adding the winning summary to the text file.
text_file.write(winning_candidate_summary)

