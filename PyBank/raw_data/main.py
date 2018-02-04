import os
import csv

#input file number
file_num=2 

#retrieve file
file = os.path.join('budget_data_' + str(file_num)+ '.csv')

#open file
with open(file,'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader,None)
    
#Create Lists
    dates=[]
    revenues=[]
    for row in csv_reader:
        date=row[0]
        revenue=row[1]
        dates.append(date)
        revenues.append(revenue)

#convert revenues to integer
revenue_int= [int(x) for x in revenues]

#create dictionary
data_dict= dict(zip(dates,revenue_int))

#Calculations
total_months= len(dates)
total_rev= sum(revenue_int)
avg_rev= total_rev/total_months
max_rev= max(revenue_int)
max_date= max(data_dict,key=data_dict.get)
min_rev= min(revenue_int)
min_date= min(data_dict,key=data_dict.get)

#Print Final Output
print("```")
print("Financial Analysis\n" + 
"-----------------------------------------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: $" + str(total_rev))
print("Average Revenue Change: $" + str(int(avg_rev)))
print("Greatest Increase in Revenue: " + str(max_date) + " $"+str(max_rev))
print("Greatest Decrease in Revenue: " + str(min_date) + " $" + str(min_rev))
print("-----------------------------------------------------")
print("```")

#print to text
f=open('budget_results.txt','w')
f.write("```\n")
f.write("Financial Analysis\n" + 
"-----------------------------------------------------\n")
f.write("Total Months: " + str(total_months)+"\n")
f.write("Total Revenue: $" + str(total_rev)+"\n")
f.write("Average Revenue Change: $" + str(int(avg_rev))+"\n")
f.write("Greatest Increase in Revenue: " + str(max_date) + " $"+str(max_rev)+"\n")
f.write("Greatest Decrease in Revenue: " + str(min_date) + " $" + str(min_rev)+"\n")
f.write("-----------------------------------------------------\n")
f.write("```")
f.close()