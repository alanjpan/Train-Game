# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 16:55:49 2018

@author: Alan Jerry Pan, CPA, CSc student
@affiliation: Shanghai Jiaotong University

program framework for description and simulation of train operation--was written entirely on a train!

Suggested citation as computer software for reference:
Pan, Alan J. (2018). Train Simulator [Computer software]. Github repository <https://github.com/alanjpan/Train-Simulator>

Note this software's license is GNU GPLv3.
"""

import random
secure_random = random.SystemRandom()

train = ['[M]', '[o]', '[o]']
capacity = {'[M]': 0, '[o]': 50, '[O]': 100}
cost = [10000, 30000]
basegasfee = 5000
schedule = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
traffic = [5, 5, 5, 10, 20, 25, 25, 25, 20, 20, 25, 30, 30, 25, 20, 15, 20, 30, 40, 50, 40, 25, 10, 5]
ticketprice = 400
active = True
roll = [2, 3, 4, 5, 6, 7, 8]

passengers = 0
cash = 5000
turn = 1
hours = 0
time = secure_random.choice(schedule)
tax = 10
while active:
    print('CHOO CHOO CHOO')
    print('turns elapsed: ' + str(turn))
    drawtrain = ''
    for i in range(len(train)-1, -1, -1):
        drawtrain += str(train[i])
    print(drawtrain)
    print('it is ' + str(time) + ':00. there are ' + str(passengers) + ' on board')
    passengers += traffic[time]
    print(str(traffic[time]) + ' passengers board your train')

    print(str(cash) + ' in earnings. ' + 'do you depart? (type buy to buy a caboose for 25000)')
    response = input()
    advance = 0
    passengerflag = True
    revenue = 0
    try:
        if response.startswith('y'):
            passengerflag = False
            revenue += passengers * ticketprice
            cash += revenue
            print(str(revenue) + ' gained')
            advance = int(secure_random.choice(roll))
            time += advance

            print(str(advance) + ' hours passed on your journey')

            paygas = advance * basegasfee + passengers*5 + len(train)*2500
            print('you arrive at your destination, pay gas of ' + str(paygas))
            cash = int(cash - paygas)
            passengers = 0
            hours += advance

        elif response.startswith('n'):
            print('time advances one hour. pay stationary tax of $250')
            time += 1
            cash -= 250
            hours += 1

        elif response.startswith('b'):
            if cash > 25000:
                print('you buy an additional caboose for your train')
                train.append('[o]')
                cash -= 25000
            else:
                print('you cannot afford it. wasted $500 on reception')
                cash -= 500
            hours += 1
        else:
            print('a flock of birds fly overhead. pay stationary tax of $250')
            time += 1
            cash -= 250
            hours += 1
    except:
        print('you blow some steam. pay stationary tax of $250')
        time += 1
        cash -= 250
        hours += 1

    passengercapacity = 0
    if passengerflag == True:
        for i in train:
            passengercapacity += capacity[i]
        leavetrain = 0
        if passengers > passengercapacity:
            leavetrain = passengers - passengercapacity
            passengers = passengers - leavetrain
            print(str(leavetrain) + ' passengers could not board your train due to overcapacity')

    if time >= 24:
        time = time - 24
    print('$$$$$$$$$$$$$$$$$')
    print('total earnings: ' + str(cash))
    print()
    
    if cash <= 0:
        active = False

    if (turn % 10) == 0:
        print('pay national tax of ' + str(tax) + '%')
        taxed = int(cash * tax / 100)
        print('taxed ' + str(taxed) + ' dollars')
        cash -= taxed
        tax += 10

    turn += 1

print('$$$$$$$$GAME OVER$$$$$$$$')
print('turns in business: ' + str(turn))
print('game hours lapsed: ' + str(hours))
drawtrain = ''
for i in range(len(train)-1, -1, -1):
    drawtrain += str(train[i])
print('nice train: ' + drawtrain)