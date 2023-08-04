from tkinter import *

win = Tk()
win.title("Wscube Tech CALCULATOR")
win.geometry("570x590+100+200")
win.resizable(False, False)
win.configure(bg="#17161b")

number = ""


def click(value):
    global number
    number += value
    result_show.config(text=number)


def clear():
    global number
    number = ""
    result_show.config(text=number)


def equation():
    global number
    result = ""
    if number != "":
        try:
            result = eval(number)
        except ZeroDivisionError:
            result = "ZeroDivisionError"
            number = ""
        except :
            result = "Error"
            number = ""
    result_show.config(text=result)


result_show = Label(win, width=25, height=2, text="", font=("arial", 30))
result_show.pack()

Button(win, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5",
       command=lambda: clear()).place(x=10, y=100)
Button(win, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: click("/")).place(x=150, y=100)
Button(win, text="* ", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: click("*")).place(x=290, y=100)
Button(win, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: click("-")).place(x=430, y=100)

Button(win, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: click("7")).place(x=10, y=200)
Button(win, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: click("8")).place(x=150, y=200)
Button(win, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: click("9")).place(x=290, y=200)
Button(win, text="+", width=5, height=3, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: click("+")).place(x=430, y=200)

Button(win, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: click("4")).place(x=10, y=300)
Button(win, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: click("5")).place(x=150, y=300)
Button(win, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: click("6")).place(x=290, y=300)

Button(win, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: click("1")).place(x=10, y=400)
Button(win, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: click("2")).place(x=150, y=400)
Button(win, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: click("3")).place(x=290, y=400)
Button(win, text="0", width=11, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: click("0")).place(x=10, y=500)

Button(win, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: click(".")).place(x=290, y=500)
Button(win, text="=", width=5, height=3, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#fe9037",
       command=lambda: equation()).place(x=430, y=400)
win.mainloop()
