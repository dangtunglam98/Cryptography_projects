def decrypt(cipherFiletext, key):
    encodeFile = open(cipherFiletext, "r")
    encode = encodeFile.read()
    key_length = len(key)
    keyChar_ord = [ord(i) for i in key]
    encodeChar_ord = [ord(i) for i in encode]
    decryptText = ''
    outFile = open('decrypt_' + cipherFiletext, 'w')
    for i in range(len(encodeChar_ord)):
        if not chr(encodeChar_ord[i]).isalpha():
            decryptText += chr(encodeChar_ord[i])
        else:
            value = (encodeChar_ord[i] - keyChar_ord[i % key_length]) % 26
            decryptText += chr(value + 65)

    decryptText = decryptText.replace("\'", '\'')
    outFile.write(decryptText)

if __name__ == "__main__":
    decryptText = decrypt("lyovgceu.txt", "dates")
    
