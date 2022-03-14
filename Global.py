import tkinter as tk
import tkinter.messagebox
import random
import time as time
Xcord = 0
Ycord = 0
Time = 21
Score = 0
Input = 0
def Program():
    # Values
    Keys = ["w", "a", "s", "d", "<Button-1>", "<Double-Button-1>", "<Triple-Button-1>"]
    Keys2 =["W", "A", "S", "D", "Single", "Double", "Triple"]
    # Summon
    root = tk.Tk()
    root.title("Global Elite FPS Trainer")
    root.configure(bg="white")
    root.geometry('400x200')
    # Game Starter
    def Start():
        global Score, Time
        Time = 21
        Score = 0
        root.unbind('<Return>')
        Inputs()
        Count()
    # Input stuff
    def Inputs():
        global Input, Xcord, Ycord
        Xcord = random.randint(50,250)
        Ycord = random.randint(50,150)  
        Input = random.randint(0,6)
        InputDisplay.configure(text=Keys2[Input])
        if Input <= 3:
            root.bind(Keys[Input], ScoreAdd)
        if Input >= 4:
            root.bind(Keys[Input], ScoreAdd2)
        InputDisplay.place(x=Xcord, y=Ycord)
    # Retry???
    def Confirm():
        global Score
        answer = tkinter.messagebox.askquestion(title="Game Over", message="Your score is " + str(Score) + ". Do you want to try again?")
        if answer == "yes":
            root.destroy()
            Program()
        if answer == "no":
            root.destroy()
    # Window Closer
    def Close():
        root.destroy()
    # Score Checker
    def ScoreAdd(x):
        global Score
        Score = Score + 1
        ScoreCounter.configure(text="Score: " + str(Score))
        root.unbind(Keys[Input])
        Inputs()
    def ScoreAdd2(x):
        global Score
        Score = Score + 2
        ScoreCounter.configure(text="Score: " + str(Score))
        root.unbind(Keys[Input])
        Inputs()
    # Time
    def Count():
        global Time
        Time = Time - 1
        TimeText = "Time left: " + str(Time)
        Timer.configure(text=TimeText) 
        if Time == 0:
            Timer.configure(text="GAME ENDED")
            InputDisplay.destroy()
            Confirm()

        else:
            Timer.after(1000, Count)
    # Time Pt. 2
    Timer = tk.Label(root, text="Time left: ???", font=('consolas', 20))
    Timer.pack(pady=10, anchor='center')
    Timer.place(x=0, y=0)
    # Input Display
    InputDisplay = tk.Label(root, text="Press [Enter] to begin", font=('consolas', 20))
    InputDisplay.pack(pady=20, anchor='center')
    InputDisplay.place(x=30, y=100)
    # Score Window
    ScoreCounter = tk.Label(root, text="???", font=('consolas', 20))
    ScoreCounter.pack(pady=20, anchor='center')
    ScoreCounter.place(x=250, y=0)
    root.bind('<Return>', lambda event: Start())
    root.bind('<Escape>', lambda event: Close())
    # End
    root.mainloop()
Program()