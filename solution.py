def is_palindrome(s: str) -> bool:
    # Remove all non-alphanumeric characters from the string and convert it to lowercase
    s = ''.join(e for e in s if e.isalnum()).lower()
    # Check if the string reads the same forwards and backwards
    return s == s[::-1]

def word_count(s: str) -> int:
    # Split the string into a list of words separated by whitespace
    words = s.split()
    # Return the number of words in the list
    return len(words)