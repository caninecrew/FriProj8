from tkinter import * # Import the tkinter module
from tkinter import ttk # Import the ttk module for themed widgets
from tkinter import messagebox # Import the messagebox module for pop-up messages
from customer import Customer # Import the Customer class from customer.py
from database import view_all_customers # Import the view_all_customers function from database.py

root = Tk() # Create the main window
root.title("Customer Information Form")
root.geometry("500x600") # Set the window size
root.configure(bg="#f0f0f0") # Set the background color

# Create a main frame with padding
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill=BOTH, expand=True)

# Add a title label to the window
title_label = ttk.Label(main_frame, text="Customer Information", font=("Arial", 12, "bold"))
title_label.pack(pady=(0, 20))

# Seperator for visual separation
ttk.Separator(main_frame, orient='horizontal').pack(fill=X, pady=5)

# Personal Info Section
personal_label = ttk.Label(main_frame, text="Personal Information", font=("Arial", 12))
personal_label.pack(anchor=W, pady=(10, 5))

# Function to create a form field
def createField(parent, labelText, width=12, placeholder=None):
    frame = ttk.Frame(parent)
    frame.pack(fill=X, pady=5)
    label = ttk.Label(frame, text=labelText, width=width, anchor=W)
    label.pack(side=LEFT)
    entry = ttk.Entry(frame)
    entry.pack(side=LEFT, fill=X, expand=True)

    # Placeholder text for entry fields
    if placeholder:
        entry.insert(0, placeholder)
        entry.config(foreground='gray')
        
        # Clear placeholder on focus
        def on_focus_in(event):
            if entry.get() == placeholder:
                entry.delete(0, END)
                entry.config(foreground='black')
                
        # Restore placeholder if field is empty
        def on_focus_out(event):
            if entry.get() == '':
                entry.insert(0, placeholder)
                entry.config(foreground='gray')
                
        entry.bind('<FocusIn>', on_focus_in)
        entry.bind('<FocusOut>', on_focus_out)

    return frame, label, entry

# Create fields for customer information
name_frame, name_label, name_entry = createField(main_frame, "Name:")
birthday_frame, birthday_label, birthday_entry = createField(main_frame, "Birthday:")
email_frame, email_label, email_entry = createField(main_frame, "Email:")
phone_frame, phone_label, phone_entry = createField(main_frame, "Phone:")

# Separator for visual organization
ttk.Separator(main_frame, orient='horizontal').pack(fill=X, pady=10)

# Address Section
address_label = ttk.Label(main_frame, text="Address Information", font=("Arial", 12))
address_label.pack(anchor=W, pady=(10, 5))

address_frame, address_label, address_entry = createField(main_frame, "Address:")
city_frame, city_label, city_entry = createField(main_frame, "City:")
state_frame, state_label, state_entry = createField(main_frame, "State:")
zip_frame, zip_label, zip_entry = createField(main_frame, "ZIP Code:")
country_frame, country_label, country_entry = createField(main_frame, "Country:", placeholder="USA")

# Separator for visual organization
ttk.Separator(main_frame, orient='horizontal').pack(fill=X, pady=10)

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