def letter_counter(str):
  letter_counts = {}
  for letter in str:
    if letter in letter_counts:
      letter_counts[letter] += 1
    else:
      letter_counts[letter] = 1
  return(letter_counts)

print(letter_counter('banana'))