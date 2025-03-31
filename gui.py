from tkinter import * # Import the tkinter module
from tkinter import ttk # Import the ttk module for themed widgets
from tkinter import messagebox # Import the messagebox module for pop-up messages
from customer import Customer # Import the Customer class from customer.py
from database import view_all_customers # Import the view_all_customers function from database.py

root = Tk() # Create the main window
root.title("Customer Information Form")
root.geometry("450x430") # Set the window size

# Create a main frame with padding
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill=BOTH, expand=True)

# Add a title label to the window
title_label = ttk.Label(root, text="Contact Information", font=("Arial", 12, "bold"))
title_label.pack(pady=(0, 15))

# Function to create a form field
def createField(parent, labelText, width=10):
    frame = ttk.Frame(parent)
    frame.pack(fill=X, pady=5)
    label = ttk.Label(frame, text=labelText, width=width, anchor=W)
    label.pack(side=LEFT)
    entry = ttk.Entry(frame)
    entry.pack(side=LEFT, fill=X, expand=True)
    return frame, label, entry

# Create fields for customer information
name_frame, name_label, name_entry = createField(main_frame, "Name:")
birthday_frame, birthday_label, birthday_entry = createField(main_frame, "Birthday:")
email_frame, email_label, email_entry = createField(main_frame, "Email:")
phone_frame, phone_label, phone_entry = createField(main_frame, "Phone:")
address_frame, address_label, address_entry = createField(main_frame, "Address:")
city_frame, city_label, city_entry = createField(main_frame, "City:")
state_frame, state_label, state_entry = createField(main_frame, "State:")
zip_frame, zip_label, zip_entry = createField(main_frame, "ZIP Code:")
country_frame, country_label, country_entry = createField(main_frame, "Country:")

# Preferred Contact (dropdown)
contact_frame = ttk.Frame(main_frame)
contact_frame.pack(fill=X, pady=5)
contact_label = ttk.Label(contact_frame, text="Preferred Contact:", width=16, anchor=W)
contact_label.pack(side=LEFT)
contact_combobox = ttk.Combobox(contact_frame, values=["Email", "Phone", "Mail"], width=17, state="readonly")
contact_combobox.current(0)  # Set default to first option
contact_combobox.pack(side=LEFT)

# Add a button to the window
button = ttk.Button(main_frame, text="Submit")
button.pack(pady=10)

root.mainloop() # Start the main event loop