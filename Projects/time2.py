import tkinter as tk
from time import strftime

app = tk.Tk()
app.title("Digital Clock")
app.geometry('420x150')
app.resizable(1,1)

text_font = ('Boulder',68,'bold')
background = '#ffffff'
foreground = '#9bb1c8'
border_width = 25

    
label = tk.Label(app,  font=text_font, bg = background, fg = foreground)
label.grid(row = 0, column=1)

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(200, time)

time()
app.mainloop()