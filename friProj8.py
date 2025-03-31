from database import close_connection
from cli import start_cli


def main(): # This is the main function that orchestrates the program flow
    
    # start_cli() # Start the command-line interface for user input
    import gui # Import the GUI module to start the GUI interface
    close_connection() # Close the database connection

# 5. Main Program Execution
if __name__ == "__main__":
    main() # Call the main function to execute the program