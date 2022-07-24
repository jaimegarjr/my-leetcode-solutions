class Solution:
    """
    Brute Force
    Runtime: O(n^2)
    Space: O(1)
    def countPrimes(self, n: int) -> int:
        count = 0
        for num in range(2, n):
            if self.isPrime(num):
                count += 1
        
        return count
    
    def isPrime(self, n: int) -> bool:
        if n <= 1: return False
        for i in range(2, n):
            if (n % i == 0): return False
        
        return True
    """
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        
        count = 0
        primes = [True] * n
        primes[0], primes[1] = False, False
        
        for i in range(2, int(sqrt(n))+1):
            if primes[i]:
                for m in range(i * i, n, i):
                    primes[m] = False
        
        return sum(primes)