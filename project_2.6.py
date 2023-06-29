sentence = input("Введите строку из нескольких слов: ")

words = sentence.split()

for i, word in enumerate(words):
    truncated_word = word[:10] if len(word) > 10 else word
    print(f"{i+1}. {truncated_word}")
