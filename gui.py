from tkinter import * # Import the tkinter module
from tkinter import ttk # Import the ttk module for themed widgets
from tkinter import messagebox # Import the messagebox module for pop-up messages
from customer import Customer # Import the Customer class from customer.py
from database import view_all_customers # Import the view_all_customers function from database.py

root = Tk() # Create the main window
root.title("Customer Information Form")

# Add a label to the window
label = ttk.Label(root, text="Contact Information")
label.pack(pady=10)

# Add a button to the window
button = ttk.Button(root, text="Submit")
button.pack(pady=10)

root.mainloop() # Start the main event loop