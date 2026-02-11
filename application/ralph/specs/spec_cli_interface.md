# Spec: CLI Interface & Menu System

## Overview
This specification defines the Command-Line Interface (CLI) and menu system for the Ralph Wiggum Fun Application. The interface provides users with a simple, intuitive menu-based navigation system to access the application's features. The menu system serves as the primary user interaction point, routing users to either the random quote display or the math homework helper, while maintaining Ralph Wiggum's playful character throughout the experience.

## Requirements

### 1. **Script Name**: `ralph_app.py` (menu system component)

### 2. **Behavior**:
- **Application Startup**:
  - Display a welcome banner when application starts
  - Show the Ralph Wiggum Fun App title with decorative formatting
  - Present the main menu immediately after banner
  - Create a friendly, inviting atmosphere

- **Menu Display**:
  - Present a clear, numbered menu with 3 options:
    1. Show me a Ralph quote
    2. Help Ralph with math homework
    3. Exit
  - Use consistent formatting and spacing
  - Include decorative elements (borders, separators) for visual appeal
  - Menu should be easy to read and understand at a glance

- **User Input Handling**:
  - Prompt user to select an option (1-3)
  - Accept numeric input from user
  - Validate input is within valid range (1-3)
  - Handle invalid input gracefully with error messages
  - Re-display menu after invalid input

- **Menu Navigation**:
  - **Option 1**: Call quote display functionality from `quotes.py`
  - **Option 2**: Call math helper functionality from `math_helper.py`
  - **Option 3**: Display goodbye message and exit application
  - After completing Option 1 or 2, return to main menu (loop)
  - Only Option 3 should terminate the application

- **Menu Loop**:
  - Implement continuous loop that keeps menu active
  - Loop should continue until user selects Exit (option 3)
  - After each feature execution, clear screen (optional) and redisplay menu
  - Provide smooth transitions between features and menu

- **Exit Behavior**:
  - Display a Ralph-themed goodbye message
  - Clean exit without errors
  - Return control to terminal/command prompt
  - No cleanup required (no files, connections, etc.)

### 3. **Data**:
- **Menu Structure**:
  ```python
  MENU_OPTIONS = {
      '1': 'Show me a Ralph quote',
      '2': 'Help Ralph with math homework',
      '3': 'Exit'
  }
  ```

- **Display Text**:
  ```python
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
  
  INVALID_CHOICE_MESSAGE = "That's not a number I know! Please choose 1, 2, or 3."
  ```

- **Valid Input Range**:
  - Acceptable inputs: '1', '2', '3' (as strings)
  - Any other input is invalid
  - Case-insensitive handling not required (numeric only)

### 4. **Execution**:
- **Module Structure**:
  ```python
  # Imports
  from quotes import get_random_quote, display_quote
  from math_helper import help_with_math
  import sys
  
  # Display functions
  def display_welcome_banner():
      """Display the welcome banner."""
      pass
  
  def display_menu():
      """Display the main menu options."""
      pass
  
  def get_user_choice():
      """Get and validate user's menu choice."""
      pass
  
  def handle_menu_choice(choice):
      """Execute the appropriate action based on user choice."""
      pass
  
  def display_goodbye():
      """Display goodbye message."""
      pass
  
  def run_menu():
      """Main menu loop."""
      pass
  ```

- **Execution Flow**:
  1. Application starts with `python ralph_app.py`
  2. `display_welcome_banner()` shows welcome message
  3. Enter main menu loop via `run_menu()`
  4. Loop iteration:
     - Display menu with `display_menu()`
     - Get user choice with `get_user_choice()`
     - Validate input
     - If valid, execute choice with `handle_menu_choice()`
     - If invalid, show error and continue loop
  5. If user selects Exit (3):
     - Display goodbye message
     - Break loop
     - Exit application

- **Integration Points**:
  - Imports and calls `get_random_quote()` and `display_quote()` from `quotes.py`
  - Imports and calls `help_with_math()` from `math_helper.py`
  - Entry point for entire application
  - Coordinates all feature modules

- **Command-Line Execution**:
  ```bash
  # Standard execution
  python ralph_app.py
  
  # With Python 3 explicitly
  python3 ralph_app.py
  ```

- **Performance Requirements**:
  - Menu display should be instantaneous
  - No noticeable delay between menu selections
  - Responsive to user input
  - Smooth transitions between features

## Example Implementation Structure

