# Напишіть функцію,яка прймає рядок з декількох слів і повертає довжину найкоротшого слова.
# Реалізуйте обчислення за допомогою генератора.

def shortest_word(sentence):
    words = sentence.split()
    shortest_length = min(len(word) for word in words)
    return shortest_length


input_sentence = input("Please input value: ")

result = shortest_word(input_sentence)
print(result)
