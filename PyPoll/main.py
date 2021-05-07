import os, csv

inpath = os.path.join("Resources", "election_data.csv")
outpath = 'Election_Results.txt'


#create dictionary: key = candidate, value = votes received 
#for each row if the candidate key is in the dictionary, add one to that key's value'
#if not add candidate key to dictionary with value of 1
#then add one to total votes

#county and voter ID data will not be used



totalVotes = 0
candidate = 0

candidateDict = {}


with open(inpath, 'r') as CSVin:

    
    electionData = csv.reader(CSVin, delimiter=',')
    next(electionData, None)


    #identify each candidate as a Key and tally votes as Values
    for row in electionData:
        totalVotes += 1
        
        if row[2] in candidateDict:
            candidateDict[row[2]] += 1           
        else:
            candidateDict[row[2]] = 1 

    
#identify key with largest number as the value
voteList = candidateDict.values()
mostVotes = max(voteList)


#identify the candidate whose votes match the highest number
for key, value in candidateDict.items():
    if value == mostVotes:
        winner = key #winner of the election!!
        

#assign percentages to each candidate and print to terminal    
print('Election Results\n===================\n(Candidate, Percentage, Votes Received)')

for key in candidateDict:
    percentage = candidateDict[key]/totalVotes
    
    print(key, '----', '{0:.0f}%'.format(percentage*100), '----',  candidateDict[key])
    
print(f'===================\nThe winner is {winner}!!!')



#assign percentages to each candidate and print to file   
with open(outpath, 'w') as outputDoc:
    print('Election Results\n===================\n(Candidate, Percentage, Votes Received)', file=outputDoc)


    for key in candidateDict:
        percentage = candidateDict[key]/totalVotes
    
        print(key, '----', '{0:.0f}%'.format(percentage*100), '----',  candidateDict[key], file=outputDoc)
    
    print(f'===================\nThe winner is {winner}!!!', file=outputDoc)

    
  
    
 