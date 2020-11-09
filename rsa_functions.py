import number_theory_functions
from number_theory_functions import *

class RSA():
    def __init__(self, public_key, private_key = None):
        self.public_key = public_key
        self.private_key = private_key

    @staticmethod
    def generate(digits = 10):
        """
        Creates an RSA encryption system object

        Parameters
        ----------
        digits : The number of digits N should have

        Returns
        -------
        RSA: The RSA system containing:
        * The public key (N,e)
        * The private key (N,d)
        """
        
        prime_1 = generate_prime(digits)
        prime_2 = generate_prime(digits)
        # prime_1 = 7919
        # prime_2 = 6841
        n = prime_1*prime_2
        k = (prime_1 - 1) * (prime_2 - 1)
        while True:
            candidate = randrange(1, k - 1)
            if extended_gcd(candidate, k)[0] == 1:
                e = candidate
                break

        d = modular_inverse(e, k)

        return RSA(
            public_key=(n, e),
            private_key=(n, d)
        )


    def encrypt(self, m):
        """
        Encrypts the plaintext m using the RSA system

        Parameters
        ----------
        m : The plaintext to encrypt

        Returns
        -------
        c : The encrypted ciphertext
        """
        n, e = self.public_key
        # print(n,e)
        return modular_exponent(m, e, n)


    def decrypt(self, c):
        """
        Decrypts the ciphertext c using the RSA system

        Parameters
        ----------
        c : The ciphertext to decrypt

        Returns
        -------
        m : The decrypted plaintext
       """
        n, d = self.private_key
        return modular_exponent(c, d, n)
