import os

import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')


total_months = 0
profit_losses_amount = 0
net_change = 0
greatest_increaseprofit = [" ", 0]
greatest_decreaselosses = [" ", 9999999999]
net_change_list = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    total_months = 1 
    firstrow = next(csvreader)
    profit_losses = int(firstrow[1])
    previous_net_change = int(firstrow[1])

    for row in csvreader:

        #Adding total months
        total_months = total_months + 1 

        #Adding total net profit/losses
        profit_losses_amount = profit_losses_amount + int(row[1])

        #Net Change
        net_change =  int(row[1]) - previous_net_change

        previous_net_change = int(row[1])

        net_change_list.append(net_change)

        #Calculating greatest increase
        if net_change > greatest_increaseprofit[1]:
            greatest_increaseprofit[1] = net_change
            greatest_increaseprofit[0] = row[0]
        #Calculating greatest losses
        if net_change < greatest_decreaselosses[1]:
            greatest_decreaselosses[1] = net_change 
            greatest_decreaselosses[0] = row[0]
    
    average_change = sum(net_change_list) / len(net_change_list)


output = (f"Financial Analysis\n"
    f"----------------------\n"
    f"Total Months {total_months}\n"
    f"Total Amount of Profit/Losses {profit_losses_amount}\n"
    f"Net Change {average_change}\n"
    f"Total Greatest Increase Profit {greatest_increaseprofit[0]} ({greatest_increaseprofit[1]})\n"
    f"Total Decrease Losses {greatest_decreaselosses[0]} ({greatest_decreaselosses[1]})\n")

print(output)

with open("budget_analysis.txt", "w") as txt_file:
    
    txt_file.write(output)