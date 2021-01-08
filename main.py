#MAIN CORE TO CHOSE THE CODE WE NEED TO RUN AND INSERT THE INPUT DATA 

#Import the Z Open Automation Utilities libraries we need
from zoautil_py import MVSCmd, Datasets
from zoautil_py.types import DDStatement
# Import os, needed to get the environment variables
import os

option = ''                    #CHOICE OF THE ACTION BY THE USER
while option != '1' and option != '2' and option != '3' and option != '4' :
    print('WHAT ACTION DO YO NEED TO EXECUTE?')
    print('1. INVESTMENT PLAN')
    print('2. PLAN OF MAINTANANCE OR REPLACEMENT OF MACHINE')
    print('3. RESOURCE ALLOCATION PLAN')
    print('4. EXIT PROCESS')
    option = input('Enter your choice (1/2/3/4): ')
USERID = os.getenv('USER')

#INSERT OF INPUT DATA AND EXECUTION IN EACH CASE
if option == '1':                                        #IN CASE OF INVESTMENT PLAN 
    output_dataset1 = USERID+".INPUT.DECISION"
    output_dataset2 = USERID+".INPUT.FUND"
    if Datasets.exists(output_dataset1):
        Datasets.delete(output_dataset1)
    if Datasets.exists(output_dataset2):
        Datasets.delete(output_dataset2)
    print('Insert the information asked to move on. ')
    print('Make sure to insert the correct type of data to avoid errors in the future.')
    fund = input('Insert your investment fund (float or integer): ')
    check = False
    while check == False :     # CHECK IF THE INPUT DATA IS CORRECT 
        try:
            float(fund)
            check = True
        except:
            fund = input('An error occurred! Insert your investment fund (float or integer): ')
    Datasets.create(output_dataset2,'SEQ')
    Datasets.write(output_dataset2,fund)
    #print(fund)
    company = input("Insert a company you are thinking of investing in: ")
    cost = input("Insert the cost of investment for this company (float or integer): ")
    check = False
    while check == False :       # CHECK IF THE INPUT DATA IS CORRECT
        try:
            float(cost)
            check = True
        except:
            cost = input('An error occurred! Insert the cost of investment for this company (float or integer): ')
    profit = input("Insert the expected profit of this investment (float or integer): ")
    check = False
    while check == False :       # CHECK IF THE INPUT DATA IS CORRECT
        try:
            float(profit)
            check = True
        except:
            profit = input('An error occurred! Insert the expected profit of this investment (float or integer): ')
    if len(company) <= 11 :
        line = company + ' '*(11-len(company)) + '|' + cost + ' '*(16-len(cost)) + '|' + profit + ' '*(16-len(profit)) + '|'
    else:
        line = company[0:11] + '|' + cost + ' '*(16-len(cost)) + '|' + profit + ' '*(16-len(profit)) + '|'
    insert_value = line
    #We need at least 2 recommendations of companies to move on  
    company = input("Insert another company you are thinking of investing in: ")
    cost = input("Insert the cost of investment for this company (float or integer): ")
    check = False
    while check == False :       # CHECK IF THE INPUT DATA IS CORRECT
        try:
            float(cost)
            check = True
        except:
            cost = input('An error occurred! Insert the cost of investment for this company (float or integer): ')
    profit = input("Insert the expected profit of this investment (float or integer): ")
    check = False
    while check == False :       # CHECK IF THE INPUT DATA IS CORRECT
        try:
            float(profit)
            check = True
        except:
            profit = input('An error occurred! Insert the expected profit of this investment (float or integer): ')
    if len(company) <= 11 :
        line = company + ' '*(11-len(company)) + '|' + cost + ' '*(16-len(cost)) + '|' + profit + ' '*(16-len(profit)) + '|'
    else:
        line = company[0:11] + '|' + cost + ' '*(16-len(cost)) + '|' + profit + ' '*(16-len(profit)) + '|'
    insert_value += '\n' + line
    
    next = input('Do you want to continue by adding another company? (Y/N) ')
    while next == 'Y' or next == 'y' or next == 'YES' or next == 'yes':
        company = input("Insert another company you are thinking of investing in: ")
        cost = input("Insert the cost of investment for this company (float or integer): ")
        check = False
        while check == False :       # CHECK IF THE INPUT DATA IS CORRECT
            try:
                float(cost)
                check = True
            except:
                cost = input('An error occurred! Insert the cost of investment for this company (float or integer): ')
        profit = input("Insert the expected profit of this investment (float or integer): ")
        check = False
        while check == False :       # CHECK IF THE INPUT DATA IS CORRECT
            try:
                float(profit)
                check = True
            except:
                profit = input('An error occurred! Insert the expected profit of this investment (float or integer): ')
        if len(company) <= 11 :
            line = company + ' '*(11-len(company)) + '|' + cost + ' '*(16-len(cost)) + '|' + profit + ' '*(16-len(profit)) + '|'
        else:
                line = company[0:11] + '|' + cost + ' '*(16-len(cost)) + '|' + profit + ' '*(16-len(profit)) + '|'
        insert_value += '\n' + line
        next = input('Do you want to continue by adding another company? (Y/N) ')
    #print(insert_value)    
    Datasets.create(output_dataset1,'SEQ')
    Datasets.write(output_dataset1,insert_value)
    #Execute the algorithm
    os.system('python3 decisions.py')
