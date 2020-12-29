# Python-Scripts
This is a collection of Python scripts I have developed in college. Please feel free to review or even try these challenges. The source code for each challenge is provided in the "Python Code Challenges" folder. Some challenges require certain text files which are in the "Text Files for Code Challenges" folder. Happy Coding! It is divided into 4 challenges:


## Python Challenge #1 

There are a total of ten problems:

1. Create str variables called product1, product2, and product3; assign them these strings that contain the product's name, product price, and number of items sold of this product: <br/>
<code>'toaster,32.75,2'</code><br/>
<code>'stock pot,56.25,5'</code><br/>
<code>'measuring cup,8.95,10'</code><br/><br/>
Display the strings. Then display product1 in all upper case (note: numerals are not affected), product2 in all
lower case, and the number of characters in product3.

2. Extract the name, price, and items from product1 into three str variables called name1, price1, and items1
using one Python statement (i.e., do not just assign name1 as 'toaster'; think about what str function to use).
Display those three variables on separate lines. Do the same for the others using name2, price2, etc. and display
them also.

3. Re-assign price1 as a float (that is, change its type from str to float), and do the same with price2 and price3.
Re-assign items1as an int and do the same with items2 and items3. Then use a formatted print statement to
display the three prices on one line in an 8-space field with a dollar sign in front and two decimal places, like
this:<br/>
<code>price1 =$ 32.75 price2 = $ 56.25 price3 = $ 8.95</code><br/>
Next, print the three items in the same way, using 5-space fields.

4. Compute the total value of each item sold; store these values in variables named amount1, amount2, and amount3 (for example, amount3 should be 89.50). Display these values in the same way you did problem 3. Then compute the total value sold and display it.

5. Display a table of the data so that it looks like this – the exact number of spaces is not required, but lining up
the columns is required; do NOT simply use spaces or tabs – use the print() formatting codes:<br/>
<code>Product Price Items Value</code><br/>
<code>toaster $ 32.75 2 $ 65.50</code><br/>
and so on for the other items. After those lines, print the total value of all three items sold, formatted and with a
label.

6. Prompt the user for a race distance given in kilometers. Convert that to miles using the formula miles = kilometers/1.609, and display both values with labels, rounded off to two decimal places. Then prompt the user for a race time – first the minutes, then the seconds. Compute their total time in minutes by dividing the seconds by 60 and adding it to the minutes. Display both versions, like this:<br/>
<code>Time: 31 minutes 15 seconds = 31.25 minutes</code><br/>
Then compute and display the user's speed in kilometers per minute and in miles per minute; display both with labels and two decimal places.

7. Using the speed calculated in #6, categorize the user's rate in kilometers per minute according to this scale.
Fast: greater than 0.125 km/min; Medium: more than 0.1 km/min but not Fast; Slow: less than Medium. Display
a message like "Your speed is Fast".

8. Prompt the user for the name of a month, then prompt for a day number (like October and 22). Assign an int
variable for the month: January is 1, February is 2, and so on. Then display the date twice, in the two formats:
October 22, 2019 and 10/22/2019. Don't worry about incorrect entries (like Blurbuary or 100).

