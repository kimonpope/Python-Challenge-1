# -*- coding: utf-8 -*-
# kpope_hw4.py
# Author: Kimon Pope
# Andrew ID: kpope
# Homework 4
import sys

# printHeader()
# Parameters:
# Displays a header for the dictionary program.
# Returns: x - sting 
def printHeader():
    x = ('''    *****************************************
    *                                       *
    *      Kimon\'s Dictionary Program       *
    *                                       *  
    *****************************************''')
    return(x)

# openFile()
# Parameters:
# Opens a data file.
# Returns: x - file variable 
def openFile():
    try:
        name = input('Please enter the name of a file: ')
        x = open(name)
    except FileNotFoundError:
        print('File not found')
        sys.exit()
    else:
        print('File ' + name + ' opened')
        return(x)

# createDictionary()
# Parameters: f - file variable returned from openFIle()
# Creates a dictionary of words and the corresponding definitions.
# Returns: dictionary - dict   
def createDictionary(f): 
    dictionary = {}
    i = 0
    for items in f:
        i+=1
        word = items[:items.find('(')].rstrip().upper()
        definition = items[items.find('('):]
        if not word in dictionary:
            dictionary[word] = [definition]
        else:
            dictionary[word].append(definition)
    return(dictionary)

# displayDefinitions(word, definition)
# Parameters: word - A single word | definition - List of definitons for the corresponding word 
# Displays the word's multiple definitions.
# Returns: 
def displayDefinitions(word, definition):
    words_num = 0
    print(word, ':')
    for x in definition:
        words_num += 1
        print(words_num, ': ' + x)

# createHistogram(dictionary)
# Parameters: dictionary
# Displays the amount of words with 1 definition, 2-5 definitions, 6-10 definitions, and more than 10 definitions.
# Returns:        
def createHistogram(dictionary):
    word_one_def = 0
    word_two_five_def = 0
    word_six_ten_def = 0
    word_greater_ten_def = 0
    max_def = 0
    max_word = 'none'
    for key in dictionary:
        if len(dictionary[key]) == 1:
            word_one_def += 1
        elif len(dictionary[key]) >= 2 and len(dictionary[key]) <= 5:
            word_two_five_def += 1
        elif len(dictionary[key]) >= 6 and len(dictionary[key]) <= 10:
            word_six_ten_def += 1
        elif len(dictionary[key]) > 10:
            word_greater_ten_def += 1
        if len(dictionary[key]) > max_def:
            max_def = len(dictionary[key])
            max_word = key
    print('Definition Counts')
    print('%s%10s%10s%10s' % ('1', '2-5', '6-10', '> 10'))
    print('%d%8d%8d%9d' % (word_one_def, word_two_five_def, word_six_ten_def, word_greater_ten_def))
    print()
    print('%s%s%s%d%s' %('Most definitions: ', max_word, ', ', max_def, ' definitions'))

# main()
# Parameters:
# The main programs calls all of the functions created above.
# Returns:    
def main():
    intro = printHeader()
    print(intro)
    open_book = openFile()
    show_dict = createDictionary(open_book)
    word = input('Enter a word to look up or ALLDONE to quit: ').upper()
    words_not_found = 0
    words_found = 0
    while (word != 'ALLDONE'):
        if word in show_dict:
            displayDefinitions(word, show_dict[word])
            words_found += 1
        else:
            print(word.upper() + ' not found')
            words_not_found += 1
        word = input('Enter a word to look up or ALLDONE to quit: ').upper()
    print()
    print('# words found:', words_found)
    print('# words not Found:', words_not_found)
    print()
    createHistogram(show_dict)
          
if __name__ == '__main__':
    main()     
    