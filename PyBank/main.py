# modules, os to run on all systems
import os
import csv
# set path for file location
csvpath = os.path.join("Resources", "budget_data copy test.csv")
print(csvpath)
# open csv file and read csv
with open(csvpath, encoding='UTF-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
#read header and skip header line
    csv_header = next(csvfile)
#set list for total months
    Total_month = []
#set variable for total net amount 
    Total = 0
#set variables for Average_change, set current_value to none as it has no value
    current_value = None
    net_change = 0
    number_change = 0
#set variables for max and min profit increases
    max_profit_increase = 0
    min_profit_increase = 0
    profit_month = ""
    profit_month_2 = ""

    
#read rows
    for row in csv_reader:
#append the month to a list
        Total_month.append(row[0])
#collect data from Profit/losses (Column 1)     
        profits_losses = float(row[1])
#find the total net amount by adding profit/losses to the Total 
#round total to a whole number
        Total = round(Total + profits_losses)
#calculate Average_change       
        if current_value is not None:
            difference = profits_losses - current_value
            net_change = net_change + difference
            number_change = number_change + 1
#set max and min profit by using "difference" and rounding the value.
#connect the max and min "difference" value to a month.
            if difference > max_profit_increase:
                max_profit_increase = round(difference)
                profit_month = row[0]
            elif difference < min_profit_increase:
                min_profit_increase = round(difference)
                profit_month_2 = row[0]
        current_value = profits_losses
        
#calculate total amount of months after reading all rows
Total_month = len(Total_month)

#calculate Average_Change and round too 2 decimal places
Average_Change = round(net_change / number_change,2)

#change final values into dollar format, this was to remove the space between "$" and variables
Total_dollar = '${:}'.format(Total)
Average_Change_dollar = '${:}'.format(Average_Change)
Largest_Profit_increase = '${:}'.format(max_profit_increase)
Smallest_Profit_increas = '${:}'.format(min_profit_increase)
#print out the collected results in terminal
print('Financial Analysis')
print('-----------------------------')
print('Total Months:', Total_month)
print('Total:', Total_dollar)
print('Average Change:',Average_Change_dollar)
#need to format in brackets around the value amount
print('Greatest Increase In Profits:', profit_month,("("+Largest_Profit_increase+")"))
print('Greatest Decrease In Profits:', profit_month_2,("("+Smallest_Profit_increas+")"))
#output results as a text file to analysis folder
output_path = os.path.join("Analysis","Finacial Analysis.text")
with open(output_path, 'w') as f:
    print('Financial Analysis', file=f)
    print('-----------------------------', file=f)
    print('Total Months:', Total_month, file=f)
    print('Total:', Total_dollar, file=f)
    print('Average Change:',Average_Change_dollar, file=f)
    print('Greatest Increase In Profits:', profit_month,("("+Largest_Profit_increase+")"), file=f)
    print('Greatest Decrease In Profits:', profit_month_2,("("+Smallest_Profit_increas+")"), file=f)