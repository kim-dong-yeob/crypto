
def makeDisk(k):
    dec_disk = {}

    for i in range(26):
        alphabet = (i + k) % 26 + 65
        dec_disk[chr(alphabet)] = chr(i + 65)

    return dec_disk

def caesar(message, key):
    ret = ''
    message = message.upper()
    disk = makeDisk(key)

    for c in message:
        if c in disk:
            ret += disk[c]
        else:
            ret += c

    return ret

def attack(message):
    for key in range(1, 26):
        decmsg = caesar(message, key)
        print("SHIFT[%d]: %s" %(key, decmsg))

if __name__=="__main__":
    message = "V ybir clguba"
    attack(message)