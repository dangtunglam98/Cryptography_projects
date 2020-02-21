# We have ax + by = g = gcd(a,b)
# Based on the Pseudocode from wikibook
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

import sys
if __name__ == "__main__":
	f = open("input.txt", mode= 'r')
        lines = f.readlines()
        a = int(lines[0])
        m = int(lines[1])
        f.close()
        outFile = open("output.txt", mode= 'w')
        outFile.write(str(modinv(a,m)))
        outFile.close()
