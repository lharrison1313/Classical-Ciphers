import secrets

def generateKey(message):
    
    key = [0 for x in range(len(message))]
    srng = secrets.SystemRandom()
    for i in range(len(message)):
        key[i] = srng.randint(0,65536)
    return key

def OTP(key,message):
    ctArr = [0 for x in range((len(message)))]
    counter = 0
    ct = ""
    for i in key:
        ctArr[counter] = i^ord(message[counter])
        counter += 1
    for i in ctArr:
        ct += chr(i)
    return ct





    
        
        
    
    

                 
        
    
    
