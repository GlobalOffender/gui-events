import tkinter as tk

ClickWindow = tk.Tk()
ClickWindow.title("Social Credits")
Value = 0
# Functions
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
    Value = Value + 1
    ClickWindow.configure(bg=CountCheck(Value))
    Num.configure(text=Value)

def CountDown():
    global Value
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
# Button 2
Down = tk.Button(ClickWindow)
Down.configure(font=(40), text="-", bg="red", command=CountDown)
Down.pack(pady=10, anchor='center')
# End
ClickWindow.mainloop()

