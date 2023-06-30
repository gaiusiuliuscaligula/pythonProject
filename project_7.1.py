def count_vowels(word):
    vowels = "aeiouy"
    count = 0
    for char in word:
        if char.lower() in vowels:
            count += 1
    return count


def check_rhythm(poem):
    phrases = poem.split()
    first_phrase_vowels = None
    for phrase in phrases:
        words = phrase.split('-')
        phrase_vowels = [count_vowels(word) for word in words]
        if first_phrase_vowels is None:
            first_phrase_vowels = phrase_vowels
        elif phrase_vowels != first_phrase_vowels:
            return "Пам парам"
    return "Парам пам-пам"


poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)
