#!/usr/bin/env python3
"""
Ralph Wiggum Fun Application - Math Homework Helper Module

This module implements Ralph's math homework helper functionality.
Accepts two numbers for addition and responds based on difficulty.

Author: IBM Bob
Version: 1.0
Date: February 11, 2026
"""

import random

# Constants
DIFFICULTY_THRESHOLD = 10

EASY_RESPONSES = [
    "I counted on my fingers! The answer is {answer}! I'm learnding!",
    "That's easy! I got {answer}! My teacher will be so proud!",
    "I used my fingers and toes! The answer is {answer}!",
    "Yay! I know this one! It's {answer}!"
]

HARD_RESPONSES = [
    "That's too hard! I ran out of fingers! My brain hurts!",
    "I can't count that high! My head feels funny!",
    "That's unpossible! I only have 10 fingers!",
    "Too many numbers! I need a nap!"
]

MATH_INPUT_ERROR_MESSAGES = [
    "That's not a number! Ralph needs numbers to count!",
    "I don't understand! Please use numbers like 5 or 3.14!",
    "My brain hurts! That's not a number I can count!"
]


def get_validated_number(prompt):
    """
    Get a validated number from user with retry logic.
    
    Args:
        prompt (str): Prompt message to display
        
    Returns:
        float: Valid number from user
    """
    while True:
        try:
            user_input = input(prompt)
            number = float(user_input)
            return number
        except ValueError:
            error_msg = random.choice(MATH_INPUT_ERROR_MESSAGES)
            print(f"{error_msg}")
            # Loop continues, re-prompting user
        except KeyboardInterrupt:
            # Re-raise to be caught at main level
            raise


def get_two_numbers():
    """
    Prompt user for two numbers and return them.
    
    Returns:
        tuple: (num1, num2) as floats
    """
    print("\nRalph needs help with his math homework!")
    print("Give Ralph two numbers to add together.")
    
    num1 = get_validated_number("First number: ")
    num2 = get_validated_number("Second number: ")
    
    return num1, num2


def calculate_sum(num1, num2):
    """
    Calculate the sum of two numbers.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        
    Returns:
        float: Sum of num1 and num2
    """
    return num1 + num2


def generate_response(num1, num2, sum_result):
    """
    Generate Ralph-style response based on difficulty.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        sum_result (float): The calculated sum
        
    Returns:
        str: Ralph's response message
    """
    print(f"\nRalph is trying to solve: {num1} + {num2}")
    print("Ralph is thinking really hard...\n")
    
    if sum_result <= DIFFICULTY_THRESHOLD:
        # Easy problem - Ralph can solve it!
        response = random.choice(EASY_RESPONSES).format(answer=sum_result)
    else:
        # Hard problem - too difficult for Ralph
        response = random.choice(HARD_RESPONSES)
    
    return response


def help_with_math():
    """
    Main function to run the math homework helper.
    Orchestrates input, calculation, and response.
    """
    # Get input numbers
    num1, num2 = get_two_numbers()
    
    # Calculate sum
    sum_result = calculate_sum(num1, num2)
    
    # Generate and display response
    response = generate_response(num1, num2, sum_result)
    
    print("=" * 50)
    print(response)
    print("=" * 50 + "\n")
