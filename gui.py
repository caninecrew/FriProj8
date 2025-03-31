from tkinter import * # Import the tkinter module
from tkinter import ttk # Import the ttk module for themed widgets
from customer import Customer
from database import view_all_customers

root = Tk() # Create the main window

button1 = ttk.Button(root, text="Submit")
button1.grid()


root.mainloop() # Start the main event loop