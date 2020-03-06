enc = 0
dec = 1

def cipherDisk(key):
    keyTable = map(lambda x: (chr(x+65), x), range(26))

    key2index = {}

    for t in keyTable:
        alphabet, index = t[0], t[1]
        key2index[alphabet] = index
        #print(key2index)
        #print(t[0], t[1])

    if key in key2index:
        k = key2index[key]
    else:
        return None, None

    enc_disk = {}
    dec_disk = {}

    for i in range(26):
        enc_i = (i + k) % 26
        enc_ascii = enc_i + 65
        enc_disk[chr(i + 65)] = chr(enc_ascii)
        dec_disk[chr(enc_ascii)] = chr(i + 65)

    return enc_disk, dec_disk

def caesar(message, key, mode):
    ret = ''

    message = message.upper()
    enc_disk, dec_disk = cipherDisk(key)
    
    if enc_disk is None:
        return ret

    if mode is enc:
        disk = enc_disk
        
    if mode is dec:
        disk = dec_disk

    for c in message:
        if c in disk:
            ret += disk[c]
        else:
            ret += c

    return ret

if __name__=="__main__":

    plaintext = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = 'C'

    print(plaintext.upper())
    ciphertext = caesar(plaintext, key, enc)
    print(ciphertext)
    deciphertext = caesar(ciphertext, key, dec)
    print(deciphertext)
