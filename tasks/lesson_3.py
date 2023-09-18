sentence = input("Введите предложение: ")
words = sentence.split()
longest_word = ""
for word in words:
    word = word.strip(",.!?")
    if len(word) > len(longest_word):
        longest_word = word
print("Самое длинное слово в предложении:", longest_word)


sentence = input("Введите строку: ")
new_sentence = ""
for char in sentence:
    if char not in new_sentence and char != " ":
        new_sentence += char
print(new_sentence)


sentence = input("Введите строку: ")
lower_count = 0
upper_count = 0
for char in sentence:
    if char.isalpha() and char.isascii():
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
print("Количество строчных букв:", lower_count)
print("Количество прописных букв:", upper_count)
