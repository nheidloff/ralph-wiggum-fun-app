#!/usr/bin/env python3
"""
Test script for Ralph Wiggum Fun Application
Simulates user interactions to verify functionality
"""

import subprocess
import sys

def test_quote_feature():
    """Test the quote display feature (option 1)"""
    print("Testing quote feature...")
    
    # Simulate: start app, select option 1, then exit
    input_data = "1\n3\n"
    
    result = subprocess.run(
        [sys.executable, "ralph_app.py"],
        input=input_data,
        capture_output=True,
        text=True,
        cwd="/workspace/application"
    )
    
    # Check for expected output
    assert "Ralph Wiggum Fun App!" in result.stdout, "Welcome banner not found"
    assert "What would you like to do?" in result.stdout, "Menu not displayed"
    assert "Ralph Wiggum says:" in result.stdout, "Quote not displayed"
    assert "Bye! I'm going to play now!" in result.stdout, "Goodbye message not found"
    assert result.returncode == 0, f"Non-zero exit code: {result.returncode}"
    
    print("✓ Quote feature test passed")
    return True

def test_math_feature_easy():
    """Test math helper with easy problem (sum <= 10)"""
    print("Testing math feature (easy problem)...")
    
    # Simulate: start app, select option 2, enter 3 + 4, then exit
    input_data = "2\n3\n4\n3\n"
    
    result = subprocess.run(
        [sys.executable, "ralph_app.py"],
        input=input_data,
        capture_output=True,
        text=True,
        cwd="/workspace/application"
    )
    
    # Check for expected output
    assert "Ralph needs help with his math homework!" in result.stdout, "Math prompt not found"
    assert "3.0 + 4.0" in result.stdout or "3 + 4" in result.stdout, "Problem not displayed"
    assert "7" in result.stdout, "Answer not shown for easy problem"
    assert result.returncode == 0, f"Non-zero exit code: {result.returncode}"
    
    print("✓ Math feature (easy) test passed")
    return True

def test_math_feature_hard():
    """Test math helper with hard problem (sum > 10)"""
    print("Testing math feature (hard problem)...")
    
    # Simulate: start app, select option 2, enter 8 + 9, then exit
    input_data = "2\n8\n9\n3\n"
    
    result = subprocess.run(
        [sys.executable, "ralph_app.py"],
        input=input_data,
        capture_output=True,
        text=True,
        cwd="/workspace/application"
    )
    
    # Check for expected output
    assert "Ralph needs help with his math homework!" in result.stdout, "Math prompt not found"
    assert "8.0 + 9.0" in result.stdout or "8 + 9" in result.stdout, "Problem not displayed"
    assert "too hard" in result.stdout.lower() or "ran out of fingers" in result.stdout.lower(), "Hard problem response not found"
    # Should NOT show the answer 17
    assert result.returncode == 0, f"Non-zero exit code: {result.returncode}"
    
    print("✓ Math feature (hard) test passed")
    return True

def test_invalid_menu_input():
    """Test invalid menu input handling"""
    print("Testing invalid menu input...")
    
    # Simulate: start app, enter invalid input, then valid input, then exit
    input_data = "5\n1\n3\n"
    
    result = subprocess.run(
        [sys.executable, "ralph_app.py"],
        input=input_data,
        capture_output=True,
        text=True,
        cwd="/workspace/application"
    )
    
    # Check for error message
    assert "not a number I know" in result.stdout or "can only count to 3" in result.stdout or "brain is confused" in result.stdout, "Error message not found"
    assert result.returncode == 0, f"Non-zero exit code: {result.returncode}"
    
    print("✓ Invalid menu input test passed")
    return True

def test_multiple_features():
    """Test using multiple features in sequence"""
    print("Testing multiple features in sequence...")
    
    # Simulate: quote -> math -> quote -> exit
    input_data = "1\n2\n5\n5\n1\n3\n"
    
    result = subprocess.run(
        [sys.executable, "ralph_app.py"],
        input=input_data,
        capture_output=True,
        text=True,
        cwd="/workspace/application"
    )
    
    # Check that both features executed
    assert "Ralph Wiggum says:" in result.stdout, "Quote not displayed"
    assert "Ralph needs help with his math homework!" in result.stdout, "Math helper not executed"
    assert result.returncode == 0, f"Non-zero exit code: {result.returncode}"
    
    print("✓ Multiple features test passed")
    return True

def test_direct_exit():
    """Test immediate exit (option 3)"""
    print("Testing direct exit...")
    
    # Simulate: start app, immediately exit
    input_data = "3\n"
    
    result = subprocess.run(
        [sys.executable, "ralph_app.py"],
        input=input_data,
        capture_output=True,
        text=True,
        cwd="/workspace/application"
    )
    
    # Check for goodbye message
    assert "Bye! I'm going to play now!" in result.stdout, "Goodbye message not found"
    assert result.returncode == 0, f"Non-zero exit code: {result.returncode}"
    
    print("✓ Direct exit test passed")
    return True

def main():
    """Run all tests"""
    print("="*50)
    print("Ralph Wiggum Fun App - Test Suite")
    print("="*50)
    print()
    
    tests = [
        test_quote_feature,
        test_math_feature_easy,
        test_math_feature_hard,
        test_invalid_menu_input,
        test_multiple_features,
        test_direct_exit
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
        except AssertionError as e:
            print(f"✗ Test failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ Test error: {e}")
            failed += 1
        print()
    
    print("="*50)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("="*50)
    
    return 0 if failed == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
