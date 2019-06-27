"""
Simple Weather

A simple widget for location based weather using Python 3 and Tkinter.
This program is licenced under GPLv3.

"""


import tkinter as tk

HEIGHT = 500
WIDTH = 600
FONT = 40

# Creates a new window.
root_tk = tk.Tk()

# Create a new canvas
canvas_main = tk.Canvas(root_tk, height=HEIGHT, width=WIDTH)
canvas_main.pack()

# Adds an image
bkg_image = tk.PhotoImage()

# Create a new frame
frame_upper = tk.Frame(root_tk, bg='#80c1ff', bd=5)
# Places the frame
frame_upper.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# Creates a text field
entry = tk.Entry(frame_upper, font=40)
entry.place(relwidth=0.65, relheight=1)

# Creates a new button
button_locate = tk.Button(frame_upper, text="Test Button", font=40)
button_locate.place(relx=0.7, relwidth=0.3, relheight=1)

# Create the lower frame
frame_lower = tk.Frame(root_tk, bg='#80c1ff', bd=10)
frame_lower.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# Creates a label
label_main = tk.Label(frame_lower)
label_main.place(relwidth=1, relheight=1)

# Runs the main window in a loop
root_tk.mainloop()

