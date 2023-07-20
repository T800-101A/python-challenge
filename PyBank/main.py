import os
import csv


csvpath = os.path.join("C:/Users/arnol/OneDrive/Documents/SMU/GitSMU/python-challenge/PyBank/Resources/budget_data.csv")
csvoutput = os.path.join("C:/Users/arnol/OneDrive/Documents/SMU/GitSMU/python-challenge/PyBank/analysis/resultspybank.txt")


## Defining Variables set in 0 for then asign their values
total_months = 0
net_total_amount = 0
average_change = 0

## Defining lists to save extraction of values from dataset
net_change_list = []
months = []
greatest_increase=["",-1000]
greatest_decrease = ["", 999999]


## opening the file as csvfile from the already assigned csvpath,reading it and eliminating headers 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_headers = next(csvreader)
    
    
##total_months will be adding till last iteration
##this lists will be set with initial positions and values in it to then save data
##to then be use in the formulas to obtain total results

    total_months += 1
    first_row = next(csvreader)
    prev = int(first_row[1])
    net_total_amount += int(first_row[1])
    
##iteration into the data

    for x in csvreader:
        
##extracting data from index 0 (dates) into months variable.        
        months.append(x[0])
        total_months += 1
        
#extracting and adding while iteraring into index 1 (prof/loss) to get totals.
        net_total_amount += int(x[1])
        
##calculating the net changes and saving this result in a new list to then comparate them and save the data
##of greatest increase/decrease saving the biggest and lowest with if conditionals
        
        net_change = int(x[1]) - prev
        net_change_list.append(net_change)
        prev = int(x[1])
        
        
        if net_change > greatest_increase[1]:
            greatest_increase[0]=x[0]
            greatest_increase[1]=net_change
        if net_change < greatest_decrease[1]:
            greatest_decrease[0]=x[0]
            greatest_decrease[1]=net_change


##utilazing now out of the loop the list created (net_change_list) to calculate averages

    average_change = sum(net_change_list) / len(net_change_list)

##then printf to show the results
    
    print("\nFinancial Analysis")
    print(f"-"*20)
    print(f"Total months                 :   {total_months} \n")
    print(f"Total                        : $ {net_total_amount}")
    print(f"Average Change               : ${round(average_change,2)}\n")
    print(f"Greatest Increase in Profit  : {greatest_increase[0]}  {greatest_increase[1]}")
    print(f"Greatest Decrease in Profit  : {greatest_decrease[0]} {greatest_decrease[1]}")
    
    
    with open(csvoutput, "a") as txtfile:
        txtfile.write(
f"""
\n                                Financial Analysis \n
                {"-"*50}

                Total months                 :   {total_months} \n
                Total                        : $ {net_total_amount}\n
                Average Change               : ${round(average_change,2)}\n
                Greatest Increase in Profit  : {greatest_increase[0]}  {greatest_increase[1]}\n
                Greatest Decrease in Profit  : {greatest_decrease[0]} {greatest_decrease[1]}\n
                {"-"*50}


                             """) 
        
        