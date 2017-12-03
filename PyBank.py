import os
import csv
with open("raw_data/budget_data_1.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    count = 0
    TotalRevenue = 0
    TotalChange = 0
    RevChangeTotal = 0
    RevList = []
    RevChangeList = []
    i=1
    for row in csvreader:
        if row[0] != "Date":
            count = count + 1
        if row[1] != "Revenue":
            TotalRevenue = TotalRevenue + int(row[1])
        if row[1] != "Revenue":
            RevList.append(int(row[1]))
        for i in range(1,int(count)):
            RevChange = RevList[i] - RevList[i-1]
            RevChangeList.append(RevChange)
            MaxRev = max(RevChangeList)
            MinRev = min(RevChangeList)
            AvRev = sum(RevChangeList)/len(RevChangeList) 
            
         
            
                   
                       

print("Total Months: " +str(count))
print("TotalRevenue: "+str(TotalRevenue))
print("Greatest Revenue Increase: "+str(MaxRev))
print("Greatest Revenue Decrease: "+str(MinRev))
print("Average Change in Revenue: "+str(AvRev))




        
        
        
