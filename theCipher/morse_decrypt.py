""" Name: Lam Dang
    For: CS240 Cryptography The Cipher
    README:
        - Make sure the input.txt file is in the same dir as the code file
        - In terminal, run: python3 morse_decrypt.py
"""


def decrypt(inputFile):
    MORSE_CODE_DICT = { '.-':'A', '-...':'B', 
                    '-.-.':'C', '-..':'D', '.':'E', 
                    '..-.':'F', '--.':'G', '....':'H', 
                    '..':'I', '.---':'J', '-.-':'K', 
                    '.-..':'L', '--':'M', '-.':'N', 
                    '---':'O', '.--.':'P', '--.-':'Q', 
                    '.-.':'R', '...':'S', '-':'T', 
                    '..-':'U', '...-':'V', '.--':'W', 
                    '-..-':'X', '-.--':'Y', '--..':'Z'} 

    REVERSED_CODE_DICT = {'U':'...', 'Q':'..-', 'V':'..x',
                    'I':'.-.', 'M':'.--', 'X':'.-x',
                    'R':'.x.', 'T':'.x-', 'Z':'.xx',
                    'S':'-..', 'W':'-.-', 'G':'-.x',
                    'C':'--.', 'K':'---', 'A':'--x',
                    'F':'-x.', 'P':'-x-', 'O':'-xx',
                    'H':'x..', 'D':'x.-', 'B':'x.x',
                    'L':'x-.', 'N':'x--', 'J':'x-x',
                    'E':'xx.', 'Y':'xx-'}
    
    
    
    inFile = open(inputFile,'r')
    encoded_message = inFile.read()
    encoded_morse = ""

    """Change to Morse Code using Fractionated Morse Code"""
    for char in encoded_message:
        encoded_morse += REVERSED_CODE_DICT[char]

    """Change to Text using Standardized Morse Code"""
    outFile = open("decrypt_ppnbtqip.txt", 'w')
    morse_phrase = ""
    decoded_phrase = ""
    for encoded_char in encoded_morse:
        if encoded_char == 'x':                 #Find the next end of character(word)
            if morse_phrase == "":
                outFile.write(" ")
            else:
                outFile.write(MORSE_CODE_DICT[morse_phrase])    #Decrypt and write to file
            morse_phrase = ""
        else:
            morse_phrase += encoded_char      #Add single signal to the phrase
    
    if len(morse_phrase) != 0:
        outFile.write(MORSE_CODE_DICT[morse_phrase])   #Decrypt the last character if exist
    
    return 0

if __name__ == "__main__":
    decrypt("ppnbtqip.txt")   #Please make sure the input.txt file is in the same dir as the code file.