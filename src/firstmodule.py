'''
Created on 6 Aug 2014

@author: jin
'''
import random
import linecache

# in_file = open("text.txt","r")
# text = in_file.read()
# in_file.close()
# words = text.split()

in_file = open("text.txt").read().splitlines()
myline = random.choice(in_file)

words = myline.split()
random.shuffle(words)

for i in words:
    print i
 