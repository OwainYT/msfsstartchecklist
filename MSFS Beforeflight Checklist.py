import tkinter as tk
import logging
import sys
import os

logging.critical('Hello World!')
# debug thing
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Logging started')

logging.info('The app should now be available')

# this is for button actions and other shnizzle

# exit hover code    
def on_enter(event):
    button3.config(text="In a while crocodile, enjoy your flight :)")
    button3.config(bg='red')
    logging.info('button3 hover')

def on_leave(event):
    button3.config(text="Exit")

# actions
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)
def create_ui():
    root = tk.Tk()
def restart_and_close():
    restart_program()
    root.destroy()
def greet():
    print("Hello, Tkinter!")
    logging.warning('button pressed')
def command1():
    print("Button 1")
    logging.warning('button pressed')
def command2():
    print("Button 2")
    logging.warning('button pressed')
def command3():
    print("in a while crocodile")
    logging.warning('quit button pressed')
    quit()

# this creates the window
root = tk.Tk()
root.geometry("400x300")
logging.warning('window created')

# buttons
# button = tk.Button(root, text="", command=)
# button.grid(row=0, column=0)
# logging.warning('button pressed')

button = tk.Button(root, text="Owain's MSFS Before-Start Checklist", command=NotImplemented)
button.grid(row=0, column=5)

button1 = tk.Button(root, text="Greet", command=command1)
button1.grid(row=1, column=0)

button2 = tk.Button(root, text="Greet", command=command2)
button2.grid(row=2, column=0)

button3 = tk.Button(root, text="Exit", command=command3)
button3.grid(row=3, column=5)
button3.bind("<Enter>", on_enter)
button3.bind("<Leave>", on_leave)

restart_button = tk.Button(root, text="Restart", command=restart_and_close)
restart_button.grid(row=4, column=0)

logging.warning('buttons created')

# starts the window 
root.mainloop()

