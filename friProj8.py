# 1. Imports
from database import conn, c, view_all_customers, close_connection
from customer import Customer
from cli import collectInfo, start_cli

def main(): # This is the main function that orchestrates the program flow
    
    start_cli() # Start the command line interface for customer information collection
    close_connection() # Close the database connection

# 5. Main Program Execution
if __name__ == "__main__":
    main() # Call the main function to execute the program