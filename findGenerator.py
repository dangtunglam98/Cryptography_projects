def computeGCD(x, y): 
  
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i 
              
    return gcd 

def find_all_coprime(y):
    co_primes = []
    for i in range(2,y):
        if computeGCD(i, y) == 1:
            co_primes.append(i)
    return co_primes


def find_generator(y):
    co_prime = find_all_coprime(y)
    generator = []
    for x in co_prime:
        print("For the number " + str(x))
        result = x
        resultList = []
        for i in range(len(co_prime)+1):
            result = (result*x)%y
            resultList.append(result)
            print(str(result), end=', ')
        print("\n")
    
        if len(set(resultList)) == len(resultList):  
            generator.append(x)
            print(str(x) + " is a generator")
        else:
            print(str(x) + " is NOT a generator")

        print("\n")
    if len(generator) != 0:
        print("generators are " + str(generator))
    else:
        print("There are no generators")

if __name__== "__main__":
    assignment = [9,13,17,19,27,12,15]
    for number in assignment:
        print("For n = " + str(number) + ':')
        find_generator(number)
        print("---------------------------------------------------------------------------")

