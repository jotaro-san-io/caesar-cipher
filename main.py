def encrypt(ptext,shift):
    res = ""
    for i in range(len(ptext)):
        char = ptext[i]

        if char.isupper():
            res += chr((ord(char)+shift - 65) % 26 + 65)
        else:
            res += chr((ord(char)+shift-97)%26+97)
    return res


def decrypt(etext,shift):
    result = ""
    for i in range(len(etext)):
        char = etext[i]

        if char.isupper():
            result += chr((ord(char)-shift - 65) % 26 + 65)
        else:
            result += chr((ord(char)-shift - 97) % 26 + 97)
    return result


text = input('Enter text: ')
shift = int(input('Enter shift key: '))
choice = input('Enter your choice: ')
if choice.upper() == 'ENCRYPT':
    print('Cipher= ',encrypt(text,shift))
elif choice.upper() == 'DECRYPT':
    print('Deciphered = ',decrypt(text,shift))
else:
    print('Invalid choice')