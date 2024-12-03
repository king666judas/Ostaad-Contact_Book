# Ostaad-Contact_Book
------------------------------------------------------------------------------------------------
   Program Description: Contact Management System
   
   This Python-based Contact Management System is a command-line application 
   designed to manage a user's contact list efficiently. It provides essential 
   features for adding, editing, searching, and removing contacts, while ensuring 
   data validation and persistence through file handling.
------------------------------------------------------------------------------------------------   
Features

-- Add Contacts:

   Allows users to input new contact details, including name, phone number, email, and address.
   Validates inputs to ensure data correctness:
      - Names must be strings.
      - Phone numbers must be numeric and unique across the contact list.
      - Emails must contain "@" and ".".
   Saves new contacts to a CSV file for persistence.

-- Edit Contacts:

   Enables users to modify existing contact details.
   Displays current values and lets users update them.
   Updates the CSV file to reflect the changes.

-- Search Contacts:

   Users can search for contacts by name, email, phone number, or address.
   Displays search results in an organized tabular format.
   Offers a repeatable search loop for convenience.

-- View Contacts:

   Displays all saved contacts in an alphabetically sorted, neatly formatted table.
   Provides a comprehensive view of the contact list.

-- Remove Contacts:

   Deletes a contact from the list based on the phone number.
   Ensures the phone number is unique, avoiding accidental deletions.

-- Input Validation:

   A centralized validation system ensures input correctness across all modules.
   Prevents duplicate phone numbers and enforces proper email formatting.

-- File Handling:

   Reads and writes contact data to a contacts.csv file located in the program's directory.
   Automatically loads data from the file upon program start and saves changes during runtime.

-- Return-to-Main Menu:

   Allows users to return to the main menu from any operational module.
   Ensures a consistent and user-friendly navigation experience.

-- Exit Program:

   Provides an option to terminate the program safely.

------------------------------------------------------------------------------------------------

How It’s Written

-- Modular Design:

   The program is divided into multiple Python files (modules), each responsible for a specific   
   functionality:
      - main.py: Main menu and application entry point.
      - validate_input.py: Input validation functions.
      - contact_operations.py: Add, edit, search, and remove contact functions.
      - file_handler.py: Functions for loading and saving data to contacts.csv.
      - utils.py: Utility functions like displaying contacts in a table.

-- Data Storage:

   Contacts are stored in a CSV file in the same directory as the program.
   The CSV format ensures data is easily readable and transferable.

-- User Interaction:

   Uses a text-based menu system to guide users through operations.
   Provides clear prompts and feedback to ensure smooth navigation.

-- Error Handling:

   Includes checks to handle invalid inputs and prevent program crashes.

-- Data Flow:

   Inputs are validated → Processed for the desired operation → Data is updated 
   in the CSV file → Results are displayed.

------------------------------------------------------------------------------------------------

Use Cases:

-- Personal Contact Management: Keep track of family, friends, and professional contacts.
-- Small Business: Maintain a contact list for customers, suppliers, and partners.
-- Academic Projects: Serve as a base for learning Python programming concepts like modularity,       file handling, and validation.

------------------------------------------------------------------------------------------------
