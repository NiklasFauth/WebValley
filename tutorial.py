from Tkinter import *

master = Tk()
master.wm_title("Calculator") #Makes the title that will appear in the top left
e = Entry(master)
e.pack()

e.focus_set()

f = Entry(master)
f.pack()

f.focus_set()

def callback():
    zahl1 = int(e.get())
    zahl2 = int(f.get())
    print zahl1
    print zahl2
    print "Result: ",
    print zahl2 + zahl1
    

b = Button(master, text="add", width=10, command=callback)
b.pack()

mainloop()

e = Entry(master, width=50)
e.pack()

f = Entry(master, width=50)
f.pack()


