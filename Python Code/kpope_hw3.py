# -*- coding: utf-8 -*-
# kpope_hw3.py
# Author: Kimon Pope
# Andrew ID: kpope
# Homework 3

# Problem 1
print('*****Problem 1*****')
print()
A = {i for i in 'Uncle Bob'}
print(A)
B = {i for i in 'Aunt Babs'}
print(B)
print(A | B)
print(A & B)
print(B - A)
print((A - B) | (B - A))
print()
print('------------------------------------------------------------------------')
print()
print()

# Problem 2
print('*****Problem 2*****')
print()
student1 = ('Smith', 4423, 'MISM')
student2 = ('Jones', 2215, 'Philosophy')
for i in student1:
    print(i)
for i in student2:
    print(i)
studentList = [student1, student2]
print(studentList)
for i in studentList:
    print(i)
studentDict = {}
i = 0
for items in studentList:
    studentDict[studentList[i][1]] = studentList[i]
    i=+1
print(studentDict)
print(studentDict[2215])
name = input('Enter student name or enter \"Done\" if finished: ')
while name != 'Done':
    studentid = input('Enter studentID: ')
    major = input('Enter student major: ')
    studentid = int(studentid)
    newstudent = (name, studentid, major)
    studentDict[newstudent[1]] = newstudent
    name = input('Enter student name or enter \"Done\" if finished: ')
print(studentDict)
studentid2 = input('Enter studentID: ')
studentid2 = int(studentid2)
if studentid2 in studentDict:
    print(studentDict[studentid2])
else:
    print('Error, not found')
print('------------------------------------------------------------------------')
print()
print()

# Problem 3
print('*****Problem 3*****')
print()
names = ['Moe', 'Larry', 'Curly']
for i in names:
    print(i)
for i in names:
    print(i, end='')
print()
caps = [i.upper() for i in names]
print(caps)
lengths = [(i, len(i)) for i in names]
print(lengths)
upDown = [[i, i.upper(), i.lower()] for i in names]
print(upDown)
i = 0
while i < len(names):
    print(i, names[i], caps[i], lengths[i], upDown[i])
    i += 1
allOfIt = names + caps + list(lengths[0]) + list(lengths[1]) + upDown[0] + upDown[1] + upDown[2]
print(allOfIt)
allOfIt = set(allOfIt)
allOfIt = list(allOfIt)
for i in allOfIt:
    print(i)
print()
print('------------------------------------------------------------------------')
print()
print()

# Problem 4
print('*****Problem 4*****')
print()
f = open('shorty.txt', 'r')
for i in f:
    print(i.rstrip())
f.close()
print()
f = open('shorty.txt', 'r')
i = 0
for items in f:
    i+=1
    word = items[:items.find('(')].rstrip()
    definition = items[items.find('('):]
    print('Word: ' + word)
    print('Definition: ' + definition)
f.close()
print()
f = open('shorty.txt', 'r')
shortD = {}
i = 0
for items in f:
    i+=1
    word = items[:items.find('(')].rstrip()
    definition = items[items.find('('):]
    shortD[word] = definition
print(shortD)
f.close()
print('------------------------------------------------------------------------')
print()
print()

# Problem 5
print('*****Problem 5*****')
print()
f = open('dictionary.txt', 'r')
dictionary = {}
i = 0
for items in f:
    i+=1
    word = items[:items.find('(')].rstrip()
    definition = items[items.find('('):]
    dictionary[word] = definition
f.close()
words_found = 0
words_not_found = 0
print()
word = input('Enter a word to look up or ALLDONE to quit: ')
word = word.upper()
while (word != 'ALLDONE'):
    if word.title() in dictionary:
        print(word.upper() + ': ' + dictionary[word.title()])
        words_found += 1
    else:
        print(word.upper() + ' not found')
        words_not_found += 1
    word = input('Enter a word to look up or ALLDONE to quit: ')
    word = word.upper()
print('# words found:', words_found)
print('# words not Found:', words_not_found)



















