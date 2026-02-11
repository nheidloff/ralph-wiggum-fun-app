# Spec: Input Validation & Error Handling

## Overview
This specification defines the input validation and error handling mechanisms for the Ralph Wiggum Fun Application. Robust input validation ensures the application handles all user inputs gracefully, preventing crashes and providing helpful, character-appropriate error messages. The validation system covers menu selections, numeric inputs for math problems, and unexpected errors, all while maintaining Ralph Wiggum's endearing personality in error messages.

## Requirements

### 1. **Script Name**: `ralph_app.py` and `math_helper.py` (validation distributed across modules)

### 2. **Behavior**:

#### **Menu Input Validation**:
- **Valid Input Range**: Accept only '1', '2', or '3' as valid menu choices
- **Input Type**: Accept string input from user
- **Validation Process**:
  - Strip whitespace from input
  - Check if input is in valid set {'1', '2', '3'}
  - If invalid, display error message and re-prompt
  - Do not crash or exit on invalid input
- **Error Response**: Display Ralph-themed error message for invalid choices
- **Retry Mechanism**: Allow unlimited retry attempts until valid input received

#### **Math Input Validation**:
- **Valid Input Types**: Accept numeric values (integers and floats)
- **Supported Formats**:
  - Positive integers: `5`, `42`, `100`
  - Negative integers: `-5`, `-42`, `-100`
  - Positive decimals: `3.14`, `0.5`, `10.75`
  - Negative decimals: `-3.14`, `-0.5`, `-10.75`
  - Zero: `0`, `0.0`
- **Invalid Inputs to Reject**:
  - Non-numeric strings: `abc`, `hello`, `ralph`
  - Special characters: `@`, `#`, `$`, `%`
  - Empty input: `` (just pressing Enter)
  - Mixed alphanumeric: `5a`, `3.14abc`
  - Multiple numbers: `5 10`, `3,4`
- **Validation Process**:
  - Attempt to convert input to float
  - If conversion fails, catch ValueError
  - Display error message and re-prompt
  - Allow retry until valid number received
- **Error Response**: Display Ralph-themed error message for invalid numbers

#### **Exception Handling**:
- **KeyboardInterrupt (Ctrl+C)**:
  - Catch gracefully at main application level
  - Display Ralph-themed exit message
  - Exit cleanly with status code 0
- **ValueError**:
  - Catch during numeric input conversion
  - Display helpful error message
  - Re-prompt for input
- **General Exceptions**:
  - Catch unexpected errors at main level
  - Display generic error message
  - Exit with status code 1
  - Log error details (optional for debugging)

#### **Error Message Characteristics**:
- **Tone**: Friendly, in Ralph's voice
- **Clarity**: Explain what went wrong
- **Guidance**: Suggest what to do next
- **Character**: Maintain Ralph's innocent, confused personality
- **No Technical Jargon**: Avoid terms like "ValueError", "invalid type", etc.

### 3. **Data**:

#### **Validation Constants**:
```python
# Menu validation
VALID_MENU_CHOICES = {'1', '2', '3'}

# Error messages
MENU_ERROR_MESSAGES = [
    "That's not a number I know! Please choose 1, 2, or 3.",
    "I can only count to 3! Pick 1, 2, or 3!",
    "My brain is confused! Use 1, 2, or 3!"
]

MATH_INPUT_ERROR_MESSAGES = [
    "That's not a number! Ralph needs numbers to count!",
    "I don't understand! Please use numbers like 5 or 3.14!",
    "My brain hurts! That's not a number I can count!"
]

KEYBOARD_INTERRUPT_MESSAGES = [
    "\n\nRalph got scared! Bye bye!",
    "\n\nI have to go now! My cat's breath smells like cat food!",
    "\n\nBye! I'm going to play with my toys!"
]

GENERAL_ERROR_MESSAGE = "\nOops! Something went wrong! Ralph's brain hurts!"
```

