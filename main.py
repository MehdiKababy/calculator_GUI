from tkinter import *


def button_1():
    global text
    text += "1"
    label.configure(text=text)


def button_2():
    global text
    text += "2"
    label.configure(text=text)


def button_3():
    global text
    text += "3"
    label.configure(text=text)


def button_4():
    global text
    text += "4"
    label.configure(text=text)


def button_5():
    global text
    text += "5"
    label.configure(text=text)


def button_6():
    global text
    text += "6"
    label.configure(text=text)


def button_7():
    global text
    text += "7"
    label.configure(text=text)


def button_8():
    global text
    text += "8"
    label.configure(text=text)


def button_9():
    global text
    text += "9"
    label.configure(text=text)


def operator_1():
    global text
    if text[-2:-1] != "+" and text != "" and text[-1].isnumeric():
        text += " + "
        label.configure(text=text)


def operator_2():
    global text
    if text[-2:-1] != "-" and text != "" and text[-1].isnumeric():
        text += " - "
        label.configure(text=text)


def operator_3():
    global text
    if text[-2:-1] != "*" and text != "" and text[-1].isnumeric():
        text += " * "
        label.configure(text=text)


def operator_4():
    global text
    if text[-2:-1] != "/" and text != "" and text[-1].isnumeric():
        text += " / "
        label.configure(text=text)


def operator_5():
    global text
    if text[-3:-1] != "**" and text != "" and text[-1].isnumeric():
        text += " ** "
        label.configure(text=text)


def operator_6():
    global text
    if text[-3:-1] != "//" and text != "" and text[-1].isnumeric():
        text += " // "
        label.configure(text=text)


def clear():
    global text
    text = ""
    label.configure(text="")


def result():
    global text
    try:
        text = str(eval(text))
        label.config(text=text)
    except:
        pass


root = Tk()
root.title("calculator")
root.geometry("500x600")
root.minsize(300, 350)
root.maxsize(600, 700)


text = ""


label = Label(
    root,
    text=text,
    bg="seagreen2",
    fg="purple4",
    font=("Vazir", 20, "bold"),
    borderwidth=2,
    relief="solid",
)
label.grid(row=0, column=0, columnspan=4, sticky="nsew")


button_1 = Button(
    root,
    text="1",
    default="active",
    command=button_1,
    font=("Vazir", 15, "bold"),
    bg="pale green",
    activebackground="lightcyan",
)
button_2 = Button(
    root,
    text="2",
    default="active",
    command=button_2,
    font=("Vazir", 15, "bold"),
    bg="pale green",
    activebackground="lightcyan",
)
button_3 = Button(
    root,
    text="3",
    default="active",
    command=button_3,
    font=("Vazir", 15, "bold"),
    bg="pale green",
    activebackground="lightcyan",
)

button_4 = Button(
    root,
    text="4",
    default="active",
    command=button_4,
    font=("Vazir", 15, "bold"),
    bg="pale green",
    activebackground="lightcyan",
)
button_5 = Button(
    root,
    text="5",
    default="active",
    command=button_5,
    font=("Vazir", 15, "bold"),
    bg="pale green",
    activebackground="lightcyan",
)
button_6 = Button(
    root,
    text="6",
    default="active",
    command=button_6,
    font=("Vazir", 15, "bold"),
    bg="pale green",
    activebackground="lightcyan",
)

button_7 = Button(
    root,
    text="7",
    default="active",
    command=button_7,
    font=("Vazir", 15, "bold"),
    bg="pale green",
    activebackground="lightcyan",
)
button_8 = Button(
    root,
    text="8",
    default="active",
    command=button_8,
    font=("Vazir", 15, "bold"),
    bg="pale green",
    activebackground="lightcyan",
)
button_9 = Button(
    root,
    text="9",
    default="active",
    command=button_9,
    font=("Vazir", 15, "bold"),
    bg="pale green",
    activebackground="lightcyan",
)

operator_1 = Button(
    root,
    text="+",
    default="active",
    command=operator_1,
    font=("Vazir", 15, "bold"),
    bg="cyan",
    activebackground="light blue1",
)
operator_2 = Button(
    root,
    text="-",
    default="active",
    command=operator_2,
    font=("Vazir", 15, "bold"),
    bg="cyan",
    activebackground="light blue1",
)
operator_3 = Button(
    root,
    text="*",
    default="active",
    command=operator_3,
    font=("Vazir", 15, "bold"),
    bg="cyan",
    activebackground="light blue1",
)
operator_4 = Button(
    root,
    text="/",
    default="active",
    command=operator_4,
    font=("Vazir", 15, "bold"),
    bg="cyan",
    activebackground="light blue1",
)
operator_5 = Button(
    root,
    text="**",
    default="active",
    command=operator_5,
    font=("Vazir", 15, "bold"),
    bg="cyan",
    activebackground="light blue1",
)
operator_6 = Button(
    root,
    text="//",
    default="active",
    command=operator_6,
    font=("Vazir", 15, "bold"),
    bg="cyan",
    activebackground="light blue1",
)

result = Button(
    root,
    text="=",
    default="active",
    command=result,
    font=("Vazir", 15, "bold"),
    bg="lawn green",
    activebackground="darkseagreen1",
)

clear = Button(
    root,
    text="clear",
    default="active",
    command=clear,
    font=("Vazir", 13, "bold"),
    bg="greenyellow",
    activebackground="darkseagreen1",
)


button_1.grid(row=1, column=0, sticky="nsew")
button_2.grid(row=1, column=1, sticky="nsew")
button_3.grid(row=1, column=2, sticky="nsew")

button_4.grid(row=2, column=0, sticky="nsew")
button_5.grid(row=2, column=1, sticky="nsew")
button_6.grid(row=2, column=2, sticky="nsew")

button_7.grid(row=3, column=0, sticky="nsew")
button_8.grid(row=3, column=1, sticky="nsew")
button_9.grid(row=3, column=2, sticky="nsew")

operator_1.grid(row=1, column=3, sticky="nsew")
operator_2.grid(row=2, column=3, sticky="nsew")
operator_3.grid(row=3, column=3, sticky="nsew")
operator_4.grid(row=4, column=0, sticky="nsew")
operator_5.grid(row=4, column=1, sticky="nsew")
operator_6.grid(row=4, column=2, sticky="nsew")

result.grid(row=4, column=3, sticky="nsew")

clear.grid(row=0, column=3, sticky="se")


root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)


root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)


button_1.config()
button_2.config()
button_3.config()

button_4.config()
button_5.config()
button_6.config()

button_7.config()
button_8.config()
button_9.config()


root.mainloop()
