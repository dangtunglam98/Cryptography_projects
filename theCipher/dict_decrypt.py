if __name__ == "__main__":   
    dictionary = {"k":"s", "r":"a", "z":"i","a":"d", "i":"l", "u":"n", "v":"e", "l":"h", "m":"w",
                "s":"o", "f":"t", "d":"u", "x":"g", "p":"v", "j":"c", "b":"r", "c":"b", "t":"m",
                "g":"p", "o":"y", "h":"f", "n":"k", "q":"x", "w":"j"}
    encode = open("ujuekpcv.txt" , "r").read()
    decode = ""
    for char in encode:
        if char in dictionary:
            decode += dictionary[char]
        else:
            decode += char
    outFile = open("decrypt_ujuekpcv.txt", 'w')
    outFile.write(decode)