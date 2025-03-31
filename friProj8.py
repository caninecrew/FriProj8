import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('customer.db') # This will create a new database file named customer.db in the current directory
c = conn.cursor() # Create a cursor object to interact with the database

# Create a table for customer information if it doesn't exist
c.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    birthday TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    preferred_contact TEXT NOT NULL            
);
''')

# Commit the changes to the database
conn.commit()

print("Contact Information Form")
print("Please fill out the following information:")
name = input("Name: ")
birthday = input("Birthday (MM-DD-YYYY): ")
email = input("Email: ")
phone_number = input("Phone Number: ")
address = input("Address: ")
city = input("City: ")
state = input("State/Province: ")
zip = input("ZIP/Postal Code: ")
country = input("Country: ")
preferredContact = input("Preferred Contact Method (Email/Phone): ")


class Customer: # This class represents a customer and their contact information
    def __init__(self, name, birthday, email, phone_number, address, city, state, zip, country, preferredContact):
        self.name = name
        self.birthday = birthday
        self.email = email
        self.phone_number = phone_number

        # Store individual address components
        self.streetAddress = address
        self.city = city
        self.state = state
        self.zip = zip
        self.country = country

        # Create combined address string
        self.address = f"{address}, {city}, {state}, {zip}, {country}"
        
        self.preferredContact = preferredContact

# Create a new customer object
customer = Customer(name, birthday, email, phone_number, address, city, state, zip, country, preferredContact)


conn.close() # Close the connection to the database