#### **Validation Functions**:
```python
def validate_menu_choice(choice):
    """
    Validate menu choice input.
    
    Args:
        choice (str): User's menu selection
        
    Returns:
        bool: True if valid, False otherwise
    """
    pass

def validate_numeric_input(input_str):
    """
    Validate and convert numeric input.
    
    Args:
        input_str (str): User's input string
        
    Returns:
        float: Converted number if valid
        
    Raises:
        ValueError: If input cannot be converted to number
    """
    pass

def get_validated_number(prompt):
    """
    Get a validated number from user with retry logic.
    
    Args:
        prompt (str): Prompt message to display
        
    Returns:
        float: Valid number from user
    """
    pass
```

### 4. **Execution**:

#### **Menu Validation Flow**:
```python
def get_user_choice():
    """Get and validate user's menu choice."""
    while True:
        choice = input("Choose an option (1-3): ").strip()
        
        if choice in VALID_MENU_CHOICES:
            return choice
        else:
            error_msg = random.choice(MENU_ERROR_MESSAGES)
            print(f"\n{error_msg}\n")
            # Loop continues, re-prompting user
```

#### **Math Input Validation Flow**:
```python
def get_validated_number(prompt):
    """Get a validated number from user with retry logic."""
    while True:
        try:
            user_input = input(prompt)
            number = float(user_input)
            return number
        except ValueError:
            error_msg = random.choice(MATH_INPUT_ERROR_MESSAGES)
            print(f"{error_msg}")
            # Loop continues, re-prompting user

def get_two_numbers():
    """Get two validated numbers from user."""
    print("\nRalph needs help with his math homework!")
    print("Give Ralph two numbers to add together.")
    
    num1 = get_validated_number("First number: ")
    num2 = get_validated_number("Second number: ")
    
    return num1, num2
```

#### **Exception Handling at Main Level**:
```python
def main():
    """Main application entry point with error handling."""
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
        # Optional: log error for debugging
        # print(f"Debug info: {e}")
        sys.exit(1)
```

#### **Integration Points**:
- Menu validation integrated into `ralph_app.py` menu loop
- Math input validation integrated into `math_helper.py` input functions
- Exception handling wraps main application entry point
- All validation functions return to normal flow after handling errors

#### **Error Recovery**:
- Invalid menu choice → Re-display menu and prompt again
- Invalid math input → Re-prompt for that specific number
- Keyboard interrupt → Display message and exit cleanly
- Unexpected error → Display message and exit with error code

## Example Implementation Structure

```python
import random
import sys

# Validation constants
VALID_MENU_CHOICES = {'1', '2', '3'}

MENU_ERROR_MESSAGES = [
    "That's not a number I know! Please choose 1, 2, or 3.",
    "I can only count to 3! Pick 1, 2, or 3!",
    "My brain is confused! Use 1, 2, or 3!"
]

MATH_INPUT_ERROR_MESSAGES = [
    "That's not a number! Ralph needs numbers to count!",
    "I don't understand! Please use numbers like 5 or 3.14!",
    "My brain hurts! That's not a number I can count!"
]

KEYBOARD_INTERRUPT_MESSAGES = [
    "\n\nRalph got scared! Bye bye!",
    "\n\nI have to go now! My cat's breath smells like cat food!",
    "\n\nBye! I'm going to play with my toys!"
]

GENERAL_ERROR_MESSAGE = "\nOops! Something went wrong! Ralph's brain hurts!"

# Validation functions
def validate_menu_choice(choice):
    """
    Validate menu choice input.
    
    Args:
        choice (str): User's menu selection
        
    Returns:
        bool: True if valid, False otherwise
    """
    return choice in VALID_MENU_CHOICES

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

def get_user_choice():
    """
    Get and validate user's menu choice.
    
    Returns:
        str: Valid menu choice ('1', '2', or '3')
    """
    while True:
        choice = input("Choose an option (1-3): ").strip()
        
        if validate_menu_choice(choice):
            return choice
        else:
            error_msg = random.choice(MENU_ERROR_MESSAGES)
            print(f"\n{error_msg}\n")

def main():
    """Main application entry point with comprehensive error handling."""
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
        # Optional: print debug info in development
        # import traceback
        # traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
```

