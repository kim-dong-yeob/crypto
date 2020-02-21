def codebook():
    
    encbook = {'a':'?', 'b':'!', 'c':'@', 'd':')', 'e':'(', 'f':'#', 'g':'%', 'h':'^', 'i':'%',\
                   'j':'a', 'k':'&', 'l':'"', 'm':':', 'n':'~', 'o':'c', 'p':'/', 'q':'`', 'r':'R', \
                   's':'1', 't':'T', 'u':'O', 'v':'*', 'w':'W', 'x':'0', 'y':'9', 'z':'', ' ':'4'}

    decbook = {}

    for key in encbook:
        value = encbook[key]
        decbook[value] = key

    return encbook, decbook

def encrypt(message, encbook):

    for c in message:
        if c in encbook:
            message = message.replace(c, encbook[c])


    return message

def decrypt(message, decbook):

    for c in message:
        if c in decbook:
            message = message.replace(c, decbook[c])

    return message

if __name__=="__main__":

    plaintext = input('input the plaintext: ')

    encbook, decbook = codebook()

    ciphertext = encrypt(plaintext, encbook)
    print(ciphertext)

    deciphertext = decrypt(ciphertext, decbook)
    print(deciphertext)
