def is_palindrome(text: str) -> bool:
    # Remove spaces and convert to lowercase
    cleaned_text = text.replace(" ", "").lower()
    
    # Check if the text is equal to its reverse
    return cleaned_text == cleaned_text[::-1]

# --- Test Cases ---
print(is_palindrome("madam"))    # True
print(is_palindrome("python"))   # False
print(is_palindrome("Racecar"))  # True
print(is_palindrome("nurses run")) # True
