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

def save_customer(name, birthday, email, phone, address, preferred_contact):
    """Save a customer to the database"""
    c.execute('''
    INSERT INTO customers (name, birthday, email, phone, address, preferred_contact)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, birthday, email, phone, address, preferred_contact))
    conn.commit()

def view_all_customers(): # This function retrieves and displays all customers from the database

    c.execute("SELECT * FROM customers") # Select all records from the customers table
    customers = c.fetchall() # Fetch all records
    
    if not customers: # If there are no customers, print a message
        print("No customers found in the database.")
        return
    
    print("\n----- CUSTOMERS IN DATABASE -----")
    for customer in customers:
        print(f"ID: {customer[0]}, Name: {customer[1]}, Birthday: {customer[2]}, Email: {customer[3]}, Phone: {customer[4]}, Address: {customer[5]}, Preferred Contact: {customer[6]}") # Print each customer's information

def close_connection():
    """Close the database connection"""
    conn.close()