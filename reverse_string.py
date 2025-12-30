# Simple script to reverse a string

def reverse_string(text):
    """
    Takes a string and returns it reversed.
    """
    return text[::-1]

# Get input from user
user_input = input("Enter a string to reverse: ")

# Print the reversed string
reversed_text = reverse_string(user_input)
print(f"Reversed string: {reversed_text}")
