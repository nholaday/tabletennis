#!/usr/bin/env python
#Created by Nic Holaday 2018
#nholaday@gmail.com
"""
Takes in a csv with a column of advanced players and beginner players.
Assigns each advanced player with a random beginner player for random
but even teams.
"""

import csv
import random

cola, colb = [], []
with open('Table_Tennis_Teams.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        cola.append(row[0]) # advanced player
        colb.append(row[1]) # beginner player

random.shuffle(cola)
random.shuffle(colb)

teams = ["{}, {}".format(a,b) for a,b in zip(cola, colb)]

print("")
for item in teams:
    print(item)
print("")


# To create bracket: https://brackets.commoninja.com/app

