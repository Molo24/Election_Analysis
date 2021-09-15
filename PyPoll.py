'''
The data we need to retrieve
1. The total number of votes cast
2. A complete list of candidates who received votes
3. The percentage of votes each candidate won
4. The total number of votes each candidate won
5. The winner of the election based on popular vote.
'''

import csv, os

'''
### Direct Path Methodology
# Assign a variable for the file to load and the path
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)
'''
'''
### Indirect Path Methodology
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)


# Writing Data to File
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
'''
'''
# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()
'''
'''
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Arapahoe, Denver, Jefferson") # adds them all to same line separate by a comma
    txt_file.write("Arapahoe\nDenver\nJefferson") # add each to their own line
'''

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

candidate_options = [] # new empty list for candidates

candidate_votes = {} # declare empty dictionary. Below we create the key = candidate name & value is candidate votes

# Winning Candidate and Winning Count Tracker
winning_candidate = "" # declare a variable that holds an empty string value for the winning candidate.
winning_count = 0 # Declare a variable for the winning count equal to zero.
winning_percentage = 0 # Declare a variable for the winning percentage equal to zero.

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    # The variable, file_reader, is referencing the file object, which is stored in memory.
    # To "pull" the data out of the file object, we can iterate through the file_reader variable and print each row, including the headers, or column names.

    # Print the header row
    headers = next(file_reader)
    #print(headers)

    # Print each row in the CSV file
    for row in file_reader:
        #print(row)

        # 2. Add to the total vote count.
        total_votes += 1

        # Identify the candidate name in each column and assign it to a variable
        candidate_name = row[2]

        # If statement ONLY to Add the candidate name to the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begin tracking the vandidate's vote count
            candidate_votes[candidate_name] = 0 
                # create each candidate as a key in the dictionary. dict_name[key] gets the value for the key and also allows you to create a key.
                # Then we set each candidate vote to 0 so can then start tallying their votes.

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# 3. Print the total votes.
#print(total_votes)

# Print Candidate Options unique list
#print(candidate_options)

# Print candidate vote dictionary
#print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate_list.
for candidate_name in candidate_votes:
    
    # Retrieve the vote count of a candidate.
    votes = candidate_votes[candidate_name]

    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # Print the candidate name and percentage of votes.
    #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determien winning vote count and candidate
    # Determine if the votes is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        
        # If true, then set winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage

        # And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

#print(winning_count)
#print(winning_percentage)
#print(winning_candidate)
#print("\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)