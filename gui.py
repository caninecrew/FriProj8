from tkinter import * # Import the tkinter module
from tkinter import ttk # Import the ttk module for themed widgets
from tkinter import messagebox # Import the messagebox module for pop-up messages
from customer import Customer # Import the Customer class from customer.py
from database import view_all_customers # Import the view_all_customers function from database.py
import re # Import the re module for regular expressions
from datetime import datetime # Import the datetime module for date handling

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

def clearForm():
    """Clear all entry fields in the form."""
    name_entry.delete(0, END)
    birthday_entry.delete(0, END)
    email_entry.delete(0, END)
    phone_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zip_entry.delete(0, END)

    # country defaults to placeholder "USA"
    country_entry.delete(0, END)
    country_entry.insert(0, "USA")
    country_entry.config(foreground='gray')

    # reset dropdown to first option
    contact_combobox.current(0)

    # Set focus back to the name entry field
    name_entry.focus()

def submitForm():
    """Submit the form and save customer information."""
    name = name_entry.get()
    birthday = birthday_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    city = city_entry.get()
    state = state_entry.get()
    zipCode = zip_entry.get()
    country = country_entry.get()
    preferredContact = contact_combobox.get()

    # Validate that all fields are filled
    if not all([name, birthday, email, phone, address, city, state, zipCode, country]):
        messagebox.showerror("Error", "All fields are required")
        return
    
    # Additional validation for birthday format
    if not re.match(r"\d{2}-\d{2}-\d{4}", birthday):
        messagebox.showerror("Error", "Birthday must be in MM-DD-YYYY format")
        return
    
    # Validate birthday is realistic
    try:
        # Parse the birthday to check if it's a valid date
        parts = birthday.split('-')
        month, day, year = int(parts[0]), int(parts[1]), int(parts[2])

        # Check month range
        if month < 1 or month > 12:
            messagebox.showerror("Error", "Month must be between 1 and 12")
            return
        
        # Check day range based on month
        maxDays = {
            1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }

        if day < 1 or day > maxDays[month]:
            messagebox.showerror("Error", "Invalid day for the given month")
            return
        
        # Check for February in non-leap years
        if month == 2 and day == 29:
            if not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                messagebox.showerror("Error", f"February 29 only exists in leap years")
                return
            
        # Check year range (between 1900 and current year)
        current_year = datetime.now().year
        if year < 1900:
            messagebox.showerror("Error", "Birth year must be 1900 or later")
            return
            
        if year > current_year:
            messagebox.showerror("Error", "Birth year cannot be in the future")
            return
        
        # Check if birthday is in the future
        birth_date = datetime(year, month, day)
        if birth_date > datetime.now():
            messagebox.showerror("Error", "Birthday cannot be in the future")
            return
        
    except ValueError:
        messagebox.showerror("Error", "Invalid date format")
        return
        
    # Create a new Customer object
    try:
        customer = Customer(name, birthday, email, phone, address, city, state, zipCode, country, preferredContact)
        
        # Save to database
        customer.saveToDatabase()

        # Show success message
        messagebox.showinfo("Success", "Customer information saved successfully!")
        
        # Clear the form after submission
        clearForm()
    
    except Exception as e:
        messagebox.showerror("Error", f"Could not save customer: {str(e)}")
        return

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

# Buttons frame
button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=20)

# Submit and Clear buttons
submit_button = ttk.Button(button_frame, text="Submit", style="Accent.TButton", command=submitForm)
submit_button.pack(side=LEFT, padx=5)

clear_button = ttk.Button(button_frame, text="Clear Form", command=clearForm)
clear_button.pack(side=LEFT, padx=5)

# Apply a modern theme if available
try:
    # Try to use a more modern theme if available
    style = ttk.Style()
    style.theme_use('clam')  # Also try: 'alt', 'classic', 'default', 'vista'
    
    # Create a custom style for the Submit button
    style.configure("Accent.TButton", font=("Arial", 10, "bold"))
except:
    pass  # If theme is not available, continue with default

root.mainloop() # Start the main event loop