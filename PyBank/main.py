# import modules and dependencies
# ideas as solution:  https://butler.bootcampcontent.com/Joel/homework/-/blob/5676aadd19a34e7d08de68b986c2e99140d47788/Python-Challenge/Solutions/PyBank/PyBank.py

#import os
#import csv

#Files to open
#PyBankcsv= os.path.join("budget_data.csv")
# Files to output (
#FinalAnalysis = os.path.join("analysis", "budget_analysis.txt")

# make empty buckets
#total_months = []
#total_profit_loss = []
#profit_loss_change = []
#profit_loss_average = []
#greatest_increase = []
#greatest_decrease = []



#with open(PyBankcsv) as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=',')

# Find The total number of months included in the dataset
# Find The net total amount of "Profit/Losses" over the entire period
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

# -*- coding: UTF-8 -*-
"""PyBank Homework Solution."""

# Dependencies
import csv
import os

# Files to load and output (Remember to change these)
PyBankcsv= os.path.join("Resources", "budget_data.csv")
FinalAnalysis = os.path.join("analysis", "output.txt")
#file_to_load = os.path.join("Python_Pybank_budget_data.csv")
#file_to_output = os.path.join("analysis", "budget_analysis.txt")

# Track various financial parameters
#total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
#greatest_decrease = ["", 9999999999999999999]
#total_net = 0

# Read the csv and convert it into a list of dictionaries
with open(PyBankcsv) as financial_data:
    reader = csv.reader(financial_data)

    # Read the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    #total_months = total_months + 1
    #total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        # Track the total
        #total_months = total_months + 1
        #total_net = total_net + int(row[1])

        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate the greatest decrease
        #if net_change < greatest_decrease[1]:
            #greatest_decrease[0] = row[0]
            #greatest_decrease[1] = net_change

# Calculate the Average Net Change
#net_monthly_avg = sum(net_change_list) / len(net_change_list)

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    #f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
#with open(file_to_output, "w") as txt_file:
    #txt_file.write(output)



