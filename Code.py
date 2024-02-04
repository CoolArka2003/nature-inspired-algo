''' program to store tasks and the time it takes to be completed
in each machine/cloud in a csv file; store the tasks in groups of 4; and
find the least time taken by each task and store the data in csv file and
calculate the makespan and cloud utilisation of the given data. '''

import csv
import random

print('\n')
print("="*80,'\n')

# # taking the value of no. of machines & no. of tasks from the user
# n = int(input('Enter the number of tasks: '))
# m = int(input('Enter the number of machines: '))
m = 32
n = 1024
# setting the machine coloumn names 
vm_names = ['Tasks/VMs']
for i in range(1,m+1):
    mname = 'M' + str(i)
    vm_names.append(mname)

# # making the randomized dataset to be put into the tasktime csv file
# dataset = []            # 2D array to store each row of task and time data
# for j in range(1,n+1):
#     row = []
#     tname = 't' + str(j)
#     row.append(tname)
#     for k in range(1,m+1):
#         row.append(random.random())
#     dataset.append(row)

with open("C://Users//KIIT0001//Desktop//CS//Research//result//u_s_lolo.txt",'r') as file:
    dataset = []
    file.readline()
    for i in range(1,n+1):
        row = []
        tname = 't' + str(i)
        row.append(tname)
        for j in range(1,m+1):
            row.append(float(file.readline().strip()))
        dataset.append(row)

# appending data into a csv file named 'Synthetic_Dataset.csv'
path1 = ".//Cloud_Task_Scheduling//Synthetic_dataset.csv"
with open(path1, 'w', newline='') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(vm_names)
    csvwriter.writerows(dataset)
print("\n--> CSV file 'Synthetic_dataset.csv' created !")

# storing tasks randomly into a csv file named 'grouped.csv'
random.shuffle(dataset)
path2 = ".//Cloud_Task_Scheduling//grouped.csv"
with open(path2, 'w', newline = '') as file2:
    writer = csv.writer(file2)
    writer.writerow(vm_names)
    writer.writerows(dataset)
print("--> Task grouping done & inserted into 'grouped.csv' !")

# storing tasks and the least time they take in a 2D array
data = []
for i in range(len(dataset)):
    least = dataset[i][1]
    leastindex = 1
    mintasklist = []    # array stores individual data of each task which is then appended into the 'data' array 
    mintasklist.append(dataset[i][0])
    for j in range(2,len(dataset[i])):
        if dataset[i][j] < least:
            least = dataset[i][j]
            leastindex = j
    mintasklist.append(vm_names[leastindex])
    mintasklist.append(least)
    data.append(mintasklist)

# appending the data into a csv file name 'least_time_data.csv'
path3 = ".//Cloud_Task_Scheduling//least_time_data.csv"
with open(path3, 'w', newline = '') as file3:
    writer = csv.writer(file3)
    writer.writerow(['tasks','Vm_name','least_time'])
    writer.writerows(data)
print("--> Least time data for each task has been inserted into 'least_time_data.csv' !\n\n")

print("="*80,'\n\n')

#calculation of makespan
makespandict = {}
with open(path3, 'r') as file:
    creader = csv.reader(file)
    next(file)
    for line in creader:
        if line[1] not in makespandict:
            makespandict[line[1]] = float(line[2])
        else:
            makespandict[line[1]] = float(makespandict[line[1]]) + float(line[2])
    
print("Makespan: ",max(makespandict.values()))
 
#calculation of cloud uilisation
i = 1
l_mkspn = []
ind_mkspn = []  # list that will store the value of cloud utilisation
while i <= m:
    with open(path1,'r') as file:
        reader = csv.reader(file)
        next(file)
        sum = 0
        for line in reader:
            sum += float(line[i])
        l_mkspn.append(sum)
        i += 1
#finding max makespan amongst all the machines/clouds
max_mkspn = max(l_mkspn)

#calculating CU(i) ( mkspan of ind. machines / max makspan )
for i in l_mkspn:
    temp_var = i/max_mkspn
    ind_mkspn.append(temp_var)
sum = 0
#calculating U ( Avg. cloud utilisation ), ( U = summation(CU(i)) / no. of machines/clouds )
for i in ind_mkspn:
    sum += i
total_mkspn = sum/m

print("Avg Cloud Utilisation: ",total_mkspn)
print("\n")