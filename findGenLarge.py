def exp(a, n, p):
    temp_n = n # used to convert n to binary
    temp_a = a # this will be the power of a
    result = 1

    while temp_n != 0:
        if temp_n % 2 == 1:
            result = (result * temp_a) % p
        temp_a = (temp_a * temp_a) % p
        temp_n //= 2

    return result

def computeGCD(x, y): 
  
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i 
              
    return gcd 
def get_mod(generator, factor, prime):
    power = (prime - 1)//factor
    return exp(generator, power, prime)

def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

def get_generator(factors, prime):
    for generator in range(2,prime):
        if isPrime(generator) == True:
            tracker = True
            for factor in factors:
                if get_mod(generator, factor, prime) == 1:
                    tracker = False
                    break
                else: 
                    continue
            if tracker == True:
                return generator

if __name__ == "__main__":
    print("For p = 28658912364823164892341239593846211")
    prime = 28658912364823164892341239593846331
    factors = [2,5,19,43,1361,1823,1413815875790673909094183]
    print("Generator is " + str(get_generator(factors, prime)))

    print("For p = 41236478923164789123648972364919458403")
    prime = 41236478923164789123648972364919458429
    factors = [2,11,31,139,552091,200485661,357269325951058459]
    print("Generator is " + str(get_generator(factors, prime)))