```python
#!/usr/bin/env python3
"""
Ralph Wiggum Fun Application
Main CLI interface and menu system
"""

from quotes import get_random_quote, display_quote
from math_helper import help_with_math
import sys

# Constants
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

INVALID_CHOICE_MESSAGE = "That's not a number I know! Please choose 1, 2, or 3."

def display_welcome_banner():
    """Display the welcome banner."""
    print(WELCOME_BANNER)

def display_menu():
    """Display the main menu options."""
    print(MENU_TEXT)

def get_user_choice():
    """
    Get and return user's menu choice.
    
    Returns:
        str: User's input choice
    """
    choice = input("Choose an option (1-3): ").strip()
    return choice

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
        
    else:
        # Invalid choice
        print(f"\n{INVALID_CHOICE_MESSAGE}\n")
        return True

def display_goodbye():
    """Display goodbye message."""
    print(GOODBYE_MESSAGE)

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
    """Main application entry point."""
    try:
        run_menu()
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\n\nRalph got scared! Bye bye!")
        sys.exit(0)
    except Exception as e:
        print(f"\nOops! Something went wrong: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

## Example User Interactions

### Successful Navigation:
```
=================================
  Ralph Wiggum Fun App!
=================================

What would you like to do?

1. Show me a Ralph quote
2. Help Ralph with math homework
3. Exit

Choose an option (1-3): 1

==================================================
Ralph Wiggum says:
"Me fail English? That's unpossible!"
==================================================

What would you like to do?

1. Show me a Ralph quote
2. Help Ralph with math homework
3. Exit

Choose an option (1-3): 3

=================================
Bye! I'm going to play now!
- Ralph
=================================
```

### Invalid Input Handling:
```
What would you like to do?

1. Show me a Ralph quote
2. Help Ralph with math homework
3. Exit

Choose an option (1-3): 5

That's not a number I know! Please choose 1, 2, or 3.

What would you like to do?

1. Show me a Ralph quote
2. Help Ralph with math homework
3. Exit

Choose an option (1-3): abc

That's not a number I know! Please choose 1, 2, or 3.

What would you like to do?

1. Show me a Ralph quote
2. Help Ralph with math homework
3. Exit

Choose an option (1-3): 2

[Math helper executes...]
```

### Keyboard Interrupt (Ctrl+C):
```
What would you like to do?

1. Show me a Ralph quote
2. Help Ralph with math homework
3. Exit

Choose an option (1-3): ^C

Ralph got scared! Bye bye!
```

## UI/UX Considerations

### Visual Design:
- Use consistent border characters (=, -, *)
- Maintain uniform spacing between sections
- Keep menu compact but readable
- Use blank lines strategically for visual separation

### User Experience:
- Menu should be self-explanatory
- No need for additional help text
- Error messages should be friendly and in Ralph's voice
- Quick return to menu after each action
- No unnecessary prompts or confirmations

### Accessibility:
- Plain text only (no special characters that might not render)
- Works in any terminal/command prompt
- No color dependencies (optional enhancement)
- Clear, readable font size (terminal default)

## Testing Requirements

### Unit Tests:
1. Test `get_user_choice()` with various inputs
2. Test `handle_menu_choice()` with each valid option (1, 2, 3)
3. Test `handle_menu_choice()` with invalid inputs
4. Test menu loop continues after options 1 and 2
5. Test menu loop exits after option 3

### Integration Tests:
1. Test complete flow: start → quote → menu → math → menu → exit
2. Test multiple iterations of same feature
3. Test alternating between features
4. Test keyboard interrupt handling
5. Verify proper module imports and function calls

### Manual Testing Scenarios:
1. Start application and verify banner displays
2. Select each menu option and verify correct feature executes
3. Test invalid inputs (letters, numbers out of range, special characters)
4. Test rapid menu selections
5. Test Ctrl+C at various points
6. Verify clean exit with option 3

## Success Criteria
- ✅ Menu displays clearly with all 3 options
- ✅ User can navigate to quote feature (option 1)
- ✅ User can navigate to math helper (option 2)
- ✅ User can exit application (option 3)
- ✅ Invalid inputs are handled gracefully
- ✅ Menu loop continues until user chooses to exit
- ✅ Application starts and exits cleanly
- ✅ Interface is intuitive for first-time users
- ✅ All text is in Ralph's character voice
- ✅ Code follows PEP 8 style guidelines
- ✅ Functions are well-documented with docstrings