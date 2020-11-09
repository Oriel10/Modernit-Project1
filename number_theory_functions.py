from random import randrange

#d = a*x +b*y 
def extended_gcd(a,b):
    #same base case like reg gcd
    if a==0:   
        return b,0,1

    d, x1, y1 = extended_gcd(b%a, a)  
    
    x = y1 - (b//a) * x1  
    y = x1  
    return d, x, y 


def modular_inverse(a, n):
    """
    Returns the inverse of a modulo n if one exists

    Parameters
    ----------
    a : Input data.
    n : Input data.

    Returns
    -------
    x: such that (a*x % n) == 1 and 0 <= x < n if one exists, else None
    """
    d, x, y = extended_gcd(a, n) # d = a*x+y*n
    if d != 1:
        return None
    return x % n
    


def modular_exponent(a, d, n):
    """
    Returns a to the power of d modulo n

    Parameters
    ----------
    a : The exponential's base.
    d : The exponential's exponent.
    n : The exponential's modulus.

    Returns
    -------
    b: such that b == (a**d) % n
    """
    # bin_num = bin(d)[-1:1:-1]#turn d to binary base
    
    # bin_num_len = len(bin_num)
    # digits = [2**i for i in range(bin_num_len)]#list of powers
    # num_comp = [int(bin_num[i])*digits[i] for i in range(len(digits))]
    
    # res = 1
    # for item in num_comp:
    #     while item != 0 and item != 1 and a != 1:
    #         a = (a**2)%n
    #         item = item//2
    #     res*= a
    
 
    return pow(a,d,n)

def miller_rabin(n):
    """
    Checks the primality of n using the Miller-Rabin test

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a 3/4 chance at least to be False
    """
    a = randrange(1,n)
    k = 0
    d = n-1
    while d % 2 == 0:
        k = k + 1
        d = d // 2
    x = modular_exponent(a, d, n)
    if x == 1 or x == n-1:
        return True
    for _ in range(k):
        x = (x * x) % n
        if x == 1:
            return False
        if x == n-1:
            return True
    return False

def is_prime(n):
    """
    Checks the primality of n

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a chance of less than 1e-10 to be True
    """
    for _ in range(10):
        if not miller_rabin(n):
            return False
    return True

def generate_prime(digits):
    for i in range(digits * 10):
        n = randrange(10**(digits-1), 10**digits)
        if is_prime(n):
            return n
    return None
