import matplotlib.pyplot as plt
import numpy as np
import csv
import re

yelp128_1 = []
yelp128_2 = []
yelp128_3 = []
yelp128_4 = []

with open('yelp128_1_scores.txt', newline='', encoding="UTF-8") as f:
    reader = csv.reader(f)
    for row in reader:
        re_filter = re.compile(r'\d+(?:\.\d+)?')
        yelp128_1.append(int(re_filter.findall(row[1])[0]))

with open('yelp128_2_scores.txt', newline='', encoding="UTF-8") as f:
    reader = csv.reader(f)
    for row in reader:
        re_filter = re.compile(r'\d+(?:\.\d+)?')
        yelp128_2.append(int(re_filter.findall(row[1])[0]))

with open('yelp128_3_scores.txt', newline='', encoding="UTF-8") as f:
    reader = csv.reader(f)
    for row in reader:
        re_filter = re.compile(r'\d+(?:\.\d+)?')
        yelp128_3.append(int(re_filter.findall(row[1])[0]))

with open('yelp128_4_scores.txt', newline='', encoding="UTF-8") as f:
    reader = csv.reader(f)
    for row in reader:
        re_filter = re.compile(r'\d+(?:\.\d+)?')
        yelp128_4.append(int(re_filter.findall(row[1])[0]))

fig1 = plt.figure()
plt.plot(yelp128_1)
plt.title('yelp128_1 scores')
plt.ylabel('score')
plt.xlabel('trial number')

fig2 = plt.figure()
plt.plot(yelp128_2)
plt.title('yelp128_2 scores')
plt.ylabel('score')
plt.xlabel('trial number')

fig3 = plt.figure()
plt.plot(yelp128_3)
plt.title('yelp128_3 scores')
plt.ylabel('score')
plt.xlabel('trial number')

fig4 = plt.figure()
plt.plot(yelp128_4)
plt.title('yelp128_4 scores')
plt.ylabel('score')
plt.xlabel('trial number')

plt.show()