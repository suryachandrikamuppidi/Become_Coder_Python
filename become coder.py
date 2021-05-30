"""
def countPrimeSetBits(self, L, R):
        def isPrime(x):
            if x < 2:
                return False
            for i in range(2, x):
                if not x%i:
                    return False
            return True
        count = 0
        for i in range(L, R+1):
            if isPrime(bin(i)[2:].count('1')):
                count += 1
        return count
"""
"""
def LSB(num, K):

    return bool(num & (1 << (K - 1) ))
num, k =10, 4
 

res = LSB(num, k)

if res :

    print(1)

else:

    print(0)
"""
"""
def printKthBit(n, k):
 

    print((n & (1 << (k - 1))) >> (k - 1))

n = 13

k = 4
 

printKthBit(n, k)
 
"""
"""
def flipBits(a):
   return a ^ 4294967295 # 2^32 - 1
 
if _name_ == '_main_':
    n = int(raw_input())
    for i in range(0,n):
        a = int(raw_input())
        res = flipBits(a)
        print(res)
"""

def count_num_finger(n):
    r = n % 8
    if r == 0:
        return 2
    if r < 5:
        return r
    else:
        return 10 - r
n=32
print(count_num_finger(n))





















