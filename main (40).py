key = int(input("Ключ: "))
def xor_cipher(string: str, key: int):
    line = [None] * len(string) 
    for i in range(len(string)):  
        line[i] = str(ord(string[i]) ^ key)
    return " ".join(line)  

def xor_uncipher(string: str, key: int):
    line = string.split()  
    for i in range(len(line)):  
        line[i] = chr(int(line[i]) ^ key)  
    return "".join(line) 
kotak = input("Введите строку которую нужно зашифровать ")
new = xor_cipher(kotak, 146)
print(new)

new_2 = xor_uncipher(new, 146)
print(new_2)