#!/usr/bin/env python3
"""
Ralph Wiggum Fun Application
Main CLI interface and menu system

This is the main entry point for the Ralph Wiggum Fun Application.
Provides a menu-driven interface to access quote display and math helper features.

Author: IBM Bob
Version: 1.0
Date: February 11, 2026
"""

# Standard library imports
import sys
import random

# Local module imports
from quotes import get_random_quote, display_quote
from math_helper import help_with_math

# Application constants
APP_NAME = "Ralph Wiggum Fun App"
APP_VERSION = "1.0"

# Display text
WELCOME_BANNER = """
=================================
  Ralph Wiggum Fun App!
=================================
"""

MENU_TEXT = """
What would you like to do?

1. Show me a Ralph quote
2. Help Ralph with math homework
3. Exit
"""

GOODBYE_MESSAGE = """
=================================
Bye! I'm going to play now!
- Ralph
=================================
"""

# Validation constants
VALID_MENU_CHOICES = {'1', '2', '3'}

MENU_ERROR_MESSAGES = [
    "That's not a number I know! Please choose 1, 2, or 3.",
    "I can only count to 3! Pick 1, 2, or 3!",
    "My brain is confused! Use 1, 2, or 3!"
]

KEYBOARD_INTERRUPT_MESSAGES = [
    "\n\nRalph got scared! Bye bye!",
    "\n\nI have to go now! My cat's breath smells like cat food!",
    "\n\nBye! I'm going to play with my toys!"
]

GENERAL_ERROR_MESSAGE = "\nOops! Something went wrong! Ralph's brain hurts!"


# Display functions
def display_welcome_banner():
    """Display the welcome banner."""
    print(WELCOME_BANNER)


def display_menu():
    """Display the main menu options."""
    print(MENU_TEXT)


def display_goodbye():
    """Display goodbye message."""
    print(GOODBYE_MESSAGE)


# Input handling functions
def get_user_choice():
    """
    Get and validate user's menu choice.
    
    Returns:
        str: Valid menu choice ('1', '2', or '3')
    """
    while True:
        choice = input("Choose an option (1-3): ").strip()
        
        if choice in VALID_MENU_CHOICES:
            return choice
        else:
            error_msg = random.choice(MENU_ERROR_MESSAGES)
            print(f"\n{error_msg}\n")


# Feature routing
def handle_menu_choice(choice):
    """
    Execute the appropriate action based on user choice.
    
    Args:
        choice (str): User's menu selection
        
    Returns:
        bool: True to continue menu loop, False to exit
    """
    if choice == '1':
        # Show random quote
        quote = get_random_quote()
        display_quote(quote)
        return True
        
    elif choice == '2':
        # Help with math homework
        help_with_math()
        return True
        
    elif choice == '3':
        # Exit application
        display_goodbye()
        return False


# Main application flow
def run_menu():
    """
    Main menu loop.
    Displays menu and handles user choices until exit.
    """
    display_welcome_banner()
    
    continue_running = True
    while continue_running:
        display_menu()
        choice = get_user_choice()
        continue_running = handle_menu_choice(choice)


def main():
    """
    Main application entry point.
    Handles application lifecycle and error management.
    """
    try:
        run_menu()
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        msg = random.choice(KEYBOARD_INTERRUPT_MESSAGES)
        print(msg)
        sys.exit(0)
    except Exception as e:
        # Handle unexpected errors
        print(GENERAL_ERROR_MESSAGE)
        sys.exit(1)


# Entry point
if __name__ == "__main__":
    main()
