from tkinter import *
import webbrowser

def open_page():
    webbrowser.open("https://www.gocomics.com/foxtrot/2003/10/03")

#Creates Tk window
master = Tk()
master.title("Foxtrot Button!")
master.geometry("500x250")

#Centers Tk window 
h = master.winfo_reqheight()
w = master.winfo_reqwidth()
hs = master.winfo_screenheight()
ws = master.winfo_screenwidth()
y = (hs/2) - (h/2)
x = (ws/2) - (w/2)
master.geometry('+%d+%d' % (x, y))

#Creates a Frame which can expand according to the size of the window
pane = Frame(master)
pane.pack(fill = BOTH, expand = True)
 
#Button 1
b1 = Button(pane, text = "Click me for Foxtrot!", background = "#33D5FF", fg = "black", command = open_page)
b1.pack(side = TOP, expand = True, fill = BOTH)

#Button 2
b2 = Button(pane, text = "QUIT", background = "#EE5D5D", fg = "white", command = quit)
b2.pack(side = TOP, expand = True, fill = BOTH)

#Prints message upon activation
print("Thanks for using the Foxtrot button! I love you!")

#Execute Tkinter
master.mainloop() 
