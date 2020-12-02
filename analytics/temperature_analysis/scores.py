import matplotlib.pyplot as plt
import numpy as np
import csv
import re

yelp128_3_02 = []
yelp128_3_04 = []
yelp128_3_06 = []
yelp128_3_08 = []

with open('yelp128_3_0.2.txt', newline='', encoding="UTF-8") as f:
    reader = csv.reader(f)
    for row in reader:
        re_filter = re.compile(r'\d+(?:\.\d+)?')
        yelp128_3_02.append(int(re_filter.findall(row[1])[0]))

with open('yelp128_3_0.4.txt', newline='', encoding="UTF-8") as f:
    reader = csv.reader(f)
    for row in reader:
        re_filter = re.compile(r'\d+(?:\.\d+)?')
        yelp128_3_04.append(int(re_filter.findall(row[1])[0]))

with open('yelp128_3_0.6.txt', newline='', encoding="UTF-8") as f:
    reader = csv.reader(f)
    for row in reader:
        re_filter = re.compile(r'\d+(?:\.\d+)?')
        yelp128_3_06.append(int(re_filter.findall(row[1])[0]))

with open('yelp128_3_0.8.txt', newline='', encoding="UTF-8") as f:
    reader = csv.reader(f)
    for row in reader:
        re_filter = re.compile(r'\d+(?:\.\d+)?')
        yelp128_3_08.append(int(re_filter.findall(row[1])[0]))

fig1 = plt.figure()
plt.plot(yelp128_3_02)
plt.title('yelp128_3_0.2 scores')
plt.ylabel('score')
plt.xlabel('trial number')

fig2 = plt.figure()
plt.plot(yelp128_3_04)
plt.title('yelp128_3_0.4 scores')
plt.ylabel('score')
plt.xlabel('trial number')

fig3 = plt.figure()
plt.plot(yelp128_3_06)
plt.title('yelp128_3_0.6 scores')
plt.ylabel('score')
plt.xlabel('trial number')

fig4 = plt.figure()
plt.plot(yelp128_3_08)
plt.title('yelp128_3_0.8 scores')
plt.ylabel('score')
plt.xlabel('trial number')

plt.show()