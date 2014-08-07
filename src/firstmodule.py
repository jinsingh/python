'''
Created on 6 Aug 2014

@author: jin
'''
import random
import Tkinter


# labl = Tkinter.label(text = "See me")
# labl.pack()
# labl.mainloop()

m = Tkinter.Tk()
m.mainloop()


in_file = open("text.txt").read().splitlines()
myline = random.choice(in_file)

words = myline.split()
wordslen = len(words)
random.shuffle(words)

for i in words:
    print i

