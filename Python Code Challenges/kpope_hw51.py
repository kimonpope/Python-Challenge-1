# -*- coding: utf-8 -*-
# kpope_hw51.py
# Author: Kimon Pope & Logan Smith
# Andrew ID: kpope & logansmi
# Homework 5 Part 1

import csv
import sys

# readAccounts(f)
# Parameters: f - bank account text file
# Opens a bank account text file and reads the account records. 
# Returns: accounts - list

def readAccounts(f):
    records_skipped = 0
    accounts = []
    file = open(f, 'r')
    for line in file:
        record = line.rstrip()
        record = line.split(' ')
        lastName  = record[0]
        firstname  = record[1]
        typ3_of_account = record[2] 
        record[3] = float(record[3]) 
        balance = record[3]
        if checkBalance(record):
            accounts.append(record)
        else:
            records_skipped += 1
    print('Records skipped:', records_skipped)
    print()
    return(accounts)
    file.close()

# checkBalance(record)
# Parameters: record - list
# Identfies accounts with a negative checking balance. 
# Returns: True or False - boolean
    
def checkBalance(record):
    for items in record:
        if record[2] != 'checking' and  record[3] < 0:
            return(False)
        else:
            return(True)

# writeFile(accounts)
# Parameters: accounts - list
# Cretes a csv file that contains each accounts' data 
# Returns: 
            
def writeFile(accounts):
    with open('newdata.csv', 'w', newline='') as file:
        wr = csv.writer(file)
        wr.writerows(accounts)

# display(accounts)
# Parameters: accounts - list
# Displays the accounts in a formatetted table 
# Returns: 
        
def display(accounts):
    accounts.sort()
    print('%s\t%10s\t%10s\t%10s\t%10s' %('Last', 'First', 'Account', 'Balance', 'Rating'))
    print('------------------------------------------------------------------')
    bad_accounts = 0
    bad_flag = '   '
    for item in accounts:
        if item[3] >= 1000:
            ratings = 'Execellent'
        elif item[3] < 0:
            ratings = 'Bad'
            bad_accounts += 1
        else:
            ratings = 'Good'
        if ratings == 'Bad':
            bad_flag = '<<<'
        else:
            bad_flag = '   '
        print('%s\t%10s\t%10s\t%10.2f\t%10s %s' %(item[0], item[1], item[2], item[3], ratings, bad_flag))
    print()
    print('# Bad Accounts:', bad_accounts)

# main()
# Parameters:
# Runs all the functions created above. 
# Returns: 

def main():
    try:
        x = readAccounts('accounts.txt')
        display(x)
        writeFile(x)
    except FileNotFoundError:
        print('File not found')
        sys.exit()
    
if __name__ == '__main__':
    main()   
    