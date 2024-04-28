import tkinter as tk
import logging
import sys
import os
import subprocess
import linecache

# logging
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Logging started')

file_path= 'variables.txt'

# actions
def save_text():
    entered_text = entry.get()
    with open(file_path, 'w') as file:
        file.write(entered_text)
    print("Text saved to 'text_file.txt'")

def save_text2():
    entered_text2 = entry.get()
    with open(file_path, 'w') as file:
        file.write(entered_text2)
    print("Text saved to 'text_file.txt'")

root = tk.Tk()

# Create the text boxes
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0)

entry2 = tk.Entry(root, width=30)
entry2.grid(row=2, column=0)

# Create a button to save the text
save_button = tk.Button(root, text="Save Volanta Path", command=save_text)
save_button.grid(row=1, column=0)

save_button2 = tk.Button(root, text="Save MSFS Path", command=save_text2)
save_button2.grid(row=3, column=0)

root.mainloop()