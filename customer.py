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