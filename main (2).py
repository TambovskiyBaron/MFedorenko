key = int(input("Введите ключ"))
def xor_cipher(str, key):
    shifr_str = ""
    for letter in str:
        shifr_str += chr(ord(letter) ^ key)
    return shifr_str
    print("зашифрованный текст:\n", shifr_strg)

def xor_cipher_encrypt(str, key):
    print("расшифрованный текст:\n", xor_cipher(shifr_strg, key))

strg = input("Введите строку для шифрации   ")
key = 8
print("ваш текст:\n", strg)
shifr_strg = xor_cipher(strg, key)
xor_cipher_encrypt(strg, key)
print("зашифрованный текст:\n", shifr_strg)