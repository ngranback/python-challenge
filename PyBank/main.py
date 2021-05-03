import os
import csv

budgetCSVpath = "Resources/budget_data.csv"


months = 0
totalIncrease = 0
totalDecrease = 0
countIncrease = 0
countDecrease = 0
biggestIncrease = 0
biggestDecrease = 0



with open(budgetCSVpath, 'r') as budgetCSV:

    #comma delimited
    budgetCSVreader = csv.reader(budgetCSV, delimiter=',')

    #skip header
    next(budgetCSVreader, None)


    for row in budgetCSVreader:
      
        # loss assessment
        if(int(row[1]) < 0): 
            countDecrease += 1
            totalDecrease = totalDecrease + int(row[1])
            
            # keep track of the biggest month loss
            if int(row[1]) < biggestDecrease:
                biggestDecrease = int(row[1])
                biggestDecreaseMonth = row[0]
            
        # profit assessment
        else: 
            countIncrease += 1
            totalIncrease = totalIncrease + int(row[1])

            # keep track of the biggest month profit
            if int(row[1]) > biggestIncrease:
                biggestIncrease = int(row[1])
                biggestIncreaseMonth = row[0]

        months += 1

netProfit = totalIncrease + totalDecrease
avgChange = int(netProfit / months)


#print the financial report
print(f"""
Financial analysis covering {months} months:
________________________________________
Net profit was ${netProfit:,d}
Average monthly change was ${avgChange:,d}
Most profitable month was {biggestIncreaseMonth} with ${biggestIncrease:,d}
Least profitable month was {biggestDecreaseMonth} with ${biggestDecrease:,d}

This analysis has also been exported to a text file.""")


with open("FinancialAnalysis.txt", 'w') as outputDoc:
    print(f"""
    Financial analysis covering {months} months:
    ________________________________________
    Net profit was ${netProfit:,d}
    Average monthly change was ${avgChange:,d}
    Most profitable month was {biggestIncreaseMonth} with ${biggestIncrease:,d}
    Least profitable month was {biggestDecreaseMonth} with ${biggestDecrease:,d}
    """, file=outputDoc)


    