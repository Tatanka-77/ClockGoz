#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
from tkinter import font
import pytz
from datetime import datetime, timedelta, timezone
import locale

def quit(*args):
        root.destroy()

def show_time():
    txt.set(datetime.now(timezone.utc).strftime("%H:%M:%S"))
    txt2.set((datetime.now(timezone.utc)+timedelta(hours=1)).strftime("%H:%M:%S"))
    txt3.set((datetime.now(timezone.utc)+timedelta(hours=2)).strftime("%H:%M:%S"))
    txt4.set(datetime.now(timezone.utc).strftime("%d/%m/%y "))
    txt5.set ("ZULU" + datetime.now(pytz.timezone('Europe/Rome')).strftime("|%a|").upper())
    txt6.set((datetime.now(timezone.utc)+timedelta(hours=1)).strftime("%d/%m/%y"))
    txt8.set((datetime.now(timezone.utc)+timedelta(hours=2)).strftime("%d/%m/%y"))
    mydate = datetime.now(pytz.timezone('Europe/Rome'))
    dst = bool(mydate.dst())
    if not dst:   
        lbl10.place(relx=1.03, rely=0.525, relheight=0.165, relwidth=0.1, anchor=E)
    else:
        lbl10.place(relx=1.06, rely=0.855, relheight=0.165, relwidth=0.1, anchor=E)
    root.after(1000, show_time)

locale.setlocale(locale.LC_TIME, "it_IT")
root = Tk()
root.attributes("-fullscreen", True)
root.configure(background='black')
root.bind("<Escape>", quit)
root.bind("x", quit)
root.after(1000, show_time)
fnt = font.Font(family='Helvetica', size=186, weight='bold') #todo: dynamic font resize
fnt1 = font.Font(family='Helvetica', size=66, weight='bold') #adjust fontsize manually
fnt2 = font.Font(family='Helvetica', size=58, weight='bold')
fnt3 = font.Font(family='Helvetica', size=120, weight='bold')
fnt4 = font.Font(family='Helvetica', size=45, weight='bold')
txt = StringVar()
txt2 = StringVar()
txt3 = StringVar()
txt4 = StringVar()
txt5 = StringVar()
txt6 = StringVar()
txt7 = StringVar()
txt8 = StringVar()
txt9 = StringVar()
txt10 = StringVar()
txt7.set ("ALFA")
txt9.set ("BRAVO")
txt10.set (u'\u2022')
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="red", background="black")
lbl.place(relx=0.015, rely=0.15, relheight=0.33, relwidth=0.73, anchor=W)
lbl2 = ttk.Label(root, textvariable=txt2, font=fnt, foreground="red", background="black")
lbl2.place(relx=0.015, rely=0.48, relheight=0.33, relwidth=0.73, anchor=W)
lbl3 = ttk.Label(root, textvariable=txt3, font=fnt, foreground="red", background="black")
lbl3.place(relx=0.015, rely=0.81, relheight=0.33, relwidth=0.73, anchor=W)
lbl4 = ttk.Label(root, textvariable=txt4, font=fnt1, foreground="red", background="black")
lbl4.place(relx=1.02, rely=0.075, relheight=0.165, relwidth=0.27, anchor=E)
lbl5 = ttk.Label(root, textvariable=txt5, font=fnt4, foreground="red", background="black")
lbl5.place(relx=1.02, rely=0.235, relheight=0.165, relwidth=0.27, anchor=E)
lbl6 = ttk.Label(root, textvariable=txt6, font=fnt1, foreground="red", background="black")
lbl6.place(relx=1.02, rely=0.400, relheight=0.165, relwidth=0.27, anchor=E)
lbl7 = ttk.Label(root, textvariable=txt7, font=fnt1, foreground="red", background="black")
lbl7.place(relx=1.02, rely=0.565, relheight=0.165, relwidth=0.27, anchor=E)
lbl8 = ttk.Label(root, textvariable=txt8, font=fnt1, foreground="red", background="black")
lbl8.place(relx=1.02, rely=0.730, relheight=0.165, relwidth=0.27, anchor=E)
lbl9 = ttk.Label(root, textvariable=txt9, font=fnt2, foreground="red", background="black")
lbl9.place(relx=1.02, rely=0.895, relheight=0.165, relwidth=0.27, anchor=E)
lbl10 = ttk.Label(root, textvariable=txt10, font=fnt3, foreground="green", background="black")
root.mainloop()


