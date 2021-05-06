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

    #identify each candidate as a Key and tally votes as Values
    for row in electionData:
        totalVotes += 1
        
        if row[2] in candidateDict:
            candidateDict[row[2]] += 1           
        else:
            candidateDict[row[2]] = 1 

    
#identify key with largest number as the value
#aka identify candidate with most votes
voteList = candidateDict.values()
mostVotes = max(voteList)

for key, value in candidateDict.items():
    if value == mostVotes:
        winner = key #winner of the election!!
        

#assign percentages to each candidate in the dictionary    
print('Election Results\n===================\n(Candidate, Percentage, Votes Received)')


for key in candidateDict:
    percentage = candidateDict[key]/totalVotes
    
    print(key, '---', '{0:.0f}%'.format(percentage*100), '---',  candidateDict[key])
    
print(f'===================\nThe winner is {winner}!!!')


print

    
  
    
 