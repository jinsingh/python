'''
Created on 6 Aug 2014

@author: jin
'''
import random
import Tkinter
from Tkinter import Tk, Frame, Button, Listbox, BOTH
from dal import dalfunc

# #Create Window frame
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        self.parent = parent        
        self.initUI()
     
    def initUI(self):
        self.parent.title("Gurbani Brain Training")
        self.pack(fill=BOTH, expand=1)
        QuitButton = Button(self, text ="Quit", command=self.quit)
        QuitButton.place(x=50, y=50)
        
        (a1, a2) = dalfunc()
        
        #ListBox1 = Listbox()
        
        for i in a2:
            print i
            
        #ListBox1.
        


# #Set widgets in frame
def main():
    root = Tkinter.Tk()
    root.geometry("750x450+300+300")
    app = Example(root)
    app.mainloop()
    #root.mainloop()
 
if __name__ == '__main__':
    main() 



        #for i in a1:
         #   print i
