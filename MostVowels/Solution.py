def most_vowels(word):
    most_vowel_word = ""
    vowels = "aeiou"
    vowel_count = 0
    most_vowel = 0
    for item in word:
        for x in item:
            if x in vowels:
                vowel_count += 1
            if vowel_count > most_vowel:
              most_vowel_word = item
              most_vowel = vowel_count
        vowel_count = 0
    return most_vowel_word
