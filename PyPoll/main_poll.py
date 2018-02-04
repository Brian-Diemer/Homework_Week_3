import os
import csv
from collections import Counter

#input file number
file_num=2

#retrieve data
poll_CSV= os.path.join('raw_data','election_data_' + str(file_num) + '.csv')

# Set Lists
Voter_ID=[]
County=[]
Candidate=[]

#read file
with open(poll_CSV, 'r') as csvFile:
        
    csvReader = csv.reader(csvFile, delimiter=',')

    #Skip Headers
    next(csvReader, None)

    #write lists
    for row in csvReader:

        Voter_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])

#Calculations
Total_votes=len(Voter_ID)
candidates= set(Candidate)
num_candidates= len(candidates)
candidate_votes= Counter(Candidate)
winner=max(candidate_votes,key=candidate_votes.get)

#Print Final Output
print("```")
print("Election Results")
print("-"*40)
print("Total Votes: ",Total_votes)
print("-"*40)
for name in candidates:
    name_amount=candidate_votes.get(name)
    name_percent=(name_amount/Total_votes)*100
    print(name,": ",round(name_percent,2),"%","(",name_amount,")")
print("-"*40)
print("Winner: ",winner)
print("-"*40)
print("```")

#Print to Text File
f=open('poll_results.txt','w')
f.write("```\n")
f.write("Election Results\n")
f.write("-"*40+"\n")
f.write("Total Votes: "+str(Total_votes)+"\n")
f.write("-"*40+"\n")
for name in candidates:
    name_amount=candidate_votes.get(name)
    name_percent=(name_amount/Total_votes)*100
    f.write(str(name)+": "+str(round(name_percent,2))+"%"+"("+str(name_amount)+")"+"\n")
f.write("-"*40+"\n")
f.write("Winner: "+str(winner)+"\n")
f.write("-"*40+"\n")
f.write("```")
f.close()