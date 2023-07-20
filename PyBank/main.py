import os
import csv


csvpath = os.path.join("budget_data.csv")
csvoutput = os.path.join("resultspybank.txt")

total_months = 0
net_total_amount = 0
average_change = 0


net_change_list = []
months = []
greatest_increase=["",-1000]
greatest_decrease = ["", 999999]



with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_headers = next(csvreader)

    total_months += 1
    first_row = next(csvreader)

    prev = int(first_row[1])


    net_total_amount += int(first_row[1])

    for x in csvreader:
        months.append(x[0])
        total_months += 1
        net_total_amount += int(x[1])
        net_change = int(x[1]) - prev
        net_change_list.append(net_change)
        prev = int(x[1])
        if net_change > greatest_increase[1]:
            greatest_increase[0]=x[0]
            greatest_increase[1]=net_change
        if net_change < greatest_decrease[1]:
            greatest_decrease[0]=x[0]
            greatest_decrease[1]=net_change




    average_change = sum(net_change_list) / len(net_change_list)


    print("Financial Analysis")
    print(f"-"*20)
    print(f"total number of months is : {total_months}")
    print(f"net total amount is : ${net_total_amount}")
    print(f"average change is {str(average_change)}")
    print(f"greatest increase in profit : {greatest_increase[0]} {greatest_increase[1]}")
    print(f"greates decrease in profit : {greatest_decrease[0]} {greatest_decrease[1]}")

    for x in csvreader:

        with open(csvoutput, "a") as txtfile:
            txtfile.write(
                         f"Financial Analysis \n"
                        
                         f"total number of months is : {total_months} \n"
                         f"net total amount is : ${net_total_amount} \n"
                         f"average change is {str(average_change)} \n"
                         f"greatest increase in profit : {greatest_increase[0]} {greatest_increase[1]} \n"
                         f"greates decrease in profit : {greatest_decrease[0]} {greatest_decrease[1]} \n"
                         f"title: {x[0]} \n"
                         f"rating_level: {x[2]} \n"
                         f"user_rating: {x[5]} \n"
                         )


