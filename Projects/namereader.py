import tkinter as tk
# from PIL  import Image, ImageTk
# Top level window
imgsize = (200,200)
canvas_bg = "#000000"


frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')

imgsize = (200,200)
canvas_bg = "#000000"



# logo = Image.open("vignxs.png")
# logo = ImageTk.PhotoImage(logo)
# logo_Label = tk.Label(image=logo)
# logo_Label.image = logo

def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    inp1 = inputtxt2.get(1.0, "end-1c")
    lbl.config(text = f"Your Name is :  {inp.title()} {inp1.title()}  ")


inputtxt = tk.Text(frame,
				height = 2,
				width = 20)
inputtxt.pack()
inputtxt2 = tk.Text(frame,
				height = 2,
				width = 20)
inputtxt2.pack()

# Button Creation
printButton = tk.Button(frame,
						text = "Tap Me !",
						command = printInput)

printButton.pack()

lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()
