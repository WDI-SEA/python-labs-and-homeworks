def letter_count(word):
    count = {}
    for letter in word:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    return count

result = letter_count("banana")
print(result)