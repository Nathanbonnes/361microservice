# Nathan Bonnes
# 5/5/22
# This is a test program for the micro-service python program written for my CS361 partner Holly Lucas.

import time

data_file = open('data.txt', 'w')
data_file.write("200 5")
data_file.close()

time.sleep(5)

data_file = open('data.txt', 'w')
data_file.write("300 5")
data_file.close()

time.sleep(5)

data_file = open('data.txt', 'w')
data_file.write("400 5")
data_file.close()

time.sleep(5)

data_file = open('data.txt', 'w')
data_file.write("500 5")
data_file.close()

time.sleep(5)

data_file = open('data.txt', 'w')
data_file.write("600 5")
data_file.close()