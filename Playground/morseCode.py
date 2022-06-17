#  Convert morse code to english and english to morse code.

dicti = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--.."
}

data = {}

while True:
    query = input('Press:\n1 for English to Morse Code\n2 for Morse Code to English\n')
    if query == '1':
        eng_word = input('Enter your English word: ').lower()
        output = ""
        for letter in eng_word:
            if letter in dicti:
                output += dicti[letter]
            else:
                output += letter
        data[output] = eng_word
        print(output)
    elif query == '2':
        morse_code = input('Enter your Morse Code: ')
        if morse_code in data:
            print(data[morse_code])