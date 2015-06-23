from Tkinter import *

master = Tk()
master.wm_title("Calculator") #Makes the title that will appear in the top left


Label(master, text="First number:").pack()

e = Entry(master)
e.pack()

Label(master, text="Second number:").pack()

f = Entry(master)
f.pack()

Label(master, text="Result:").pack()

v = StringVar()
Label(master, textvariable=v).pack()

v.set("0")



def callback():
    zahl1 = int(e.get())
    zahl2 = int(f.get())
    print zahl1
    print zahl2
    print "Result: ",
    print zahl2 + zahl1
    v.set(str(zahl2 + zahl1))
    
    

b = Button(master, text="add", width=10, command=callback)
b.pack()

mainloop()

e = Entry(master, width=50)
e.pack()

f = Entry(master, width=50)
f.pack()


