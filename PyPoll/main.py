import os, csv

inpath = os.path.join("Resources", "election_data.csv")
outpath = 'xxxxx'

'''
create dictionary
key = candidate
value = votes received 

for each row
if the candidate key is in the dictionary
add one to that item

if not
add candidate key to dictionary
add one to that item

add one to total votes
next row


no mention of county???

'''


totalVotes = 0
candidate = 0

candidateDict = {}

with open(inpath, 'r') as CSVin:

    #comma delimited
    electionData = csv.reader(CSVin, delimiter=',')

    #skip header
    next(electionData, None)


    for row in electionData:
        totalVotes += 1
        
        if row[2] in candidateDict:
            candidateDict[row[2]] += 1           
        else:
            candidateDict[row[2]] = 1 
      
    

print(candidateDict)
print(totalVotes)