9. Assign these values to these variables: x: 2.45, y: 3, z: 10, then write Python code for the following formulas
and display their values (don't worry about rounding):<br/>
(a.) (x minus y) divided by two – as a float<br/>
(b.) (y times z) divided by seven – as an int, no remainder<br/>
(c.) (y times z) divided by seven – but *only* the remainder<br/>
(d.) the average of x, y, and z<br/>
(e). 𝑧((100-x^4)/(sqrt(10y)))<br/><br/>
Assign these values to these variables: s: 'Vampires', t:'ravage', u:'Pittsburgh', write Python code and display the following using str functions:<br/>
(f.) The index of the 'a' in s, in t, and in u<br/>
(g.) s, t, and u concatenated into one string with a space between each, the result named v<br/>
(h.) Three s's (using the * operator)<br/>
(i.) Whether the letter 'z' is in u<br/>
(j.) The sum of the number of characters in s, t, and u

10. Display the values of the following Boolean expressions (using the variables in #9 – no need to re-declare them). (Note: you don't have to write if-statements here; just print the Boolean values by putting the expression in a print( ) statement.)<br/>
(a.) (x>5) and (x<5)<br/>
(b.) (x>5) or (x<5)<br/>
(c.) not (x == 5)<br/>
You have to write Python expressions yourself for these:<br/>
(d.) Does u have at least 5 characters?<br/>
(e.) Are t and u the same strings?<br/>
(f.) Is z greater than zero and does u contain the letter 'P'?<br/>
(g.) Is x at least zero?<br/>
(h.) Does s have at least x characters?<br/>
(i.) Is x divided by y positive?<br/>
(j.) Is the position of 'bur' in u greater than 2 but less than 5?<br/><br/>


## Python Challenge #2

There are a total of seven problems:

1. Create an empty list variable named ***powers***. Use a for loop over integers from 1 to 10 inclusive; insert into
powers the integer raised to the same power (11, 22, 33, etc.). Use a second for loop to display a table containing the integers and their powers side-by-side, like this (make sure that second column is wide enough):<br/>
<code>Integer Power</code><br/>
<code>1 1</code><br/>
<code>2 4</code><br/>
<code>3 27</code><br/>
<code>... and so on ...</code>

2. Create a list named ***words*** containing these strings: log, fog, bog, dog, hog, cog, nog, jog. Print the original
list as a column with the header 'Original'. Print the words in sorted order in a column labeled 'Sorted'. Print the
words (still sorted) in all upper case in a column labeled 'Upper'. Finally, print the words (still sorted) in Title
case in a column labeled 'Title'.

3. Prompt the user for his/her systolic blood pressure and diastolic blood pressure; capture both as int variables.
Next, error check both data item: they should be positive and lower than 400 (somewhat arbitrary, but the
highest ever recorded were 370 and 360); if either is bad, display the error category. Then classify this person's
blood pressure by the rules in the chart below displaying the correct category.<br/>
<table>
    <thead>
        <tr>
            <th colspan="1">Category</th>
            <th colspan="1">Systolic</th>
            <th colspan="1"></th>
            <th colspan="1">Diastolic</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Error Low</td>
            <td>less than 0</td>
            <td>or</td>
            <td>less than 0</td>
        </tr>
       <tr>
            <td>Normal</td>
            <td>less than 120</td>
            <td>and</td>
            <td>less than 80</td>
        </tr>
       <tr>
            <td>Prehypertension</td>
            <td>120 to 139</td>
            <td>or</td>
            <td>80-89</td>
        </tr> 
       <tr>
            <td>Stage 1 Hypertension</td>
            <td>140-159</td>
            <td>or</td>
            <td>90-99</td>
        </tr>
        <tr>
            <td>Stage 2 Hypertension</td>
            <td>160 or more</td>
            <td>or</td>
            <td>100 or more</td>
        </tr>
        <tr>
            <td>Error High</td>
            <td>more than 400</td>
            <td>or</td>
            <td>more than 400</td>
        </tr>
    </tbody>
</table>

4. Download the file 'salesdata.txt' from Canvas (copy it into the directory you're working in). You can look at
the data in a text editor, but don't change it. The data, in CSV format, contains sales records in the form
<item>,<price>,<#sold>. Write code to do the following. Open the file for reading, and read it in one line at a
time. Separate the three pieces of data into variables and change the type of the latter two (float and int).
Compute the amount of money taken in from that sale – for example, if the line says 'coat,65.25,2', the amount
of that sale of two coats is 130.50. Use the loop to find the grand total of the amount of money taken in over all
the sales in the file and to display the sales data as a formatted table. Display the grand total below the table, as
in: <br/><br/>
<code>Item      Price       #sold       Amount</code><br/>
<code>----------------------------------------</code><br/>
<code>coat      $ 65.25         2       $130.50</code><br/>
<code>pants     $ 27.25         1       $ 27.25</code><br/>
<code>... and so on ...</code><br/>
<code>----------------------------------------</code><br/>
<code>Grand total: $717.30</code><br/><br/>
Note that the grand total above is just an example; the actual total will be some other value. The formatting does not have to match the table above exactly – get the data to line up in columns. Close the file at the end.
  
5. Download the file 'weather.txt'. It is a CSV file containing weather data for one day in this format: The first line contains city, date; the rest of the lines contain time, temperature, humidity, wind. For example, the first two lines might be:<br/><br/>
<code>Pittsburgh,3/29/2019</code><br/>
<code>01:27,35,78,4</code><br/><br/>
which says that on March 29 in Pittsburgh, at 01:27 (using the 24-hour clock) the temperature was 35, the relative humidity was 78, and the wind speed was 4 miles per hour.</br>

Write code that will process this data in the following way. Open the file (make sure that the data file and the your script are in the same directory). Read the city and date using readline(), as in:<br/>

<code>city, date = f.readline().split(',')</code><br/>

Display the date using the name of the month, not the numeric value (hint: after splitting the city and date, split the date; declare a list with the month names in it, and use the month number to access the month name). Then, using a for loop, read and display the four values for each weather reading. Close the file. At the end of this table, display the average temperature, the average humidity, and the average wind speed, like this:<br/>

<code>Weather data for Pittsburgh</code>
<code>March 29, 2019</code><br/>

<code>Time Temperature Humidity Wind</code><br/>
<code>-------------------------------</code><br/>
<code>01:27 35 78 4</code><br/>
<code>02:14 36 78 3</code><br/>
<code>... and so on ...</code><br/>
<code>-------------------------------</code><br/>
<code>Average temperature: 42.3</code><br/>
<code>Average humidity: 82.1</code><br/>
<code>Average wind: 3.2</code><br/>

The summary data above is made up – the actual values will differ. Report the averages with one decimal place.
Don't try to code all of this problem at one go – take it in steps. See if you can read the file and print the raw
data; then see if you can compute and display the average temperature; and so on. You'll also need to convert
the str data read from the file for temperature, humidity, and wind to type int.

6. One thing that #5 didn't do, but would likely be of interest, is to display the high and low temperatures. This
problem will compute those twice, the easy way and the hard way. Open the file, read the first line, and display
the header and date as in #5. The use a for loop to read the rest of the file and extract the four date items from
each line. This time, only put the temperature (converted to an int) into a list called ***temperatures***. After the for
loop, close the file. Then use min(temp) and max(temp) to find the minimum and maximum temperatures;
display them with a label. That's the easy way – the built-in functions do the work, and that's the way you
should do it in real programs.
The hard way is to implement the equivalent of min( ) and max( ) on your own. To do this, set ***small*** =
temperatures[0] and ***large*** = temperatures[0]. Then write a for loop that counts over a range from 1 to the
number of values in temperatures; inside the loop, implement this logic: if the temperature at this point in the
list (that is, at temperatures[i] if i is your loop variable) is less than small, then small has to be reset to equal this
temperature. The idea is, you initially set small to the first temperature you see. If you later find a smaller
temperature, then small needs to be reset. Similarly, do the same with large. After the loop, display small and
large; they should be the same values you found by the easy method.

7. Use the list ***data*** below to do the following using list operations as suggested. You may need to look up some
of these functions. Display data after every operation.<br/>

<code>data = [5, -10, 17, 90, -3, 44, 5, 5, -3, 50, 5, 100]</code><br/>

(a.) Change 17 to 27 using index( ) to find 17 first.<br/>
(b.) Remove the last element using pop() and display it.<br/>
(c.) Add new item 20 at the end of ***data*** using append( ).<br/>
(d.) Increment the first and last items by 10 and 20, respectively.<br/>
(e.) Remove duplicate elements from the list (use set( ) to help do this); make sure the result is a list named ***data***.<br/>
(f.) Sort the list using sort( ).<br/>
(g.) Create a new list named ***subdata*** containing elements 2 through 6 inclusive of ***data*** using a slice. Display ***subdata*** instead of ***data***.<br/><br/>
  
  
## Python Challenge #3

There are a total of 5 problems:

1. (a.) Create a set named A containing the characters in the string 'Uncle Bob' using a comprehension; display
A. Create a set named B containing the characters in the string 'Aunt Babs' using a comprehension; display B.
Then compute and display the following sets using set operations and display them:
(b.) everything in both A and B
(c.) only the things common to both A and B
(d.) the things in B without the things in A
(e.) the things in A but not in B plus the things in B but not in A

2. Create two variables student1 and student2 as tuples containing last name, id, and major information:
Smith,4423,MISM and Jones,2215,Philosophy
(a.) Write a loop that iterates over student1's fields and prints them on separate lines; do the same for student2 in
a separate loop.
(b.) Create a list named studentList and store student1 and student2 in it. Then write a for loop that prints each
entry of studentList (as tuples, not as in part a).
(c.) Create a dict called studentDict that uses the student's id as the key and the whole student tuple as the value
(but don't hardcode the id – extract it from each tuple); do this with a for loop over studentList. Then print
studentDict (no loop needed). Then print studentDict[2215].
(d.) Prompt the user to enter a student name (and say to enter 'Done' when finished). If the user enters 'Done' as
the name, print studentDict. If not, prompt the user to enter the id, then prompt for the major. Convert the id to
an int, create a new tuple containing the user's new data, and insert the new student into studentDict.
Hint: the structure of this should be as follows:
prompt for a name # Do this outside the loop in case user enters 'Done'
while name != 'Done': # This is actual Python code
prompt for the id
… and do the other stuff …
prompt for another name # Repeat the prompt for name
print the dictionary
(e.) Prompt the user for a student id number (don’t forget to convert it to int). If there's a student with that id in
the dictionary, display that person's record; if not, display the message 'Error, not found'. (Just once, no loop).

3. (a.) Create a list called names containing these strings: 'Moe', 'Larry', and 'Curly'. Use a for loop to display
its contents on separate lines. The use a for loop to display it on one line (hint: end = ' ').
(b.) Use list comprehensions to create three more lists using names as the source. The first one, caps, should
contain the three names in all capital letters. The second one, lengths, should contain three tuples, where each
tuple is a name and its length, as in ('Moe', 3) and so on. The third one, upDown, should contain three sublists,
where each one contains the name, the name in all capitals, and the name in all lower case, as in ['Moe', 'MOE',
'moe] and so on. Display all three lists (no loops needed).
(c.) Display all four lists in one table as shown. You'll have to use a counter loop. Don't worry about spacing.
0 Moe MOE ('Moe', 3) ['Moe', 'MOE', 'moe']
1 Larry
etc.
(d.) Create a list named allOfIt that contains all of the entries from all four lists, unpacked – that is, it should
concatenate (using +) the entries of names, the entries of caps, list( lengths[0] ), list( lengths[1] ), and so on – all
the individual parts of the tuples and sublists. Print allOfIt (no for loop needed).
(e.) Use a set to remove the duplicates from allOfIt, then turn it back into a list, then display its contents in a
column using a for loop.

4. This problem is practice for doing #5. Download the file 'shorty.txt' to your laptop. Then write code to:
(a.) Open the file 'shorty.txt' and display all the lines. Then close the file. Note that short.txt is *not* a CSV file,
so we won't be splitting the lines in the usual way in the other parts below.
(b.) Repeat part a, but instead display two substrings from each line: the part of the string up to the first left
parenthesis (use the variable name word), and the part of the string from the left parenthesis to the end (use the
variable name definition). For example, here's one line from shorty.txt:
Keel (n.) Fig.: The whole ship.
As you read lines from this file, use find( ) to find the left parenthesis of the part-of-speech (that is, don't use
split() ). Recall that line.find(str) returns you the index numb er of where str is inside line (it returns -1 if not
found, but you'll always find the left parenthesis). Create word as a slice up to that point and use rstrip( ) to
remove any spaces from the end of word. Create definition as a slice using the rest of the line and display the on
separate lines with labels. So, for example, for the line above, you'd display:
Word: Keel
Definition: (n.) Fig.: The whole ship.
Don't forget to close the file.
(c.) Create an empty dict name shortD. Then repeat part a, but instead of displaying word and definition, use
them as <key, value> pairs and add them to short – but first, then use upper( ) before inserting it into short.
Then display shortD (no loop required).

5. In this problem, you'll create a dict named dictionary from the file 'dictionary.txt'. This file is set up like
'shorty.txt' but contains many more words. Use part 4c as the model for this – in fact, there shouldn't be much
different except for the file name. You don't have to display dictionary, but if you do, watch out: it's pretty big.
Note that there are many duplicate words in this file. For simplicity, we'll just use the last definition of the word
– that is, just enter word-definition pairs without even considering duplicates. This will overwrite old entries,
but for this problem, that's okay. For example, for Keel, the definition above is the one of several. The last one
is:
Keel (v. i.) To turn up the keel; to show the bottom.
so that's the one that will display. So in other words, don't worry about duplicates!
find this ( to break it into KEEL and the rest: slice the line based on ('s index
Next, prompt the user for a word. If she/he enters 'ALLDONE', quit (change the user's input to all capitals, so it
works even if the user entered something like 'alldone' or 'AllDone'). Otherwise, look up the capitalized version
of the word (because that's how you stored the keys in the dictionary). If it's not in the dictionary, display
'<word> not found', but if it's in the dictionary, display '<word>: <definition>', where <word> is printed in all
capital letters. Then prompt the user for another word; continue until 'ALLDONE' is entered (hint: use a while
loop with the same general structure as in #2d). Keep counters of the number of words found and the number
not found and display these at the end. For example, it might look like this, using the entry KEEL from above
Enter a word to look up or ALLDONE to quit: keel
KEEL: (n.) Fig.: The whole ship.
Enter a word to look up or ALLDONE to quit: xyz
XYZ not found
Enter a word to look up or ALLDONE to quit: alldone
# words found: 1
# words not found: 1
  
  
## Python Challenge #4

There are a total of 7 problems:

1. Put comments in front of each function with a brief description of the function's parameters and their types,
the function's purpose, and the return value (or n/a, if there isn't one), something like this:
# myfunction(x3b)
# Parameters: x3b - list
# Creates a dictionary from the key,value pairs in x3b.
# Returns: d - dict

2. In this problem, you'll re-do Python Challenge 3, Problem 5: create a dictionary of words and their meanings from a
CSV file. Put your code from that problem into a main( ) program; add the standard two lines to make sure
main() runs:
if __name__ == '__main__':
main()
Make sure your program runs from the command line (in a terminal or cmd window in the directory where both
this code and dictionary.txt reside, type python hw4.py) As you code the other problems below, where you'll be
writing functions, you should test them by calling them from main( ). This won't be graded, but it's good
practice to make sure your functions work correctly. See below for the rest of the story on main( ).
Create a function called printHeader( ) that displays a header like this:
*****************************************
* *
* <your name here>'s Dictionary Program *
* *
*****************************************
  
3. Create a function called openFile( ). Instead of hard-coding the name of the dictionary file, prompt the user
to enter then name of the file. Add a try-except block around the call to open the data file in #1. If an exception
is thrown, display an error message and exit the program. If the file opens correctly, display a message that
says, 'File xxx opened', where xxx is the file name. Return the file variable.

4. Add a function called createDictionary(f), where the parameter f is the file variable returned from openFile(),
which is called in the main program. It should create an empty dict, create the dictionary, then return the dict
variable. As a start, copy the code from homework 3 that created the dictionary and test it on 'shorty.txt' before
trying the bigger dictionary file.
Now make the following changes to the old code. In that version, if there were duplicate word entries, we just
overwrote the old definition with the new one. Here, we'll store all the definitions for each word, and display all
of them when the user asks for the definition of a word.
To handle duplicates, instead of storing a single definition as the value part of the dictionary, this version will
store a list of definitions. Use this logic to create the dictionary: Reading the file and using find( ) to divide the
word from the definition stay the same. If the word is not in the dictionary, add it as a list: dictionary[word] =
[definition]. Note the use of square brackets around definition here – that makes it a list containing one thing,
the definition. If the word is in the dictionary, retrieve its value into a variable – and remember, this is now a
list. Then append the new definition (new because this is a duplicate entry for the word) onto that list. Then set
that list to be the word's value (i.e., you'll overwrite the old list): the syntax is the same as creating the initial
list, because you're assigning a new list.
Modify main( ) – you won't need to declare an empty dict variable. Just set dictionary to the return value of
createDictionary().

5. Create a function called displayDefnintions(word, definition) that handles the logic of displaying the word's
multiple definitions. It does not return anything, because it's just printing the multiple definitions for the word.
The first parameter is a single word; the second parameter is the list of definitions for that word.
Use a for loop to iterate over that list, and print the definitions one at a time, numbered – use a counter variable
for the numbering. Here's an example display (note that the 'Ener a word …' part is not done in this function):
Enter a word to look up, ALLDONE to quit: Keel
Keel :
1: (v. t. & i.) To cool; to skim or stir.
2: (n.) A brewer's cooling vat; a keelfat.
3: (n.) A longitudinal timber, or series of timbers scarfed together, extending from stem
to stern along the bottom of a vessel. It is the principal timber of the vessel, and, by
means of the ribs attached on each side, supports the vessel's frame. In an iron vessel,
a combination of plates supplies the place of the keel of a wooden ship. See Illust. of
Keelson.
4: (n.) Fig.: The whole ship.
5: (n.) A barge or lighter, used on the Type for carrying coal from Newcastle; also, a
barge load of coal, twenty-one tons, four cwt.
6: (n.) The two lowest petals of the corolla of a papilionaceous flower, united and
inclosing the stamens and pistil; a carina. See Carina.
7: (n.) A projecting ridge along the middle of a flat or curved surface.
8: (v. i.) To traverse with a keel; to navigate.
9: (v. i.) To turn up the keel; to show the bottom.
You'll call this function from main( ), inside the loop that does the user prompting. To show all of the
definitions for a word that the user enters, retrieve the word's list of definitions into a list variable (as before,
look up the upper case version of the word, and display an error message if the word is not in the dictionary)
and use those two variables – the word and the list of definitions – as parameters to displayDefinitions( ).

6. The main( ) program, continued. The main program will call printHeader(), then openFile( ), then
createDictionary( ). Next it will do the same while loop as in homework 3: prompt the user for a word; display
an error message if the word is not in the dictionary, or call displayDefinitions( ) if it is in the dictionary;
prompt for the next word; continue until the user enters 'alldone' in some form. You'll also do the counters for
#words found and #words not found and display those results. Finally, call createHistogram( ), described next.

7. Create a function called createHistogram(dictionary) that iterates over the dictionary's keyset (yes, the
keyset) to create a list containing histogram data for the number of definitions that the words have, based on
these four categories: # of words with exactly one definition; # of words with 2-5 definitions; # of words with 6-
10 definitions; and # of words with more than 10 definitions. In addition, keep track of the word that has the
most definitions. Display the results as a table, like this:
Definition Counts
1 2-5 6-10 > 10
86282 22019 2435 894
Most definitions: <some word>, 72 definitions
  
## Python Challenge #5.1

Put comments in front of each function with a brief description of the function's parameters and their types, the
function's purpose, and the return value (or n/a, if there isn't one), something like this:

# myfunction(x3b)
# Parameters: x3b - list
# Creates a dictionary from the key,value pairs in x3b.
# Returns: d - dict

Download the file 'accounts.txt' to use with this problem.

There are a total of 5 problems for the first part of this challenge:

1. Write a function called readAccounts(f). The parameter f is an open bank account text file. It should read
account records, which have the format
lastName firstName type-of-account balance
i.e. it is space delimited (you can look at 'accounts.txt' to see sample records). Create a list containing the data
for one account. Create a list called accounts, initially empty; this will be a list of lists (i.e. it contains the
account records). As you read each line, do the error check described in #2, checkBalance, on the data. If it
passes the test, add it to accounts; if it fails the test, skip it.
If the record is okay, change the fourth field to a float and add it to accounts – that is, each person's data is in a
list, and all these lists are inside accounts. So, accounts will look something like this:
[ ['Barrett', 'Martin', 'checking', -1000.00],
['French', 'Yolanda', 'mortgage', 190000.00],
…
['Adams', 'Martin', 'ira', 42000.00] ]
Display the number of accounts skipped because checkBalance returned False. Then function readAccounts( )
should return the list accounts.

2. If the record's type-of-account is 'checking', any amount is okay, but no negative balances are allowed for the
other account types. Put this logic in a function named checkBalance(record), where record is a list. The
function returns True if the record is okay and False if there's an error.

3. Write a function called writeFile(accounts) whose parameter is the list of accounts. It should create a CSV
file named 'output.txt' by writing each account's data on one line; for example, here's a sample line:
Barnes,Joann,checking,1000.00

4. Write a function called display(accounts) that displays the accounts in a formatted table, as shown below.
The Rating column categorizes the account based on this rule: balances at least 10000 are Excellent; balances
below 0 are Bad; any other balance is Good. Flag any Bad accounts with the symbol '<<<', as shown. After the
table, display the number of Bad accounts.

5. Finally, create a main( ) function that glues this all together: main should open a file with the file name
'accounts.txt' using a try-except block – display an error message and exit the program if the file does not exist;
then call readAccounts() – that function calls the data checking function to ensure good data - then close the
input file. Next, sort the data on the last name, then call displayAccounts() to display the data. Finally call
writeFile(). Add the Python standard code to make your program run:
if __name__ == '__main__':
main()


## Python Challenge #5.2

The following application can be modeled using matrices and vectors – you'll need to use numpy and matrix
multiplication to solve this. (Adapted from Applied Linear Algebra, 2nd Edition, Noble and Daniel) This is
an example of a Markov Chain process.

Three coffee shops – Alice's, Bob's, and Carrie's – operate in a small town. Initially, they split the customers in
town with Alice's taking 20%, Bob's taking 30%, and Carrie's with 50%. Each month, some of the customers
from one shop change to one of the other two. For simplicity, we'll assume that the changes are the same each
month: Alice's retains 80% of its customers and gains 20% of Bob's and 10% of Carrie's. Bob's retains 70% of
its customers and gains 10% of Alice's and 30% of Carrie's. Carrie's retains 60% of its customers and gains 10%
of Alice's and 10% of Bob's.

There are a total of 3 problems:

1. Write a 3x3 matrix named M that models the change in customers. Each row contains the change percentages
described above – row 0 is Alice's, 1 is Bob's, and 2 is Carrie's. Each row's diagonal element is the percentage
that the shop retains. Write a 3x1 vector named x containing the original percentages. Display each of these.
The values of each column of M, and the values of x, should add to 1. Verify this by displaying them with
labels.

2. Multiplication of M times x yields the new split of customers for the next month – that is, a new value of x.
Provide a monthly report of the percentages of customers over two years, partially shown below, by computing
new values of x for each month. What conclusion can you draw about the results?

3. Instead of computing new values of x on each step, the calculation can be done by calculating an ongoing
matrix M on each step. This will keep track of the percentage of customers moving from Bob's and Carrie's to
Alice's in the first row, and so on. Compute and display these values: M, M2, M3, for two years (no need to
compute the value of x – we did that in problem 2). A partial display is shown below. What conclusion can you
draw about the results?
