
def createVigenereSquare():
    vSquare = [[0 for x in range(26)] for y in range(26)]
    for r in range(26):
        for c in range(26):
            vSquare[r][c] = (c+r)%26
    return vSquare
    
def encryptVC(key, plaintext):
    key = key.lower()
    plaintext = plaintext.lower()
    vSquare = createVigenereSquare()
    counter = 0
    ciphertext = ""
    
    for i in range(len(plaintext)):
        if ord(plaintext[i]) >= 97 and ord(plaintext[i]) <= 122:
            r = ord(key[counter%len(key)])-97
            c = ord(plaintext[i])-97
            ciphertext += chr((vSquare[r][c])+97)
            counter += 1
        else:
            ciphertext += plaintext[i]
        
    return ciphertext

def decryptVC(key, ciphertext):
    ciphertext = ciphertext.lower()
    key = key.lower()
    vSquare = createVigenereSquare()
    counter = 0
    plaintext = ""

    for i in range(len(ciphertext)):
        if ord(ciphertext[i]) >= 97 and ord(ciphertext[i]) <= 122:
            r = ord(key[counter%len(key)])-97
            letter = ciphertext[i]
            for x in range(26):
                if( chr((vSquare[r][x])+97) == letter):
                    plaintext += chr(x+97)
            counter += 1
        else:
            plaintext += ciphertext[i]

    return plaintext





        
    
