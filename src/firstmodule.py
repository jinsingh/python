'''
Created on 6 Aug 2014

@author: jin
'''
#import random
import Tkinter
from Tkinter import Tk, Frame, Button, Listbox, BOTH
from dal import dalfunc
from Crypto.SelfTest import SelfTestError
from gi.overrides.keysyms import End, Left
from Tkconstants import LEFT
#Add to list function
# def fillList():
#     (a1, a2) = dalfunc()
#     ListBox1 = Listbox()
#     count = 1
#     for i in a2:
#         ListBox1.insert(count, i) 
#         count=count+1
#     ListBox1.pack() 

# class DataManager(Listbox):
#         (a1, a2) = dalfunc()     
#         def reloadData(self):
#             count = 1
#             for i in self.a2:
#                 listBox1.insert(count, i) 
#                 count=count+1
                
#Create Window frame
class Example(Frame):
    #listBox1 = Listbox()
     
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        self.parent = parent        
        self.initUI()
     
    def initUI(self):
        self.parent.title("Gurbani Brain Training")
        self.pack(fill=BOTH, expand=1)
        QuitButton = Button(self, text ="Quit", command=self.quit)
        QuitButton.place(x=200, y=200)
        QuitButton.pack()
        
        RandButton = Button(self, text ="Random", command=self.reloadData)
        RandButton.place(x=200, y=200)   
        self.listBox1 = Listbox()
        self.listBox1.pack()
             
        RandButton.pack()
        
    def reloadData(self):
        (wordlens, words, myline) = dalfunc()
        
        for i in range(wordlens):
            i = Button(self, text = words[i])
            i.pack(side=LEFT)
                
            
            #count = 1
            #for i in a2:
            #    self.listBox1.insert(count, i) 
            #    count=count+1
        
        
#     def reloadData(self):
#             (a1, a2, a3) = dalfunc()
#             self.listBox1.delete(0, End)
#             count = 1
#             for i in a2:
#                 self.listBox1.insert(count, i) 
#                 count=count+1

        
    
    
#Set widgets in frame
def main():
    root = Tkinter.Tk()
    root.geometry("750x450+300+300")
    app = Example(root)
    app.mainloop()
    #root.mainloop()
 
if __name__ == '__main__':
    main() 


