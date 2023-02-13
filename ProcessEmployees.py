'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
employee_data=open('employee_data.csv','r')
employee=csv.reader(employee_data, delimiter=',')
next(employee_data)
employee_outfile=open('employee_data','w')
writer=csv.writer(employee_outfile, delimiter= ',')


#create an empty dictionary
employees= {}

#use a loop to iterate through the csv file
for line in employee_data:
    print("Manager Name: "+line[1]+' '+line[2]+' '+"Current Salary: "+line[5])
    

    #check if the employee fits the search criteria
    salary=line[5]
    department=line[3]
    calc_salary= round(float(salary*.10))
    if department in "Marketing":
        print(calc_salary)

    

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout
print(employees)


          
        

        
    
