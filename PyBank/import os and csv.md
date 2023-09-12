import os and csv
    import os
    import csv
set path for file
    csvpath = os.path.join("Resources", "budget_data copy test.csv")
    print(csvpath)
open csv 
with open(csvpath, encoding='UTF-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
read header first 
read through the file
    for row in csv_reader:
The total number of months included in the dataset
    find and store the total number of months
date = 
The net total amount of "Profit/Losses" over the entire period
    subtracting each month from each other and adding the difference 
The changes in "Profit/Losses" over the entire period, and then the average of those changes
    add up all profit/losses and then subtract the sum from amount in period for average
The greatest increase in profits (date and amount) over the entire period
    identify and store the max increase in date and amount
The greatest decrease in profits (date and amount) over the entire period
    indentify and store the max decrease in date and amount

Print - finacial analysis
    -   total months:
    -   total $:
    -   average change $:
    -   greatest increase in profit: date and money 
    -   great decrease in profit: date and money
    == equals a value (look up)
    = is that value (look up meaning)