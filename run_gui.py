from tkinter import *
from pyswip import *
import tkinter as tk

def helloCallBack(texts):
    p = Prolog()
    p.consult("food.pl")

    if (texts == "what food?"):
        dilicious = Functor("food", 1)
        lao = Functor(texts, 1)
        X = Variable()
        all_food = ""

        r = Query(dilicious(X))
        count = 1
        while r.nextSolution():
            print(count , ". = ", X.value)
            all_food = all_food + str(count) + ". = " + str(X.value) + "\n"
            count += 1
        label = tk.Label(lower_frame, font=('Courier', 18), anchor='nw', justify='left', text = str(all_food)) 
        label.place(relwidth=1, relheight=1)
        r.closeQuery()
    else:
        print(str(texts) + " food....")
        lao = Functor(texts, 1)
        X = Variable()
        q = Query(lao(X))
        count = 1
        all_food = ""
        while q.nextSolution():
            print(count , ". = ", X.value)
            all_food = all_food + str(count) + ". = " + str(X.value) + "\n"
            count += 1
        label = tk.Label(lower_frame, font=('Courier', 18), anchor='nw', justify='left', text = str(texts) + " food....\n" + str(all_food)) 
        label.place(relwidth=1, relheight=1)
root = Tk()

H = 500 
W = 800
canvas = tk.Canvas(root, height=H, width=W)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 18))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='ตกลง', font=40, command = lambda:helloCallBack(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg= '#80c1ff', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 18), anchor='nw', justify='left') 
label.place(relwidth=1, relheight=1)

root.mainloop()