def letter_counter(word):
    result = {}
    for i in word:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    print(result)

letter_counter('banana')




# Uncomment the code below if you want to test out the example code

# word_to_count = "banana"
# result = letter_counter(word_to_count)
# print(result)
