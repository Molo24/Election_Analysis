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

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    # The variable, file_reader, is referencing the file object, which is stored in memory.
    # To "pull" the data out of the file object, we can iterate through the file_reader variable and print each row, including the headers, or column names.

    #for row in file_reader:
    #    print(row)
    
    # Pring the header row
    headers = next(file_reader)
    print(headers)