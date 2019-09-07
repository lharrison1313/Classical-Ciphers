
def Atbash(plaintext):
    plaintext = plaintext.lower()
    ciphertext = ""
    for x in plaintext:
        if(ord(x) >= 97 and ord(x) <= 122):
            ciphertext += chr((25-(ord(x)-97))+97)
        else:
            ciphertext += x
    return ciphertext




        
