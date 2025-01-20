#Lerato Moholo
#Palindromic Primes
#21/09/2024

N = int(input("Enter the start point N:\n"))
M = int(input("Enter the end point M:\n"))

# is the number a prime number?
print("The palindromic primes are:")
for i in range(N+1,M):
    number = True     # nuber is prime until proven otherwise
    
    # from 2 until sqrt(number)
    for j in range(2, int(i**0.5) + 1):
        r =i % j
        if r == 0:      # remeinder is not zero
            number = False  # then number is not a prime number
            break
    
    # If the number is prime, print it
    if number and i > 1: # up to so far I know these are prime numbers
        k= i
        g = str(k)
        p = g[::-1]
        t = int(p)
        if t==i:
            
            print(i)
        
        
