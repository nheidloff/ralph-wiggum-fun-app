#!/usr/bin/env python3
"""
Ralph Wiggum Fun Application - Quote Storage & Selection Module

This module handles storage and random selection of Ralph Wiggum quotes.
Provides functions to retrieve and display quotes in character.

Author: IBM Bob
Version: 1.0
Date: February 11, 2026
"""

import random

# Quote storage - authentic Ralph Wiggum quotes from The Simpsons
RALPH_QUOTES = [
    "I'm a unitard!",
    "Me fail English? That's unpossible!",
    "My cat's breath smells like cat food.",
    "I bent my Wookiee.",
    "I'm learnding!",
    "That's where I saw the leprechaun. He tells me to burn things!",
    "My doctor said I wouldn't have so many nose bleeds if I kept my finger outta there.",
    "When I grow up, I want to be a principal or a caterpillar."
]


def get_random_quote():
    """
    Select and return a random Ralph Wiggum quote.
    
    Returns:
        str: A randomly selected quote from RALPH_QUOTES
        
    Raises:
        ValueError: If RALPH_QUOTES is empty
    """
    if not RALPH_QUOTES:
        raise ValueError("No quotes available")
    return random.choice(RALPH_QUOTES)


def display_quote(quote):
    """
    Display a quote with proper formatting.
    
    Args:
        quote (str): The quote to display
    """
    print("\n" + "=" * 50)
    print("Ralph Wiggum says:")
    print(f'"{quote}"')
    print("=" * 50 + "\n")