elif option == '2' :                          # IN CASE OF REPLACEMENT - MAINTENANCE
    output_dataset1 = USERID+".INPUT.EXTRAINF"
    output_dataset2 = USERID+".INPUT.FIXREP"
    if Datasets.exists(output_dataset1):
        Datasets.delete(output_dataset1)
    if Datasets.exists(output_dataset2):
        Datasets.delete(output_dataset2)
    print('Insert the information asked to move on. ')
    print('Make sure to insert the correct type of data to avoid errors in the future.')
    N = input('Insert the number of periods for which you need the plan (integer): ')
    check = False
    while check == False :       # CHECK IF THE INPUT DATA IS CORRECT
        try:
            int(N)
            check = True
        except:
            N = input('An error occurred! Insert the number of periods for which you need the plan (integer): ')
    H = input('Insert the maximum usability time (integer): ')
    check = False
    while check == False :       # CHECK IF THE INPUT DATA IS CORRECT
        try:
            int(H)
            check = True
        except:
            H = input('An error occurred! Insert the maximum usability time (integer): ')
    X = input('Insert the current age of the machine (integer): ')
    check = False
    while check == False :       # CHECK IF THE INPUT DATA IS CORRECT
        try:
            int(X)
            check = True
        except:
            X = input('An error occurred! Insert the current age of the machine (integer): ')
    T = input('Insert the cost of buying a new machine (float or integer): ')
    check = False
    while check == False :       # CHECK IF THE INPUT DATA IS CORRECT
        try:
            float(T)
            check = True
        except:
            T = input('An error occurred! Insert the cost of buying a new machine (float or integer): ')
    line = "  N =" + N + ' '*(7-len(N)) + '|  H =' + H + ' '*(7-len(H)) + '|  X =' + X + ' '*(7-len(X)) + '|  T =' + T + ' '*(7-len(T)) + '|'
    #print(line)
    Datasets.create(output_dataset1,'SEQ')
    Datasets.write(output_dataset1,line)
    insert_value = ''
    for i in range(int(H)+1):
        m = input('Insert the maintenance cost for the ' + str(i) + ' periods old machine (float or integer): ')
        check = False
        while check == False :       # CHECK IF THE INPUT DATA IS CORRECT
            try:
                float(m)
                check = True
            except:
                m = input('An error occurred! Insert the maintenance cost for the ' + str(i) + ' periods old machine (float or integer): ')
        r = input('Insert the resale price for the ' + str(i) + ' periods old machine (float or integer): ')
        check = False
        while check == False :       # CHECK IF THE INPUT DATA IS CORRECT
            try:
                float(r)
                check = True
            except:
                r = input('An error occurred! Insert the resale price for the ' + str(i) + ' periods old machine (float or integer): ')
        if i < int(H):
            insert_value += str(i) + ' '*(11-len(str(i))) + '|' + m + ' '*(16-len(m)) + '|' + r + ' '*(16-len(r)) +'|' +'\n'
        else:
            insert_value += str(i) + ' '*(11-len(str(i))) + '|' + m + ' '*(16-len(m)) + '|' + r + ' '*(16-len(r)) +'|'
    #print(insert_value)
    Datasets.create(output_dataset2,'SEQ')
    Datasets.write(output_dataset2,insert_value)
    #Execute the algorithm
    os.system('python3 fix_rep.py')
