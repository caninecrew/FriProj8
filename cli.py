from customer import Customer
from database import view_all_customers

def collectInfo(): # This function collects customer information from the user
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
    validContactMethods = ["email", "phone", "mail"]
    preferredContact = input("Preferred Contact Method (Email/Phone/Mail): ").lower()

    return name, birthday, email, phone_number, address, city, state, zipCode, country, preferredContact

def start_cli():
    name, birthday, email, phone_number, address, city, state, zipCode, country, preferredContact = collectInfo() # Collect customer information
    
    # Create a new customer object
    customer = Customer(name, birthday, email, phone_number, address, city, state, zipCode, country, preferredContact)
    customer.printInfo() # Print the customer's information
    customer.saveToDatabase() # Save the customer's information to the database

    view_all_customers() # View all customers in the database