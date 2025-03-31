from tkinter import * # Import the tkinter module
from tkinter import ttk # Import the ttk module for themed widgets
from tkinter import messagebox # Import the messagebox module for pop-up messages
from customer import Customer # Import the Customer class from customer.py
from database import view_all_customers # Import the view_all_customers function from database.py

root = Tk() # Create the main window
root.title("Customer Information Form")
root.geometry("400x500") # Set the window size

# Create a main frame with padding
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill=BOTH, expand=True)

# Add a title label to the window
title_label = ttk.Label(root, text="Contact Information", font=("Arial", 12, "bold"))
title_label.pack(pady=(0, 15))

# Create fields for customer information
# NAME
name_frame = ttk.Frame(main_frame)
name_frame.pack(fill=X, pady=5)
name_label = ttk.Label(name_frame, text="Name:", width=15, anchor=W)
name_label.pack(side=LEFT)
name_entry = ttk.Entry(name_frame)
name_entry.pack(side=LEFT, fill=X, expand=True)

# Add a button to the window
button = ttk.Button(root, text="Submit")
button.pack(pady=10)

root.mainloop() # Start the main event loop