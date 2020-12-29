# -*- coding: utf-8 -*-
# kpope_hw2.py
# Author: Kimon Pope
# Homework 2

# Problem 1
print('*****Problem 1*****')
print()
powers = list()
powers = [i*i for i in range(1,11)]
print('%s \t %s' % ('Integer', 'Power'))
for x in powers:
    print('%d \t\t %5d' % (int(x**0.5), x))
print('------------------------------------------------------------------------')
print()
print()

# Problem 2
print('*****Problem 2*****')
print()
words = ['log', 'fog', 'bog', 'dog', 'hog', 'cog', 'nog', 'jog']
print('Original')
for i in words:
    print(i)
print()
words.sort()
print('Sorted')
for i in words:
    print(i)
print()
print('Upper')
for i in words:
    print(i.upper())
print()
print('Title')
for i in words:
    print(i.title())
print('------------------------------------------------------------------------')
print()
print()

# Problem 3
print('*****Problem 3*****')
print()
blood_pressure = str(input('Please enter your systolic blood pressure and diastolic blood pressure. For example, \'199:239\' Enter here: '))
blood_pressure = blood_pressure.split(':')
systolic = int(blood_pressure[0])
diastolic = int(blood_pressure[1])
if((systolic < 0) or (diastolic < 0)):
    print('Category: Error Low')
elif((systolic > 400) or (diastolic > 400)):
    print('Category: Error High')
elif((systolic < 120) and (diastolic < 80)):
    print('Category: Normal')
elif((systolic >= 120 and systolic <= 139) or (diastolic >= 80 and diastolic <= 89)):
    print('Category: Prehypertension')
elif((systolic >= 140 and systolic <= 159) or (diastolic >= 90 and diastolic <= 99)):
    print('Category: Stage 1 Hypertension')
elif((systolic >= 160) or (diastolic >= 100)):
    print('Category: Stage 2 Hypertension')
print('------------------------------------------------------------------------')
print()
print()

# Problem 4
print('*****Problem 4*****')
print()
f = open('salesdata.txt', 'r')
print ('Item\t\tPrice\t#sold\tAmount')
print('----------------------------------------')
grand_total = 0
for line in f:
    y = line.split(',')
    item = y[0]
    price = y[1]
    price = float(price)
    sold = y[2]
    sold = int(sold)
    amount = price*sold
    grand_total += amount
    print('%8s\t$ %2.2f\t%5d\t%3.2f' % (item, price, sold, amount))
print('----------------------------------------') 
print('%s%3.2f' % ('Grand total: $', grand_total))
f.close()
print('------------------------------------------------------------------------')
print()
print()

# Problem 5
print('*****Problem 5*****')
print()
f = open('weather.txt', 'r')
city, date = f.readline().split(',')
date = date.split('/')
month = date[0]
month = int(month)
day = date[1]
year = date[2]
month_list = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month = month_list[month - 1]
print('Weather data for Pittsburgh')
print('%s %s, %s' % (month, day, year))
print('')
print('Time Temperature Humididty Wind')
print('-------------------------------')
f.close()
f = open('weather.txt', 'r')
f_data = f.readlines()[1:]
sum_temperature = 0
sum_humidity = 0
sum_wind = 0
for line in f_data:
     y = line.split(',')
     time = y[0]
     temperature = y[1]
     temperature = int(temperature)
     humidity = y[2]
     humidity = int(humidity)
     wind = y[3]
     wind = int(wind)
     sum_temperature += temperature
     sum_humidity += humidity
     sum_wind += wind
     print('%s %10d %9d %4d' % (time, temperature, humidity, wind))
f.close()
print('-------------------------------')
avg_temperature = sum_temperature / 14
avg_humidity = sum_humidity / 14
avg_wind = sum_wind / 14
print('%s %2.1f' % ('Average temperature: ', avg_temperature))
print('%s %2.1f' % ('Average humidity: ', avg_humidity))
print('%s %2.1f' % ('Average wind: ', avg_wind))     
print('------------------------------------------------------------------------')
print()
print()

# Problem 6
print('*****Problem 6****')
print()
f = open('weather.txt', 'r')
city, date = f.readline().split(',')
date = date.split('/')
month = date[0]
month = int(month)
day = date[1]
year = date[2]
month_list = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month = month_list[month - 1]
print('Weather data for Pittsburgh')
print('%s %s, %s' % (month, day, year))
f.close()
f = open('weather.txt', 'r')
f_data = f.readlines()[1:]
temperatures = list()
for line in f_data:
     y = line.split(',')  
     temperatures.append(int(y[1]))
f.close()
print('Easy Minimum Temperature')
print(min(temperatures))
print('Easy Maximum Temperature')
print(max(temperatures))
print()
f = open('weather.txt', 'r')
city, date = f.readline().split(',')
date = date.split('/')
month = date[0]
month = int(month)
day = date[1]
year = date[2]
month_list = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month = month_list[month - 1]
print('Weather data for Pittsburgh')
print('%s %s, %s' % (month, day, year))
f.close()
f = open('weather.txt', 'r')
f_data = f.readlines()[1:]
temperatures = list()
for line in f_data:
     y = line.split(',')  
     temperatures.append(int(y[1]))
smallest = temperatures[0]
largest = temperatures[0]
for i in range(1, 14):
    if(smallest > temperatures[i]):
        smallest = temperatures[i]
    if(largest < temperatures[i]):
        largest = temperatures[i]
f.close()
print('Hard Minimum Temperature')
print(smallest)
print('Hard Maximum Temperature')
print(largest)
print('------------------------------------------------------------------------')
print()
print()

# Problem 7
print('*****Problem 7*****')
print()
data = [5, -10, 17, 90, -3, 44, 5, 5, -3, 50, 5, 100]
data[data.index(17)] = 27
print(data)
print(data.pop())
print(data)
data.append(20)
print(data)
data[0] = data[0] + 10
data[11] = data[11] + 20
print(data)
data = set(data)
data = list(data)
print(data)
data.sort()
print(data)
subdata = data[2:7]
print(subdata)















