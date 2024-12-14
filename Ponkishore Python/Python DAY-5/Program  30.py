def length_of_last_word(s: str) -> int:
    # Strip trailing spaces and split the string into words
    words = s.strip().split()
    # Return the length of the last word, or 0 if there are no words
    return len(words[-1]) if words else 0

# Example usage
s = "Hello World   "
print(length_of_last_word(s))# Output: 5
