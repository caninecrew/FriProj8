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
# Name field
name_frame = ttk.Frame(main_frame)
name_frame.pack(fill=X, pady=5)
name_label = ttk.Label(name_frame, text="Name:", width=15, anchor=W)
name_label.pack(side=LEFT)
name_entry = ttk.Entry(name_frame)
name_entry.pack(side=LEFT, fill=X, expand=True)

# Birthday field
birthday_frame = ttk.Frame(main_frame)
birthday_frame.pack(fill=X, pady=5)
birthday_label = ttk.Label(birthday_frame, text="Birthday:", width=15, anchor=W)
birthday_label.pack(side=LEFT)
birthday_entry = ttk.Entry(birthday_frame)
birthday_entry.pack(side=LEFT, fill=X, expand=TRUE)

# Email
email_frame = ttk.Frame(main_frame)
email_frame.pack(fill=X, pady=5)
email_label = ttk.Label(email_frame, text="Email:", width=15, anchor=W)
email_label.pack(side=LEFT)
email_entry = ttk.Entry(email_frame)
email_entry.pack(side=LEFT, fill=X, expand=TRUE)

# Phone
phone_frame = ttk.Frame(main_frame)
phone_frame.pack(fill=X, pady=5)
phone_label = ttk.Label(phone_frame, text="Phone:", width=15, anchor=W)
phone_label.pack(side=LEFT)
phone_entry = ttk.Entry(phone_frame)
phone_entry.pack(side=LEFT, fill=X, expand=TRUE)

# Address
address_frame = ttk.Frame(main_frame)
address_frame.pack(fill=X, pady=5)
address_label = ttk.Label(address_frame, text="Address:", width=15, anchor=W)
address_label.pack(side=LEFT)
address_entry = ttk.Entry(address_frame)
address_entry.pack(side=LEFT, fill=X, expand=TRUE)

# City
city_frame = ttk.Frame(main_frame)
city_frame.pack(fill=X, pady=5)
city_label = ttk.Label(city_frame, text="City:", width=15, anchor=W)
city_label.pack(side=LEFT)
city_entry = ttk.Entry(city_frame)
city_entry.pack(side=LEFT, fill=X, expand=TRUE)

# State
state_frame = ttk.Frame(main_frame)
state_frame.pack(fill=X, pady=5)
state_label = ttk.Label(state_frame, text="State:", width=15, anchor=W)
state_label.pack(side=LEFT)
state_entry = ttk.Entry(state_frame)
state_entry.pack(side=LEFT, fill=X, expand=TRUE)

# ZIP Code
zip_frame = ttk.Frame(main_frame)
zip_frame.pack(fill=X, pady=5)
zip_label = ttk.Label(zip_frame, text="ZIP Code:", width=15, anchor=W)
zip_label.pack(side=LEFT)
zip_entry = ttk.Entry(zip_frame)
zip_entry.pack(side=LEFT, fill=X, expand=TRUE)

# Country
country_frame = ttk.Frame(main_frame)
country_frame.pack(fill=X, pady=5)
country_label = ttk.Label(country_frame, text="Country:", width=15, anchor=W)
country_label.pack(side=LEFT)
country_entry = ttk.Entry(country_frame)
country_entry.pack(side=LEFT, fill=X, expand=TRUE)

# Preferred Contact (dropdown)
contact_frame = ttk.Frame(main_frame)
contact_frame.pack(fill=X, pady=5)
contact_label = ttk.Label(contact_frame, text="Preferred Contact:", width=15, anchor=W)
contact_label.pack(side=LEFT)
contact_combobox = ttk.Combobox(contact_frame, values=["Email", "Phone", "Mail"])
contact_combobox.current(0)  # Set default to first option
contact_combobox.pack(side=LEFT, fill=X, expand=TRUE)

# Add a button to the window
button = ttk.Button(root, text="Submit")
button.pack(pady=10)

root.mainloop() # Start the main event loop