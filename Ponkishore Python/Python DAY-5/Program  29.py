def reverse_word(word):
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    return reversed_word

# Example usage
input_word = "Python"
result = reverse_word(input_word)
print("Reversed word:",result)
