MORSE_CODE_DICT = {' ': '_',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}

class MorseCode():

    # Function to encrypt the string
    # according to the morse code chart
    def encode(message):
        message = message.upper()
        cipher = ''
        for letter in message:
            if letter != ' ':
                cipher += MORSE_CODE_DICT[letter] + ' '
            else:
                cipher += ' '

        return cipher

    # Function to decrypt the string
    # from morse to english
    def decode(message):
        # message += ' '

        decipher = ''
        citext = ''
        for letter in message:
            if (letter != ' '):
                i = 0
                # storing morse code of a single character
                citext += letter
            else:
                i += 1
                if i == 2:
                    # adding space to separate words
                    decipher += ' '
                else:
                    # accessing the keys using their values (reverse of encryption)
                    decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                                                                  .values()).index(citext)]
                    citext = ''

        return decipher