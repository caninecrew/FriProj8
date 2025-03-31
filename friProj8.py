# User interaction (start with text input)

# name, birthday, email, phone number, address, and a dropdown menu for preferred contact method

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

class Customer:
    def __init__(self, name, birthday, email, phone_number, address, city, state, zip, country, preferredContact):
        self.name = name
        self.birthday = birthday
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.country = country
        self.preferredContact = preferredContact