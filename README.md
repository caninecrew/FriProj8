# Customer Information Management System

## Overview
This application is a Customer Information Management System developed as a project for the DS-3850-001 course. It allows businesses to collect and store customer information through a user-friendly graphical interface. The system features robust data validation, secure storage in an SQLite database, and both GUI and CLI interfaces.

## Features
- **Graphical User Interface**: Modern Tkinter-based interface for data entry
- **Data Validation**: Comprehensive validation for all fields including:
  - Email format verification
  - Phone number formatting
  - Date validation for birthdays
  - US state and ZIP code validation
- **SQLite Database**: Secure local storage of customer information
- **Form Management**: Auto-clearing after submission and placeholder text
- **Dual Interface**: Both GUI and CLI options available

## Installation
1. Ensure Python 3.x is installed on your system
2. Clone this repository
3. No additional dependencies are required as the project uses Python's built-in libraries

## Usage
To run the application with the GUI:
```bash
python friProj8.py
```


If you prefer the command-line interface, modify friProj8.py to uncomment the start_cli() line and comment out import gui.

## Project Structure
- `friProj8.py`: Main entry point of the application
- `gui.py`: Tkinter GUI implementation
- `cli.py`: Command-line interface implementation
- `customer.py`: Customer class definition
- `database.py`: Database management and connection
- `customer.db`: SQLite database file (generated on first run)

## Data Fields
The system collects the following customer information:
- **Personal Information**:
  - Name
  - Birthday (MM-DD-YYYY format)
  - Email
  - Phone number
- **Address Information**:
  - Street address
  - City
  - State/Province
  - ZIP/Postal code
  - Country
- **Contact Preferences**:
  - Preferred contact method (Email, Phone, or Mail)

## Validation Rules
The application performs the following validations:
- All fields are required
- Emails must follow standard format
- US state must be valid 2-letter abbreviation (if country is USA)
- ZIP codes must follow 5-digit or ZIP+4 format (if country is USA)
- Phone numbers must have correct number of digits
- Birthdays must be in valid format and represent a real date

## Implementation Details
### Database
The application uses SQLite for data storage, creating a simple but effective relational database to store customer records. Each customer is assigned a unique ID, and all of their information is stored in a single table for easy retrieval.

### GUI
The graphical interface is built with Tkinter and includes:
- Organized sections for personal and address information
- Visual separators for better readability
- Placeholder text to guide user input
- Clear button to reset the form
- Submit button with validation feedback

### Data Validation
Robust validation ensures data integrity:
- Regular expressions for email, ZIP code, and date format checking
- Dictionary lookup for US state validation
- Comprehensive date validation including leap year checking
- Phone number format normalization

## Future Enhancements
- Customer search functionality
- Data export features 
- Customer record editing
- User authentication
- Data visualization and reporting

## Author
- Samuel Rumbley

