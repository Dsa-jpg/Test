def worth_of_words(words):
    letter_values = {
        'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1, 't': 1, 'l': 1, 's': 1, 'u': 1,
        'd': 2, 'g': 2,
        'b': 3, 'c': 3, 'm': 3, 'p': 3,
        'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
        'k': 5,
        'j': 8, 'x': 8,
        'q': 10, 'z': 10
    }

    def word_value(word):
        return sum(letter_values[letter] for letter in word)

    most_valuable_word = max(words, key=word_value)
    return most_valuable_word

# Example usage:
result1 = worth_of_words(['hi', 'quiz', 'bomb', 'president'])
result2 = worth_of_words(['zero', 'one', 'two', 'three', 'four', 'five'])

print(result1)  # Output: 'quiz'
print(result2)  # Output: 'zero'
