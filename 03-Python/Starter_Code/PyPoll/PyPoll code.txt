# Modules
import os
import csv

# Set path for file
csvpath = "Resources/election_data.csv"

# variables
total_votes = 0
candidate_names = {}
candidate_names_perc = {}

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the first row as the header row 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # read each row in the csv
    for row in csvreader:
        total_votes += 1

        # candidate names in the 3rd column
        candidate = row[2]

        # if the 3rd column has a name not in the dictionary add the name and give it a value of 1
        if candidate in candidate_names.keys():
            candidate_names[candidate] += 1
        # if the name is in the dictionary already add 1 to its value
        else:
            candidate_names[candidate] = 1
        
        #for all the values in the dictionary (votes) divide by the total number of votes and multiply by 100
        for votes in candidate_names.keys():
            candidate_names_perc[votes] = candidate_names[votes] / total_votes*100

            # Get the key with the largest (maximum) value in the dictionary
            # https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
        winner = max(candidate_names, key=candidate_names.get)
            

# print variables
print(f"{total_votes} total votes")
print(f"Each candidate and their respective received votes: {candidate_names}")
print(f"Each candidate and their respective percentage of votes received: {candidate_names_perc}")
print(f"The winner is...{winner}")

# print to txt file
# help from prof Booth

txtfile = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------\n"""
# loop through each candidate-vote pair in the dictionary
for key in candidate_names.keys():
    # for each value (number of votes) in the dictionary get the percent of votes received
    percent = round(100*candidate_names[key]/total_votes, 3)
    #Print the candidate (key) percent 
    results = f"{key}: {percent}% ({candidate_names[key]})\n"
    # add this section to the total votes already printed
    txtfile += results 

# add the winner to txt file
lastline = f"""
--------------------
Winner: {winner}
----------------------
"""
txtfile += lastline
print(txtfile)

# create and write results to CSV
# https://www.adamsmith.haus/python/answers/how-to-write-a-variable-to-a-file-in-python
file = open("PyPoll_resuls.txt", "w")
file.write(txtfile)
file.close()