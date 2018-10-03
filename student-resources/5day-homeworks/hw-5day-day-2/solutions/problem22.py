def letter_counter(input):
    letters = {}
    for l in input:
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1

    return letters
