import tkinter as tk

ClickWindow = tk.Tk()
ClickWindow.title("Social Credits")
Value = 0
UpLast = False
DownLast = False
# Functions
def Check(action):
    global UpLast, DownLast
    UpLast = action
    DownLast = not action

def Math(x):
    global Value, UpLast, DownLast
    if UpLast:
        Value = Value * 3
    if DownLast:
        Value = Value / 3
    Num.configure(text=Value)

def BGColor(x):
    ClickWindow.configure(bg="yellow")

def BGColor2(x):
    ClickWindow.configure(bg=CountCheck(Value))

def CountCheck(Value) -> str:
    Kleur = "white"
    if Value == 0:
        Kleur = "grey"
    if Value > 0:
        Kleur = "green"
    if Value < 0:
        Kleur = "red"
    return Kleur
def CountUp():
    global Value
    Check(action = True)
    Value = Value + 1
    ClickWindow.configure(bg=CountCheck(Value))
    Num.configure(text=Value)

def CountDown():
    global Value
    Check(action = False)
    Value = Value - 1
    ClickWindow.configure(bg=CountCheck(Value))
    Num.configure(text=Value)

# Window Settings
ClickWindow.configure(bg="white")
ClickWindow.geometry("300x250")
# Button 1
Up = tk.Button(ClickWindow)
Up.configure(font=(40), text="+", bg="green", command=CountUp)
Up.pack(pady=10, anchor='center')
# Display
Num = tk.Label(ClickWindow, text="???", font=('consolas', 20))
Num.pack(pady=40, anchor='center')
Num.bind('<Enter>', BGColor)
Num.bind('<Leave>', BGColor2)
Num.bind('<Double-Button-1>', Math)
# Button 2
Down = tk.Button(ClickWindow)
Down.configure(font=(40), text="-", bg="red", command=CountDown)
Down.pack(pady=10, anchor='center')
# Binds
ClickWindow.bind("+", lambda event: CountUp())
ClickWindow.bind("-", lambda event: CountDown())
ClickWindow.bind("space", lambda event: Math())
# End
ClickWindow.mainloop()