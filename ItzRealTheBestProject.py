from customtkinter import *
win = CTk()
score = 0
def touch():
    global score
    score += 1
    text2.configure(text=f"Score: {score}")
win.title("ItzRealTheBestProject")
win.geometry("400x300")
win.configure(fg_color="blue")
btn = CTkButton(win, text="Touch", command = touch)
text = CTkLabel(win, text="Touch if u love owl!")
text2 = CTkLabel(win, text=f"{score}")

text2.pack()
text.pack()
btn.pack()

win.mainloop()


