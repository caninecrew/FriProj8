# 1. Imports
from database import conn, c, view_all_customers, close_connection

# 2. Database Connection and Setup






# 3. Class Definition

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

# 4. Function Definitions

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


    
def main(): # This is the main function that orchestrates the program flow
    name, birthday, email, phone_number, address, city, state, zipCode, country, preferredContact = collectInfo() # Collect customer information
    
    # Create a new customer object
    customer = Customer(name, birthday, email, phone_number, address, city, state, zipCode, country, preferredContact)
    customer.printInfo() # Print the customer's information
    customer.saveToDatabase() # Save the customer's information to the database

    view_all_customers() # View all customers in the database

    close_connection() # Close the database connection

# 5. Main Program Execution
if __name__ == "__main__":
    main() # Call the main function to execute the program