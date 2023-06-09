def XOR_cipher(data, key):
    res=""
    for a in data:
         res=res+chr(ord(a)^key)
    return res
def XOR_uncipher(data,key):
    return XOR_cipher(data,key)
    
print(XOR_cipher("Test",45))
print(XOR_uncipher("yH^Y",45))
