import tkinter as tk
from tkinter import messagebox
import logging
import sys
import os
import subprocess
import linecache

logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

file_path = 'variables.txt'

root = tk.Tk()
window_width = 180
window_height = 200
x_position = 960 # Distance from the left edge of the screen
y_position =  540 # Distance from the top edge of the screen
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# logging
logging.info('Logging started')

# actions
def save_text():
    entered_text = entry.get()
    with open(file_path, 'w') as file:
        file.write('"' + entered_text + '"')
    print("Text saved to 'text_file.txt'")

def save_text2():
    entered_text2 = entry2.get()
    with open(file_path, 'a') as file:
        file.write('\n' + '"' + entered_text2 + '"')
    print("Text saved to 'text_file.txt'")

def save_text3():
    entered_text3 = entry3.get()
    with open(file_path, 'a') as file:
        file.write('\n' + '"' + entered_text3 + '"')
    print("Text saved to 'text_file.txt'")

def check_path():
            messagebox.showinfo("Paths outputted to debug log or terminal")

# Create the text boxes
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0)

entry2 = tk.Entry(root, width=30)
entry2.grid(row=2, column=0)

entry3 = tk.Entry(root, width=30)
entry3.grid(row=4, column=0)


# Create a button to save the text
save_button = tk.Button(root, text="Save Volanta Path", command=save_text)
save_button.grid(row=1, column=0)

save_button2 = tk.Button(root, text="Save MSFS Path", command=save_text2)
save_button2.grid(row=3, column=0)

save_button3 = tk.Button(root, text="Save Navigraph Charts Path", command=save_text3)
save_button3.grid(row=5, column=0)

button4 = tk.Button(root, text= "Check paths", command=check_path)
button4.grid(row=10, column=0)

root.mainloop()