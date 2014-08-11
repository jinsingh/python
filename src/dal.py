'''
Created on 8 Aug 2014

@author: jin
'''
import random

def dalfunc():

    in_file = open("text.txt").read().splitlines()
    myline = random.choice(in_file)

    words = myline.split()
    wordslen = len(words)
    random.shuffle(words)

#for i in words:
#   print i
     
    return wordslen, words, myline