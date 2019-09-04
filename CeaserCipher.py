
def encrypt(shift,plaintext):
    ct = ""
    for i in plaintext:
        num = ord(i)
        if num >= 97 and num <= 122: 
            ct += chr(97 + (((num-97) + shift)%26))
        elif num >= 65 and num <= 90:
            ct += chr(65 + (((num-65) + shift)%26))
        else:
            ct += i
    return ct

def decrypt(shift,ciphertext):
    pt = ""
    for i in ciphertext:
        num = ord(i)
        if num >= 97 and num <= 122:
            pt += chr(97 + (((num-97) - shift)%26))
        elif num >= 65 and num <= 90:
            pt += chr(65 + (((num-65) - shift)%26))
        else:
            pt += i
    return pt


        
            
        

    
    
    


        
            
