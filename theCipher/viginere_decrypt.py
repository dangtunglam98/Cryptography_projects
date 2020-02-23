def decrypt(cipherFiletext, key):
    encodeFile = open(cipherFiletext, "r")
    encode = encodeFile.read()
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in encode]
    decryptText = ''
    outFile = open('decrypt_' + cipherFiletext, 'w')
    for i in range(len(ciphertext_int)):
        if not chr(ciphertext_int[i]).isalpha():
            decryptText += chr(ciphertext_int[i])
        else:
            value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
            decryptText += chr(value + 65)

    decryptText = decryptText.replace("\'", '\'')
    outFile.write(decryptText)

if __name__ == "__main__":
    decryptText = decrypt("lyovgceu.txt", "dates")
    
