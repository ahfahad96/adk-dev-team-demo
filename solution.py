def is_palindrome(s: str) -> bool:
    # Remove spaces and convert to lowercase
    s = ''.join(c for c in s if c.isalnum()).lower()
    # Compare the string with its reverse
    return s == s[::-1]

def word_count(s: str) -> int:
    # Split the string into words by whitespace
    words = s.split()
    # Return the number of words
    return len(words)