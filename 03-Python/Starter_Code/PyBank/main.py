import os
import csv

# Set path for file
csvpath = "Resources/budget_data.csv"

# variables
total_months = 0
total_profit_loss = 0
last_profit_loss = 0
profit_changes = []
max_change = -9999999999
min_change = 999999999
max_month = ""
min_month = ""

# Open the CSV using UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the first row as a header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Received assistance from Prof Booth

    # Loop through each row of data after the header
    for row in csvreader:

        # If not the first month then profit change is profit/loss column - the previous profit/loss, then append the changes into a list
        if total_months != 0:
            profit_change = int(row[1]) - last_profit_loss
            profit_changes.append(profit_change)

            # if the profit change is greater than the last one then this is the new max change and set the max month equal to this month
            if profit_change > max_change:
                max_change = profit_change
                max_month = row[0]
            # if the profit change is less than the last one then this is the new min change and set the min month equal to this month   
            elif profit_change < min_change:
                min_change = profit_change
                min_month = row[0]
            else:
                pass # keep going

        # set the last profit
        last_profit_loss = int(row[1])

        # add all the profit/loss values as it loops through the CSV
        total_profit_loss += int(row[1])         

        # add 1 for each row to count the months
        total_months += 1

    # print variables
    print(total_months)
    print(total_profit_loss)

    avg_change = round(sum(profit_changes)/ len(profit_changes),2)
    print(avg_change)

    print(max_change)
    print(max_month)

    print(min_change)
    print(min_month)


# Financial Analysis summary
txtfile = f"""
Financial Analysis
--------------
Total Months: {total_months}
Total: ${total_profit_loss}
Average Change: ${avg_change}
Greatest Increase in Profits: {max_month} (${max_change})
Greatest Decrease in Profits: {min_month} (${min_change})
"""
print(txtfile)

# create and write results to CSV
# https://www.adamsmith.haus/python/answers/how-to-write-a-variable-to-a-file-in-python
file = open("PyBank_resuls.txt", "w")
file.write(txtfile)
file.close()