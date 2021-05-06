import os, csv

inpath = os.path.join("Resources", "election_data.csv")
outpath = 'xxxxx'

'''
create dictionary
key for each candidate
associated values = votes received and % of total votes

for each row
if the candidate is in the list
add one to votes received

if not
add candidate to list
add one to votes received

add one to total votes
next row


no mention of county???

'''


votes = 0
candidate = 0

candidateList = []


with open(inpath, 'r') as CSVin:

    #comma delimited
    electionData = csv.reader(CSVin, delimiter=',')

    #skip header
    next(electionData, None)


    for row in electionData:
        votes += 1
        
        if row[2] in candidateList:
            randomvariable=1            
        else:
            candidateList.append(row[2])
      
    

print(candidateList)



