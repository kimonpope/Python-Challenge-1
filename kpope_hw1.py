# -*- coding: utf-8 -*-
# kpope_hw1.py
# Author: Kimon Pope
# Homework 1

#Problem 1
print('*****Problem 1*****')
print()
product1 = 'toaster,32.75,2'
product2 = 'stock pot,56.25,5'
product3 = 'measuring cup,8.95,10'
print(product1)
print(product2)
print(product3)
print(product1.upper())
print(product2.lower())
print(len(product3))
print('-----------------------------------------------------------------------------')
print()
print()

#Problem2
print('*****Problem 2*****')
print()
name1 = product1.split(',')[0]; price1= product1.split(',')[1]; items1= product1.split(',')[2];
print(name1)
print(price1)
print(items1)
name2 = product2.split(',')[0]; price2= product2.split(',')[1]; items2= product2.split(',')[2];
print(name2)
print(price2)
print(items2)
name3 = product3.split(',')[0]; price3= product3.split(',')[1]; items3= product3.split(',')[2];
print(name3)
print(price3)
print(items3)
print('-----------------------------------------------------------------------------')
print()
print()

#Problem3
print('*****Problem 3*****')
print()
price1 = float(price1)
price2 = float(price2)
price3 = float(price3)

items1 = int(items1)
items2 = int(items2)
items3 = int(items3)

print('price1 =$ %8s price2 = $ %8s price3 = $ %8s' %(price1, price2, price3))
print('items1 = %5s items2 = %5s items3 = %5s' %(items1, items2, items3))
print('-----------------------------------------------------------------------------')
print()
print()

#Problem4
print('*****Problem 4*****')
print()
amount1 = price1 * items1
amount2 = price2 * items2
amount3 = price3 * items3
total_amount = amount1 + amount2 + amount3

print('Amount1 =$ %8s Amount2 = $ %8s Amount3 = $ %8s Total Amount = $ %8s' %(amount1, amount2, amount3, total_amount))
print('-----------------------------------------------------------------------------')
print()
print()

#Problem5 
print('*****Problem 5*****')
print()
info = [(name1, price1, items1, amount1), (name2, price2, items2, amount2), (name3, price3, items3, amount3)]
print('{0:16} {1:16} {2:16} {3:16}'.format('Product','Price','Items','Value'))
for element in info:
    print('{0:16} ${1:<16} {2:<16} {3:<16}'.format(element[0], element[1], element[2], element[3]))
print(" ")
print('{0:16}'.format('Total Amount'))
print('$%3.2f' %(total_amount))
print('-----------------------------------------------------------------------------')
print()
print()

#Problem6
print('*****Problem 6*****')
print()
km_dist = float(input('Enter a race distance in kilometers: '))
miles_dist = km_dist/1.609
info2 = [(miles_dist), (km_dist)]
print('{0:16} {1:16}'.format('Distance in miles', 'Distance in kilometers'))
print('%14.2f %14.2f' %(miles_dist, km_dist))
minutes = input('What was your race time minutes? Enter minutes here: ')
seconds = input('What was your race time seconds? Enter seconds here: ')
minutes = int(minutes)
seconds = int(seconds)
total_time = minutes + (seconds/60)
print('Time: %d minutes %d seconds = %.2f minutes' %(minutes, seconds, total_time))
km_speed = km_dist / total_time
miles_speed = miles_dist / total_time
print('{0:16} {1:16}'.format('Speed in km/min', 'Speed in miles/min'))
print('%14.2f %14.2f' %(km_speed, miles_speed))
print('-----------------------------------------------------------------------------')
print()
print()

#Problem7
print('*****Problem 7*****')
print()
if(km_speed > 0.125):
    print('Your speed is Fast')
elif(km_speed > 0.1) and (km_speed <= 0.125):
    print('Your speed is Medium')
else:
    print('Your speed is Slow')
print('-----------------------------------------------------------------------------')
print()
print()

#Problem8
print('*****Problem 8*****')
print()
month = str(input('Enter a month. For example, you can type October. Enter month here: '))
day = str(input('Enter a day. For example, you can type 22. Enter day here: '))
print('Date Format 1: ')
print(month, day + ', 2019')
print('Date Format 2: ')
if month == ('January'):
    monthNumber = 1
elif month == 'February':
    monthNumber = 2;
elif month == 'March':
    monthNumber = 3;
elif month == 'April':
    monthNumber = 4;
elif month == 'May':
    monthNumber = 5;
elif month == 'June':
    monthNumber = 6;
elif month == 'July':
    monthNumber = 7;
elif month == 'August':
    monthNumber = 8;
elif month == 'September':
    monthNumber = 9;
elif month == 'October':
    monthNumber = 10;
elif month == 'November':
    monthNumber = 11;
elif month == 'December':
    monthNumber = 12;
monthNumber = str(monthNumber)
print(monthNumber + '/' + day + '/' + '2019')   
print('-----------------------------------------------------------------------------')
print()
print()

#Problem9
print('*****Problem 9*****')
print()
x = 2.45
y = 3
z = 10
print((x - y)/2)
print((y * z)//7)
print((y * z)%7)
print((x + y + z)/3)
print(z*((100 - (x**4))/((10*y)**0.5)))
s = 'Vampires'
t = 'ravage'
u = 'Pittsburgh'
print(s.find('a'))
print(t.find('a'))
print(u.find('a'))
v = s, t, u
print(v)
print('s'*3)
if ('z' in u):
    print('The letter \'z\' is in u')
else:
    print('The letter \'z\' is not in u')
print(len(s) + len(t) + len(u))
print('-----------------------------------------------------------------------------')
print()
print()

#Problem10
print('*****Problem 10*****')
print()
print((x>5) and (x<5))
print((x>5) or (x<5))
print(not (x==5))
print(len(u) >= 5)
print(t == u)
print((z > 0) and ('P' in u))
print(x >= 0)
print(len(s) >= x)
print((x / y) > 0 )
print((u.find('bur') > 2) and (u.find('bur') <5))
    
    