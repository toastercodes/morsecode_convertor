morse_table = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    ":": "---...",
    ";": "_._._.",
    "'": ".----.",
    '"': ".-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "/": "-..-.",
    "-": "-....-",
    "=": "-...-",
    "+": ".-.-.",
    "!": "-.-.--",
    "&": ".-...",
    "_": "..--.-",
    "$": "...-..-",
    "¿": "..-.-",
    "¡": "--...-",
    "@": ".--.-.",
    " ": "/",
}

rev_morse_table = { v: k for k, v in morse_table.items()}

def encode(string):
    return ' '.join(morse_table[c] for c in string.upper())

def decode(morse):
    return ''.join(rev_morse_table[c] for c in morse.split())

def main():
    print('Welcome To Morse Code Convertor!')
    print()

    while True:
        print('Available Commands: encode, decode')
        cmd = input('Enter a command(q to quit): ').lower()

        if cmd == 'q':
            break
        elif cmd == 'encode':
            txt = input('Enter Text To Encode: ')
            print(encode(txt))
        elif cmd == 'decode':
            morse = input('Enter Morse Code: ')
            print(decode(morse))
        else:
            print('Unrecognised Command!')
            continue
    
    print('Exiting!')

main()