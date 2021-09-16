# Election_Analysis

## Overview of Project
The local Election Commission has asked if there is an efficient and repeatable methodoloy to accurately tabulate election results. Using their most recent election as a starting point, this analysis will use Python to establish a process for tabulating election outcomes which can be leveraged for future elections.

## Analysis
The data set (Resources/election_results.csv) contained nearly 370,000 rows of voting returns. Each row consisted of the Ballot_ID (unique identifier for the vote record), County the vote was cast in and the Candidate who received the vote. Due to the volume of data, Python was used to parse the data and to compile the necessary results to answer the following questions:
1. Which candidate won?
2. What were the results for each candidate?
3. What was overall voter turnout? 
4. What was voter turnout by county?

Besides determining the overall election results, there was a requirement to write the results to a file.

### Investigation of source data

The source data, election_results.csv, is a comma separate value (CSV) file that contains headers and three (3) columns of data per row.
```    
$ head election_results.csv
Ballot ID,County,Candidate
1323913,Jefferson,Charles Casper Stockham
1005842,Jefferson,Charles Casper Stockham
1880345,Jefferson,Charles Casper Stockham
1600337,Jefferson,Charles Casper Stockham
1835994,Jefferson,Charles Casper Stockham
1772756,Jefferson,Charles Casper Stockham
1920023,Jefferson,Charles Casper Stockham
1040408,Jefferson,Charles Casper Stockham
1018414,Jefferson,Charles Casper Stockham

```
Further, we can see the file has 369,712 rows (including the header) of data:
 ```
$ cat election_results.csv | wc -l
369712

```
### Python Analysis Steps

The following key steps were undertaken using Python.

#### 1) Import the required libraries to work with CSV files and local computer folders

```
import csv, os
```

#### 2) Load source data and identify the file to write results to.
```
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
```
#### 3) Setup initial variables, lists and dictionaries.
```
# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# Create a county list and county votes dictionary.
county_list = []
county_votes_dict = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the largest county and county voter turnout.
largest_county = ""
largest_county_turnout = 0
```

#### 4) Identify candidates and their count of votes.
```
# If the candidate does not match any existing candidate add it to the candidate list
if candidate_name not in candidate_options:

    # Add the candidate name to the candidate list.
    candidate_options.append(candidate_name)

    # And begin tracking that candidate's voter count.
    candidate_votes[candidate_name] = 0

# Add a vote to that candidate's count
candidate_votes[candidate_name] += 1
```

#### 5) Identify counties and their count of votes.
```
# Write an if statement that checks that the county does not match any existing county in the county list.
if county_name not in county_list:

    # Add the existing county to the list of counties.
    county_list.append(county_name)

    # Begin tracking the county's vote count.
    county_votes_dict[county_name] = 0

# Add a vote to that county's vote count.
county_votes_dict[county_name] += 1
```

#### 6) Calculate candidate results and the overall winning candidate.
```
for candidate_name in candidate_votes:

    # Retrieve vote count and percentage
    votes = candidate_votes.get(candidate_name)
    vote_percentage = float(votes) / float(total_votes) * 100
    candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Print each candidate's voter count and percentage to the terminal.
    print(candidate_results)
    #  Save the candidate results to our text file.
    txt_file.write(candidate_results)

    # Determine winning vote count, winning percentage, and candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage
```

#### 7) Calculate county results and the county with the highest turnout.
```
for county_name in county_votes_dict:

    # Retrieve the county vote count.
    total_county_votes = county_votes_dict[county_name]

    # Calculate the percentage of votes for the county.
    county_vote_percentage = float(total_county_votes) / float(total_votes) * 100
    county_results = (f"{county_name}: {county_vote_percentage:.1f}% ({total_county_votes:,})\n")
        
    # Print the county results to the terminal.
    print(county_results)
       
    # Save the county votes to a text file.
    txt_file.write(county_results)
        
    # Write an if statement to determine the winning county and get its vote count.
    if (total_county_votes > largest_county_turnout):
        largest_county_turnout = total_county_votes
        largest_county = county_name
```

#### 8) Finally, print results to terminal and write the results to a file.
```
# Print the winning candidate (to terminal)
winning_candidate_summary = (
    f"------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Candidate Vote Count: {winning_count:,}\n"
    f"Winning Candidate Percentage: {winning_percentage:.1f}%\n"
    f"------------------------------\n")
print(winning_candidate_summary)

# Save the winning candidate's name to the text file
txt_file.write(winning_candidate_summary)

# Print the county with the largest turnout to the terminal.
county_with_largest_turnout = (
    f"------------------------------\n"
    f"Largest County Turnout: {largest_county}\n"
    #f"Winning County Voter Turnout: {largest_county_turnout:,}\n"
    f"------------------------------\n\n"
print(county_with_largest_turnout)

# Save the county with the largest turnout to a text file.
txt_file.write(county_with_largest_turnout)
```

## Results
The outcome of the election:
- Total Votes/Turnout = 369,711
- Election Winner: Diana DeGette
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)
- County with highest turnout: Denver
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)

These results can be seen in the terminal output:

![election_results_terminal](https://user-images.githubusercontent.com/89284280/133538428-073fc7ed-8309-48aa-bd8d-4ad5b73e1e98.PNG)


## Summary

The Python script which was established produces the outcome that was asked for during the outset of this analysis. The script is structured, as illustrated above, in an intuitive way that will allow the Election Commission to make subtle modifications in order to meet future elections needs. For example...

#### Additional data is captured in the election results file which alters the column assignments
The current working file, election_results.csv, only has 3 columns: Ballot_ID, County and Candidate. However, if there was a desire to add in voter information this could change the order in which the current columns are found. If the Candidate column changes the script would need to be updated to be able to identify the candidates and to tally their results. At present, since Candidate is in the third column it is identified in the script:
```
        # Get the candidate name from each row.
        candidate_name = row[2] # column indexing starts at 0, so column 3 is identified using 2
```
To update this script looking for Candidate in another column, the election commission would simply have to alter the index to whichever column the candidate names are found in.

#### Write results to a different election_analysis file
At present, the current script writes to a file generically named "election_analysis.txt". However, to prevent the Election Commission from over-writing a previous file, they should update the name of the output file based on which election they are analyzing. They can do this by changing:
```
file_to_save = os.path.join("analysis", "election_analysis.txt")
```
To another name, such as:
```
file_to_save = os.path.join("analysis", "election_analysis_2020_Govenor.txt")
```
Because the filename `election_analysis.txt` is mapped to the variable `file_to_save`, all that needs to change in the script is the filename in this one location.

Doing this will ensure the results are written to a unique file and do not overwrite a previous analysis.

