# dependencies and modules to import
import csv

# Fils to open
file_to_open = "Resources/budget_data.csv"
# Files to output
file_to_output = "analysis/budget_output.txt"

# Track various revenue parameters:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, 
# then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

# initially start at 0 & will be adding as we loop thru
total_months = 0
# calculate rev change for each month
prev_month_profit_loss = 0
# starts as empty list & appending to each month in data set
month_of_change = []
# list of profit/loss changes corresponding to month of chnage
profit_loss_change_list = []
# then find the average of those changes

# The greatest increase in profits (date and amount) over the entire period
#first string part will have month/date of change; then need to compare
greatest_increase =["", 0]
# The greatest decrease in profits (date and amount) over the entire period
greatest_decrease =["", 9999999999999999999999999999]
total_profit_loss = 0

#read the csv and convert it to a list of dictionaries
with open(file_to_open) as rev_data:
    reader = csv.reader(rev_data)
    header = next(reader)
    #begin loop
    for row in reader:
        
        #track totals
        total_months = total_months + 1
        #cast value as integers bc readers default to strings
        print(row[1])
        total_profit_loss = total_profit_loss + int(row[1])

        #track profit and loss changes
        profit_loss_change = int(row[1]) - prev_month_profit_loss
        prev_month_profit_loss = int(row[1])
        profit_loss_change_list.append(profit_loss_change) 
        # month_of_change = month_of_change + row[0]

        #Calculate greatest increase
        if (profit_loss_change > greatest_increase[1]):
                greatest_increase[0] = row[0]
                greatest_increase[1] = profit_loss_change

        #Calculate greatest decrease
        if (profit_loss_change < greatest_decrease[1]):
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = profit_loss_change

# Calculate the average profit and loss change
profit_loss_average = sum(profit_loss_change_list ) / len(profit_loss_change_list)

#Generate Output Summary.  f formats variables when you concatenate str + int for example
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Profit Loss: {total_profit_loss}\n"
    f"Greatest Increase: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease: {greatest_decrease[0]} (${greatest_decrease[1]})\n"


)

#Print Output
print(output)

#Export results to text file
with open(file_to_output, "w") as txt_file:
        txt_file.write(output)