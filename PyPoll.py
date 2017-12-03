import os
import csv
with open("raw_data/election_data_1.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


    count = 0
    Vestal = 0
    Torres = 0
    Seth = 0
    Cordin = 0
    for row in csvreader:
        count = count + 1
        
        if row[2] == "Vestal":
            Vestal = Vestal + 1
        if row[2] == "Torres":
            Torres = Torres + 1
        if row[2] == "Seth":
            Seth = Seth + 1
        if row[2] == "Cordin":
            Cordin = Cordin +1
        

        
WinningNumber = max(Vestal,Torres,Seth,Cordin)
if WinningNumber == Vestal:
    WinningCandidate = "Vestal"
if WinningNumber == Torres:
    WinningCandidate = "Torres"
if WinningNumber == Seth:
    WinningCandidate = "Seth"
if WinningNumber == Cordin:
    WinningCandidate = "Cordin"




print("Number of Votes: "+str(count))
print("Vestal: "+str(Vestal)+" (" + str((Vestal/count)*100)+" %)")
print("Torres: "+str(Torres)+" (" + str((Torres/count)*100)+" %)")
print("Seth: "+str(Seth)+" (" + str((Seth/count)*100)+" %)")
print("Cordin: "+str(Cordin)+" (" + str((Cordin/count)*100)+" %)")
print("Winner: "+WinningCandidate)

# id county candidte
#Vestal Torres Seth Cordin

        
        
