def is_binary_number(number_str):
    # Set of binary digits
    binary_digits = {'0', '1'}
    
    # Check if all characters in the input string are either '0' or '1'
    if set(number_str).issubset(binary_digits):
        return True
    else:
        return False

# Example usage
number_str = input("Enter a number to check if it is binary: ")
if is_binary_number(number_str):
    print(f"{number_str} is a binary number.")