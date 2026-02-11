# Spec: Math Homework Helper Logic

## Overview
This specification defines the math homework helper functionality for the Ralph Wiggum Fun Application. The module implements Ralph's endearing struggle with mathematics by accepting simple addition problems and responding in character. The helper distinguishes between "easy" problems (sum ≤ 10, which Ralph can solve using his fingers) and "hard" problems (sum > 10, which overwhelm Ralph). This feature provides interactive entertainment while staying true to Ralph's character.

## Requirements

### 1. **Script Name**: `math_helper.py`

### 2. **Behavior**:
- **Input Acceptance**:
  - Accept two numbers from the user for addition
  - Support integer and float inputs
  - Handle both positive and negative numbers
  - Process numbers of any magnitude (though responses are based on sum)

- **Calculation Logic**:
  - Calculate the sum of the two input numbers
  - Determine difficulty level based on sum:
    - **Easy**: sum ≤ 10 (Ralph can count on his fingers)
    - **Hard**: sum > 10 (Ralph runs out of fingers)
  - Perform calculation accurately regardless of difficulty

- **Response Generation**:
  - **For Easy Problems (sum ≤ 10)**:
    - Display the correct answer
    - Include an encouraging Ralph-style message
    - Reference counting on fingers or similar Ralph-isms
    - Examples: "I counted on my fingers! The answer is 7! I'm learnding!"
  
  - **For Hard Problems (sum > 10)**:
    - Do NOT display the answer
    - Include a humorous Ralph-style message about difficulty
    - Reference running out of fingers, brain hurting, etc.
    - Examples: "That's too hard! I ran out of fingers! My brain hurts!"

- **Character Voice**:
  - All responses must be in Ralph's voice
  - Use Ralph's vocabulary and speech patterns
  - Include Ralph's characteristic phrases ("I'm learnding!", "unpossible!", etc.)
  - Maintain innocent and endearing tone

### 3. **Data**:
- **Difficulty Threshold**:
  ```python
  DIFFICULTY_THRESHOLD = 10
  ```

- **Response Messages**:
  ```python
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
  ```

- **Data Types**:
  - Input numbers: int or float
  - Sum calculation: float (to handle decimal inputs)
  - Threshold comparison: numeric comparison
  - Response strings: formatted strings with placeholders

### 4. **Execution**:
- **Module Import**:
  ```python
  from math_helper import help_with_math, get_two_numbers
  ```

- **Function Definitions**:
  ```python
  def get_two_numbers():
      """
      Prompt user for two numbers and return them.
      
      Returns:
          tuple: (num1, num2) as floats
          
      Raises:
          ValueError: If input cannot be converted to number
      """
      pass
  
  def calculate_sum(num1, num2):
      """
      Calculate the sum of two numbers.
      
      Args:
          num1 (float): First number
          num2 (float): Second number
          
      Returns:
          float: Sum of num1 and num2
      """
      pass
  
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
      pass
  
  def help_with_math():
      """
      Main function to run the math homework helper.
      Orchestrates input, calculation, and response.
      """
      pass
  ```

- **Execution Flow**:
  1. User selects math helper option from main menu
  2. `help_with_math()` is called
  3. Function prompts for two numbers
  4. Numbers are validated (handled by input validation module)
  5. Sum is calculated
  6. Difficulty is determined (sum ≤ 10 or sum > 10)
  7. Appropriate Ralph-style response is generated and displayed
  8. Control returns to main menu

- **Integration Points**:
  - Called by `ralph_app.py` when user selects option 2 (Help Ralph with math homework)
  - Uses input validation from `ralph_app.py` or dedicated validation module
  - Should complete calculation in < 100ms
  - No external dependencies (uses only Python standard library)

- **Performance Requirements**:
  - Calculation must complete in < 100ms
  - Response generation should be instantaneous
  - Support for numbers up to Python's float limits

## Example Implementation Structure

```python
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

def get_two_numbers():
    """Prompt user for two numbers and return them."""
    print("\nRalph needs help with his math homework!")
    print("Give Ralph two numbers to add together.")
    
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    
    return num1, num2

def calculate_sum(num1, num2):
    """Calculate the sum of two numbers."""
    return num1 + num2

def generate_response(num1, num2, sum_result):
    """Generate Ralph-style response based on difficulty."""
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
    """Main function to run the math homework helper."""
    try:
        # Get input numbers
        num1, num2 = get_two_numbers()
        
        # Calculate sum
        sum_result = calculate_sum(num1, num2)
        
        # Generate and display response
        response = generate_response(num1, num2, sum_result)
        
        print("="*50)
        print(response)
        print("="*50 + "\n")
        
    except ValueError as e:
        print(f"\nOops! Ralph is confused! Please use numbers only.")
    except Exception as e:
        print(f"\nSomething went wrong! Ralph's brain hurts!")
```

## Example Interactions

### Easy Problem (sum ≤ 10):
```
Ralph needs help with his math homework!
Give Ralph two numbers to add together.
First number: 3
Second number: 4

Ralph is trying to solve: 3 + 4
Ralph is thinking really hard...

==================================================
I counted on my fingers! The answer is 7.0! I'm learnding!
==================================================
```

### Hard Problem (sum > 10):
```
Ralph needs help with his math homework!
Give Ralph two numbers to add together.
First number: 8
Second number: 9

Ralph is trying to solve: 8 + 9
Ralph is thinking really hard...

==================================================
That's too hard! I ran out of fingers! My brain hurts!
==================================================
```

### Edge Cases:
```
# Zero sum
Input: 0 + 0 → Output: "Yay! I know this one! It's 0!"

# Negative numbers (sum ≤ 10)
Input: -5 + 3 → Output: "I counted on my fingers! The answer is -2! I'm learnding!"

# Negative numbers (sum > 10)
Input: 20 + (-5) → Output: "That's too hard! I ran out of fingers! My brain hurts!"

# Decimal numbers
Input: 2.5 + 3.5 → Output: "That's easy! I got 6.0! My teacher will be so proud!"
```

## Testing Requirements

### Unit Tests:
1. Test `calculate_sum()` with various number combinations:
   - Positive integers
   - Negative integers
   - Decimal numbers
   - Zero
   - Large numbers

2. Test `generate_response()` logic:
   - Sum exactly 10 (boundary case - should be "easy")
   - Sum exactly 11 (boundary case - should be "hard")
   - Sum < 10 (easy)
   - Sum > 10 (hard)
   - Negative sums

3. Test response message formatting:
   - Verify {answer} placeholder is replaced correctly
   - Verify response is from appropriate list (easy/hard)

4. Test error handling:
   - Invalid input (non-numeric)
   - Empty input
   - Special characters

### Integration Tests:
1. Test complete workflow from input to output
2. Test integration with main application menu
3. Test multiple consecutive calculations
4. Verify no state is maintained between calculations

### Edge Case Tests:
1. Very large numbers (near float limits)
2. Very small numbers (near zero)
3. Exactly at threshold (10)
4. Negative numbers resulting in positive sum
5. Positive numbers resulting in negative sum

## Success Criteria
- ✅ Correctly calculates sum of any two numbers
- ✅ Accurately determines difficulty (≤10 vs >10)
- ✅ Displays correct answer for easy problems
- ✅ Does NOT display answer for hard problems
- ✅ All responses are in Ralph's character voice
- ✅ Handles invalid input gracefully
- ✅ Calculation completes in < 100ms
- ✅ Code follows PEP 8 style guidelines
- ✅ Functions are well-documented with docstrings
- ✅ Provides entertaining and authentic Ralph Wiggum experience