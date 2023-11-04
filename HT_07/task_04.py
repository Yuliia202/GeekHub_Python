# Створіть функцію <morse_code>, яка приймає на вхід рядок у вигляді коду Морзе та виводить декодоване
# значення (латинськими літерами).
#    Особливості:
#     - використовуються лише крапки, тире і пробіли (.- )
#     - один пробіл означає нову літеру
#     - три пробіли означають нове слово
#     - результат може бути case-insensetive (на ваш розсуд - велики чи маленькими літерами).
#     - для простоти реалізації - цифри, знаки пунктуацїї, дужки, лапки тощо використовуватися
# не будуть. Лише латинські літери.
#     - додайте можливість декодування сервісного сигналу SOS (...---...)
#     Приклад:
#     --. . . -.- .... ..- -...   .. ...   .... . .-. .

def morse_code(morse_input):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        'SOS': '...---...',
    }

    morse_input = morse_input.upper()
    morse_words = morse_input.split('   ')
    decoded_message = []

    for word in morse_words:
        morse_letters = word.split(' ')
        decoded_word = ''

        for letter in morse_letters:
            for char, morse_code in morse_code_dict.items():
                if letter == morse_code:
                    decoded_word += char
                    break

        decoded_message.append(decoded_word)

    return ' '.join(decoded_message)


morse_input = input('Please enter Morse code: ')
decoded_message = morse_code(morse_input)
print(decoded_message)
