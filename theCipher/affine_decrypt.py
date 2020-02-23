def egcd(a, b):
    s, old_s = 0, 1
    while a != 0:
        quotient = b // a
        b, a = a , b - a * quotient    #Assigning new a and b for gcd
        s, old_s = old_s, s - old_s * quotient  #Keep track to get the inverse number
    
    return b, s


def modinv(a, m):
    g , s = egcd(a, m)
    if g != 1:
        return None
    else:
        if s < 0:
            s += m
        return s


def decryptFile(encodeFileText, a, b):
    encodeFile = open(encodeFileText, "r")
    encode = encodeFile.read()
    decrypt = ""
    inverse_a = modinv(a,26)
    outFile = open("decrypt_" + encodeFileText, 'w')
    for char in encode:
        outFile.write(chr(((inverse_a * (ord(char) - ord("A") - b)) % 26) + ord("A")))
    
    # outFile = open("output_" + encodeFile, 'w')
    # outFile.write(decrypt)

if __name__ == "__main__":
    decryptFile("irydkbkh.txt", 11, 1)
    decryptFile("vvcenyzc.txt", 1, 7)