elif option == '3' :                         # IN CASE OF RESOURCE ALLOCATION
    output_dataset = USERID+".INPUT.RESOURCE"
    if Datasets.exists(output_dataset):
        Datasets.delete(output_dataset)
    Datasets.create(output_dataset,'SEQ')
    print('Insert the information asked to move on. ')
    print('Make sure to insert the correct type of data to avoid errors in the future.')
    pos = []
    print("WARNING !! Only 9 characters of the position names will apear")
    pos += [input('Insert the 1st position: ')]
    pos += [input('Insert the 2nd position: ')]   # WE NEED AT LEAST 2 POSITIONS TO MAKE THE ALLOCATION PLAN 
    next = input('Do you want to continue by adding a 3rd position? (Y/N) ')
    counter = 3
    while next == 'Y' or next == 'y' or next == 'YES' or next == 'yes':
        if counter == 3:
            pos += [input('Insert the ' + str(counter) + 'rd position: ')]
        else:
            pos += [input('Insert the ' + str(counter) + 'th position: ')]
        counter += 1
        next = input('Do you want to continue by adding a '+ str(counter)+'th position? (Y/N) ')
    insert_value = " RES \ POS |"
    for e in pos:
        if len(e) <= 9:
            insert_value += e + ' '*(9-len(e)) + '|'
        else:
            insert_value += e[0:9] + '|'
    insert_value += '\n' + '0          |' + '0        |'*len(pos)
    m = input('How many resources do you have? (integer) : ')
    check = False
    while check == False :       # CHECK IF THE INPUT DATA IS CORRECT
        try:
            int(m)
            check = True
        except:
            m = input('An error occurred! How many resources do  you have? (integer) : ')
    for i in range(1 , int(m)+1):
        lst = []
        for e in pos:
            if i == 1:
                prod = input('Insert the productivity of 1 resourse in ' + e + ' (float or integer):')
                check = False
                while check == False :       # CHECK IF THE INPUT DATA IS CORRECT
                    try:
                        float(prod)
                        check = True
                    except:
                        prod = input('An error occurred! Insert the productivity of 1 resourse in ' + e + ' (float or integer):')
                lst += [prod]
            else:
                prod = input('Insert the productivity of ' + str(i) + ' resourses in ' + e + ' (float or integer):')
                check = False
                while check == False :       # CHECK IF THE INPUT DATA IS CORRECT
                    try:
                        float(prod)
                        check = True
                    except:
                        prod = input('An error occurred! Insert the productivity of ' + str(i) + ' resourses in ' + e + ' (float or integer):')                
                lst += [prod]
        insert_value += '\n' + str(i) + ' '*(11-len(str(i))) + '|'           # WRITE THE LINE i
        for prod in lst:
            insert_value += prod + ' '*(9-len(prod)) + '|'
    print(insert_value)
    Datasets.write(output_dataset,insert_value)
    #Execute the algorithm
    os.system('python3 resource_alloc.py')
else:
    print('OK BYE !!')