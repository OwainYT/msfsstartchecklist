import tkinter as tk
import logging
import sys
import os
import subprocess
import linecache
 # this is all the special features

 # this creates the window
root = tk.Tk()
window_width = 265
window_height = 300
x_position = 960 # Distance from the left edge of the screen
y_position =  540 # Distance from the top edge of the screen
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
root.title("MSFS PreFlight Checklist")
logging.warning('window created')

logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Logging started')
file_path= 'variables.txt'

# Read the specified line from the file
#line_number= 1
#line = linecache.getline(file_path, line_number)

# open the variables file
with open('variables.txt', 'r') as file:
    file_contents = file.read()
logging.info('Opening variables.txt')
logging.info (print(file_contents))

logging.critical('Hello World!')

logging.info('The app should now be available')

# this is for button actions and other shnizzle

# exit hover code    
def on_enter(event):
    button10.config(text="In a while crocodile, enjoy your flight :)")
    button10.config(bg='red')
    logging.info('exit button hover')

def on_leave(event):
    button10.config(text="Exit")

# actions
def command1():
    print("Button 1")
    line_number=1
    line = linecache.getline(file_path, line_number)
    print(linecache.getline(file_path, line_number))
    logging.warning('button pressed')
    subprocess.Popen(linecache.getline(file_path, line_number))

def command2():
    print("Button 2")
    line_number=2
    line = linecache.getline(file_path, line_number)
    print(linecache.getline(file_path, line_number))
    logging.warning('button pressed')
    subprocess.Popen(linecache.getline(file_path, line_number))

def command3():
    print("Button 3")
    line_number=3
    line = linecache.getline(file_path, line_number)
    print(linecache.getline(file_path, line_number))
    logging.warning('button pressed')
    subprocess.Popen(linecache.getline(file_path, line_number))

def command10():
    print("in a while crocodile")
    logging.warning('quit button pressed')
    quit()

# buttons
# button = tk.Button(root, text="", command=)
# button.grid(row=0, column=0)
# logging.warning('button pressed')

button = tk.Button(root, text="Owain's MSFS Before-Start Checklist", command=NotImplemented)
button.grid(row=0, column=5)

button1 = tk.Button(root, text="Start Volanta", command=command1)
button1.grid(row=1, column=5)

button2 = tk.Button(root, text="Start MSFS", command=command2)
button2.grid(row=2, column=5)

button3 = tk.Button(root, text="Start Navigraph Charts", command=command3)
button3.grid(row=3, column=5)

button10 = tk.Button(root, text="Exit", command=command10)
button10.grid(row=4, column=5)
button10.bind("<Enter>", on_enter)
button10.bind("<Leave>", on_leave)

logging.warning('buttons created')

# starts the window 
root.mainloop()