## Example Error Scenarios

### Invalid Menu Choice:
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

Choose an option (1-3): hello

I can only count to 3! Pick 1, 2, or 3!

What would you like to do?

1. Show me a Ralph quote
2. Help Ralph with math homework
3. Exit

Choose an option (1-3): 2

[Proceeds to math helper...]
```

### Invalid Math Input:
```
Ralph needs help with his math homework!
Give Ralph two numbers to add together.
First number: abc
That's not a number! Ralph needs numbers to count!
First number: @#$
I don't understand! Please use numbers like 5 or 3.14!
First number: 5
Second number: hello
My brain hurts! That's not a number I can count!
Second number: 3

Ralph is trying to solve: 5.0 + 3.0
[Continues normally...]
```

### Keyboard Interrupt:
```
What would you like to do?

1. Show me a Ralph quote
2. Help Ralph with math homework
3. Exit

Choose an option (1-3): ^C

Ralph got scared! Bye bye!
```

### Empty Input:
```
Ralph needs help with his math homework!
Give Ralph two numbers to add together.
First number: 
That's not a number! Ralph needs numbers to count!
First number: 5
Second number: 
I don't understand! Please use numbers like 5 or 3.14!
Second number: 3

[Continues normally...]
```

## Edge Cases to Handle

### Menu Validation:
- Empty string: `` → Invalid
- Whitespace only: `   ` → Invalid (after strip)
- Leading/trailing spaces: ` 1 ` → Valid (after strip)
- Multiple characters: `12` → Invalid
- Decimal: `1.0` → Invalid
- Negative: `-1` → Invalid

### Math Input Validation:
- Very large numbers: `999999999999` → Valid
- Very small numbers: `0.0000001` → Valid
- Scientific notation: `1e10` → Valid (Python float supports it)
- Leading zeros: `007` → Valid (converts to 7.0)
- Negative zero: `-0` → Valid (converts to 0.0)
- Infinity: `inf` → Valid (Python float supports it)
- NaN: `nan` → Valid (Python float supports it)

### Exception Handling:
- Ctrl+C during menu prompt → Caught and handled
- Ctrl+C during math input → Caught and handled
- Ctrl+C during feature execution → Caught and handled
- Unexpected system errors → Caught and logged

## Testing Requirements

### Unit Tests:
1. **Menu Validation**:
   - Test valid inputs: '1', '2', '3'
   - Test invalid inputs: '0', '4', 'a', '', '1.5'
   - Test whitespace handling: ' 1 ', '  2  '

2. **Math Input Validation**:
   - Test valid integers: '5', '-10', '0'
   - Test valid floats: '3.14', '-2.5', '0.0'
   - Test invalid inputs: 'abc', '', '@#$', '5a'
   - Test edge cases: very large/small numbers, scientific notation

3. **Error Message Display**:
   - Verify error messages are displayed
   - Verify messages are in Ralph's voice
   - Verify random selection from message lists

### Integration Tests:
1. Test complete flow with invalid inputs followed by valid inputs
2. Test multiple consecutive invalid inputs
3. Test keyboard interrupt at various points
4. Test recovery after errors (application continues normally)

### Manual Testing Scenarios:
1. Try every type of invalid menu input
2. Try every type of invalid math input
3. Test Ctrl+C at different points in application
4. Test rapid invalid inputs
5. Test mixing valid and invalid inputs
6. Verify application never crashes from user input

## Success Criteria
- ✅ All invalid menu inputs are caught and handled gracefully
- ✅ All invalid math inputs are caught and handled gracefully
- ✅ Application never crashes from user input
- ✅ Error messages are clear, helpful, and in Ralph's voice
- ✅ Users can recover from errors and continue using the application
- ✅ Keyboard interrupt (Ctrl+C) is handled gracefully
- ✅ Unexpected errors are caught and logged appropriately
- ✅ Validation provides unlimited retry attempts
- ✅ No technical jargon in error messages
- ✅ Code follows PEP 8 style guidelines
- ✅ Functions are well-documented with docstrings
- ✅ Application maintains character consistency even in error states