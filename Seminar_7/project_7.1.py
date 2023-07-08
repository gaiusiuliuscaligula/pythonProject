# Задание 1.
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова,
# если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Стихотворение Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
# если с ритмом все не в порядке

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
