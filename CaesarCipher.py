
def encryptCC(shift,plaintext):
    plaintext = plaintext.lower()
    ct = ""
    for i in plaintext:
        num = ord(i)
        if num >= 97 and num <= 122: 
            ct += chr(97 + (((num-97) + shift)%26))
        else:
            ct += i
    return ct

def decryptCC(shift,ciphertext):
    ciphertext = ciphertext.lower()
    pt = ""
    for i in ciphertext:
        num = ord(i)
        if num >= 97 and num <= 122:
            pt += chr(97 + (((num-97) - shift)%26))
        else:
            pt += i
    return pt





    
    
    


        
            
