import matplotlib.pyplot as plt
import numpy as np
import csv
import re

morty = []
yelp = []
sports = []

with open('morty_scores.txt', newline='', encoding="UTF-8") as f:
    reader = csv.reader(f)
    for row in reader:
        re_filter = re.compile(r'\d+(?:\.\d+)?')
        morty.append(int(re_filter.findall(row[1])[0]))

with open('sports_scores.txt', newline='', encoding="UTF-8") as f:
    reader = csv.reader(f)
    for row in reader:
        re_filter = re.compile(r'\d+(?:\.\d+)?')
        sports.append(int(re_filter.findall(row[1])[0]))

with open('yelp_scores.txt', newline='', encoding="UTF-8") as f:
    reader = csv.reader(f)
    for row in reader:
        re_filter = re.compile(r'\d+(?:\.\d+)?')
        yelp.append(int(re_filter.findall(row[1])[0]))

fig1 = plt.figure()
plt.plot(morty)
plt.title('morty.model scores')
plt.ylabel('score')
plt.xlabel('trial number')
fig2 = plt.figure()
plt.plot(yelp)
plt.title('yelp.model scores')
plt.ylabel('score')
plt.xlabel('trial number')
fig3 = plt.figure()
plt.plot(sports)
plt.title('sports.model scores')
plt.ylabel('score')
plt.xlabel('trial number')
plt.show()