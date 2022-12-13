from tkinter import *
from tkinter.ttk import *

from time import *

ro=Tk()

ro.title('Clock')
# ro.icon('hourglass')
photo=PhotoImage(file="D:\Python\py clock\icoclk.png")
ro.iconphoto(True, photo)
def time():
    strt=strftime("%H:%M:%S %p")
    l.config(text=strt)
    l.after(1000, time)
l=Label(ro,font=("Technology",50),background="black",foreground='lawn green')
l.pack(anchor='center')

time()
ro.mainloop()