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

def collectInfo():
    print("Contact Information Form")
    print("Please fill out the following information:")
    name = input("Name: ")
    birthday = input("Birthday (MM-DD-YYYY): ")
    email = input("Email: ")
    phone_number = input("Phone Number: ")
    address = input("Address: ")
    city = input("City: ")
    state = input("State/Province: ")
    zipCode = input("ZIP/Postal Code: ")
    country = input("Country: ")
    preferredContact = input("Preferred Contact Method (Email/Phone): ")

    return name, birthday, email, phone_number, address, city, state, zipCode, country, preferredContact

class Customer: # This class represents a customer and their contact information
    def __init__(self, name, birthday, email, phone_number, address, city, state, zipCode, country, preferredContact):
        self.name = name
        self.birthday = birthday
        self.email = email
        self.phone_number = phone_number

        # Store individual address components
        self.streetAddress = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.country = country

        # Create combined address string
        self.address = f"{address}, {city}, {state}, {zipCode}, {country}"

        self.preferredContact = preferredContact

    def printInfo(self): # This method prints the customer's information
        print(f"Name: {self.name}")
        print(f"Birthday: {self.birthday}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Address: {self.address}")
        print(f"Preferred Contact Method: {self.preferredContact}")

    def saveToDatabase(self): # This method saves the customer's information to the database
        c.execute('''
        INSERT INTO customers (name, birthday, email, phone, address, preferred_contact)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.name, self.birthday, self.email, self.phone_number, self.address, self.preferredContact))
        conn.commit()

def view_all_customers():
    c.execute("SELECT * FROM customers") # Select all records from the customers table
    customers = c.fetchall() # Fetch all records
    
    if not customers: # If there are no customers, print a message
        print("No customers found in the database.")
        return
    
    print("\n----- CUSTOMERS IN DATABASE -----")
    for customer in customers:
        print(f"ID: {customer[0]}, Name: {customer[1]}, Birthday: {customer[2]}, Email: {customer[3]}, Phone: {customer[4]}, Address: {customer[5]}, Preferred Contact: {customer[6]}") # Print each customer's information
    
def main():
    name, birthday, email, phone_number, address, city, state, zipCode, country, preferredContact = collectInfo() # Collect customer information
    
    # Create a new customer object
    customer = Customer(name, birthday, email, phone_number, address, city, state, zipCode, country, preferredContact)
    customer.printInfo() # Print the customer's information
    customer.saveToDatabase() # Save the customer's information to the database

    conn.close() # Close the connection to the database

if __name__ == "__main__":
    main() # Call the main function to execute the program