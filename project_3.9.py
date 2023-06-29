def int_func(word):
    return word.capitalize()

print(int_func('text'))  # Output: Text

def int_func(word):
    return word.capitalize()

def capitalize_words(sentence):
    words = sentence.split()
    capitalized_words = [int_func(word) for word in words]
    return ' '.join(capitalized_words)

sentence = 'hello world how are you'
result = capitalize_words(sentence)
print(result)  # Output: Hello World How Are You
