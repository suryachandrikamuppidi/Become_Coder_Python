"""
n=int(input())
for i in range(0,n+1):
        print(i,end=" ")
"""
"""
n=int(input())
i=n
while i>=1:
    print(i,end=" ")
    i-=1
"""
"""
num=int(input())
while num>0:##/num!=0/num
        print(num,end=" ")
        num-=1
"""
"""
num=int(input())
i=1
while i<=num:
    if i%3==0:
        i+=1
        continue
  print(i,end=" ")
    i+=1
"""
"""
n=int(input())
i=1
while i<num:
    print(i,end=" ")
    i+=1
    if
"""
"""
n=int(input())
while num:
  r=num%10
  num=num//10
  print(r,num)
"""

"""
n=int(input())
s=0
while True:
s=0
    while num:
        r=num%10
        num=num//10
        s+=r
  if s>9:
        num=s
        print(num)
    else:
        print(s)
        break
"""
"""
num=int(input())
s=0
while num:
        r=num%10
        num=num//10
        s+=r
        if num==0 and s>9:
            num=s
            s=0
print(s)
"""    
"""
num,r1,r2=map(int,input().split())
inc=1
if r1>r2:
    inc=-1
for i in range(r1,r2+inc,inc):
    print(num," x ",i," = ",num*i)
"""
"""
num1,num2,r1=map(int,input().split())
for i in range(1,r1+1):
    if i%3==0:
        continue
    print(num1," x ",i," = ",num*i)
 """
"""
num=int(input())
while True:
    r=num%10
    num=num//10
    print(r,num)
    if num==0:
        break
"""
"""
num=int(input())
while num!=0:
    r=num%10
    num=num//10
    print(r,num)
"""
"""
num=int(input())
c=0
while num:
    r=num%10
    num=num//10
    c+=1
    print(c)
"""

"""
n=int(input())
even=0
odd=0
while n:
    r=n%10
    n=n//10
    if r%2==0:
        even+=1
    else:
        odd+=1
if even%2==0:
    print(' even')
if odd%2:
    print('odd')
if even%2 and odd%2==0:
    print('mixed')
"""
"""
n=int(input())
even=0
odd=0
while n:
    r=n%10
    n=n//10
    if r%2==0:
        even=even*10+r
    else:
        odd=odd*10+r
print(even,odd)
"""

"""n=int(input())
even=0
odd=0
ec=1
oc=1
while n:
    r=n%10
    n=n//10
    if r%2:
        odd=odd+r*oc
        oc=oc*10
    else:
        even=even+r*10
        ec=ec*10
print(even,odd)
"""
"""
n,a,b=map(int,input().split())
nnm=0
c=1//c=0
while n:
    r=n%10
    n=n//10
    if r==a:
        r=b
    nnm=nnm+r*c//nnm=nnm+r*pow(10,c)
    c=c*10
print(nnm)
"""
"""
n,sv,rv=map(int,input().split())
rev=0
while n:
    r=n%10
    n=n//10
    rev=rev*10+r
print(rev)
while 
    if r==a:
        r=b
    elif r%a==0:
        r=(r//2)
    nnm=nnm+r*c
    c=c*10
print(nnm)
"""
"""
n=int(input())
temp=n
min=n%10
max=n%10
while n:
    r=n%10
    n=n//10
    if r>max:
        max=r
    elif r<min:
        min=r
print(min,max)
n=temp
a=0
b=0
while n:
    r=n%10
    n=n//10
    if r==min:
        a+=1
    elif r==max:
        b+=1
print('no.of min digits=',a,'no.of max digits=',b)
"""
"""
n=int(input())
min=n%10
max=n%10
minc=0
maxc=0
while n:
    r=n%10
    n=n//10
    if r==min:
        minc+=1
    elif r<min:
        min=r
        minc=1
    if r==max:
        maxc+=1
    elif r>max:
        max=r
        maxc=1
print(minc,maxc)
"""
"""
def sum(a,b):
    res=a+b
    return res
r=sum(1,2)
print(r)
"""
"""
def sum_of_threenumbers(a=0,b=0,c=0):
    print(a,b,c)
    res=a+b+c
    return res
a=int(input())
b=int(input())
r=sum_of_threenumbers(a,b,c)
print(r)
"""
"""
def gen_fib(L,U,a=0,b=0):
     if L==0:
        print(a,b,end=" ")
     if L==1:
         print(b,end=" ")
     c=0
     i=1
     while c<=U:
        c=a+b
        if c>=L and c<=U:10
        
            print(c,end=" ")
        a=b
        b=c
        print(i)
        i+=1
L,U=map(int,input().split())
gen_fib(L,U)
"""
"""
def isfib(n):
     if n==0 or n==1:
          return True
     a=0
     b=1
     while True:
          c=a+b
          if c==n:
               return True
          if c>n:
               return False
          a=b
          b=c
          
n=int(input())
print(isfib(n))
"""
"""
def isfib(n):
     if n==0 or n==1:
          return True
     a=0
     b=1
     
     cn=2
     while True:
          c=a+b
          cn+=1
          if c==n:
               return True
          print(cn)
          if c>n:
               return False
          a=b
          b=c
n=int(input())
print(isfib(n))
"""
"""
a,b=map(int,input().split())
n=0
while True:
     if a%2:
          n=n+b
     a=a//2
     b=b*2
     if a==0:
          break
print(n)
"""
"""
def mul(a,b):
     res=0
     while True:
          if a%2:
               res+=b
          if a==0:
               break
          a//=2
          b*=2
a,b=map(int,input().split())
res mul(a,b)
 print(res)
"""
"""
n=int(input())
print(n,end=" ")
while True:
          if n==1:
               break
          if n%2:
               n=3*n+1
          else:
               n=n//2
print(n)
"""
"""
def seq(n):
     if n%2:
          return 3*n+1
     return n//2
n=int(input())
print(n,end=" ")
while(n;=seq(n)):
     print(n,end=" ")
     if n==1:
          break
"""
"""
# recursion
def mul(a,b):
     if a==1:
          return 1
     if a%2:
          return b+mul(a//2,b*2)
     else:
          return 0+mul(a//2,b*2)
a,b=map(int,input().split())
print(mul(a,b))
"""
"""
def fibi(a,b,d,num):
     if d>num:
          return
     if d==1 and d<=num:
          print(a,end=" ")
          d+=1
     if d==2 and d<=num:
          print(b,end=" ")
          d+=1
     if d<=num:
          print(a+b,end=" ")
          fibi(b,a+b,d+1,num)
num=int(input())
fibi(0,1,1,num)                                                                                                                                                                                                                                                  
"""
"""
def rev(n,s=0,r=0):
     if n==0:
          print(s)
          return
     r=n%10
     n=n//10
     s=s*10+r
     rev(n,s=s,r=r)
     
n=int(input())
print(rev(n))
"""
"""
def armstrng(num):
     sum=0
     temp=num
     while temp>0:
          digit=temp%10
          sum+=pow(digit,3)
          temp//=10
     if num==sum:
          print(num ,'armstrong number')
     else:
          print(num,'not an armstrong number')
num=int(input())
print(armstrng(num))
"""
"""
def gcd(a,b):
     if a>b:
          a,b=b,a
     b=b%a
     return a
a,b=map(int,input().split())
print(gcd(a,b))
"""
"""
def pronic(n):
      for i in range(1,n//2+1):
           print(i)
           if i*(i+1)==n:
                return True
      return False
n=int(input())
print(pronic(n))
"""
#Disarium:
"""
def isdisarium(n):
     dc=0
     temp=n
     while temp:
          temp//=10
          dc+=1
     temp=n
     res=0
     while temp:
          r=temp%10
          temp//=10
          res+=pow(r,dc)
"""
"""
#Harshadh number:
def harshadh(n):
     temp=n
     sum=0
     while n:
          r=n%10
          n=n//10
          sum+=r
     if (temp%sum==0):
          print(True)
     else:
          print(False)
n=int(input())
harshadh(n)
"""
"""
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()
"""
"""
n=int(input())
for i in range(0,n):
    for j in range(0,n):
        print(j+1,end=" ")
    print()
"""
""" stars pyramid
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
"""
"""
n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
"""
"""
n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
print()
"""
"""
n=int(input())
for i in range(0,n):
    for j in range(0,n):
        print(i+j,end=" ")
    print()
"""
"""
n=int(input())
for i in range(1,n+1):
    for j in range(n,0,-1):
        print(j,end=" ")
    print()
"""
"""
n=int(input())
for i in range(1,n+1):
    if i%2==0:
        for j in range(n,0,-1):
            print(j,end=" ")
        print()
    else:
        for j in range(1,n+1):
            print(j,end=" ")
        print()
"""
"""
n=int(input())
s=5
for i in range(1,n+1):
   for j in range(1,n+1): 
        if i%2==1:
            print(j,end=" ")
        else:
            print(j,end=" ")
            s=s-1
   s=5
   print()
"""

"""
n=int(input())
for i in range(1,n+1):
    for j in range(n,0,-1):
        if i%2==1:
            print(j,end=" ")
        if i%2==0:
            print(i,end=" ")
    print()
"""
"""
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()
"""

"""
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j%2==0:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()
"""
""" 7
n=int(input())
for i in range(1,n+1):
    if i%2!=0:
        for j in range(1,n+1):
            if j%2==0:
                print(0,end=" ")
            else:
                print(1,end=" ")
        print()
    else:
         for j in range(1,n+1):
            if j%2==0:
                print(1,end=" ")
            else:
                print(0,end=" ")
         print()
"""
"""
n=int(input())
for i in range(1,n+1):
    for s in range(n,i,-1):
        print(" " ,end=" ")
    
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""
"""
n=int(input())
for i in range(1,n+1):
    for s in range(2,i+1):
        print(" ",end=" ")
    for j in range(n+1,i,-1):
        print("*",end=" ")
    print()
"""
"""
n=int(input())
for i in range(1,n+1):
    for s in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    """
"""
n=int(input())
for i in range(n,0,-1):
    t=i
    for s in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(t,end=" ")
        t-=1
    print()
"""
"""
n=int(input())
for i in range(1,n+1):
    for s in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    print()
"""
"""
n=int(input())
for i in range(1,n+1):
    for s in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print(i,end=" ")
    print()
"""
"""
n=int(input())
for i in range(1,n+1):
    for s in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print(j,end=" ")
    print()
"""
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
"""


'''
def total_marks(n,data):
    res=0
    for i in data:
        res+=i
        return res

n=int(input())
data=list(map(int,input().split())
total=total_marks(n,data)
          print(total)
'''
'''
def evenodd(n,data):
    ec,oc=0,0
    for i in data:
        if i%2==0:
            ec+=1
        else:
            oc+=1
    return ec,oc
n=int(input())
data=list(map(int,input().split()))
total=evenodd(n,data)
print(*total)
##for i in total
##print(total,end=" ")
'''
'''
import math as m
def isprime(n):
    s=int(m,sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return 0
    return 1
def countprime(n,data):
    pc=0
    for i in data:
        if isprime(i):
            pc+=1
    return pc
n=int(input())
data=list(map(int,input().split()))
pc=countPrimes(n,data)
print(pc)
'''
'''
import math as m
def isprime(n):
    if num==1:
        return 0
    s=int(m.sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return 0
    return 1
def findPrimes(n,data):
    m=[]
    for i in data:
        if isprime(i):
            m.append(i)
    return m
n=int(input())
data=list(map(int,input().split()))
primes=findPrime(n,data)
print(*prime)
'''
'''
import math as m
def isprime(n):
    if num==1:
        return 0
    s=int(m.sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return 0
    return 1
def findPrimes(n,data):
    prime=[]
    nonprimes=[]
    for i in data:
        if isprime(i):
            prime.append(i)
        else:
            nonprimes.append(i)
    return prime,nonprimes
n=int(input())
data=list(map(int,input().split()))
primes,nonprimes=findPrimes(n,data)
print(*primes)
print(*nonprimes)

'''
'''
def sum(n):
    s=0
    while True:
        r=n%10
        n=n//10
        s=s+r
    return s

def sumofdigits(n,data):
    for i in range(len(data)):
        data[i]=sum(data[i])
n=int(input())
data=list(map(int,input().split()))
sumofdigits=findPrime(n,data)
print(*data)
'''


#reverse of a number in list
#count of palindromes in list

'''
import math
def reverse(n):
    s=0
    while True:
        r=n%10
        n=n//10
        s=s*10+r
    return s
def sumofdigits(n,data):
    for i in range(len(data)):
        data[i]=sum(data[i])
    return data
n=int(input())
data=list(map(int,input().split()))
sumofdigits(n,data)
print(*data)
'''

'''
import math
def palindrome(n):
    m=n
    s=0
    while True:
        r=n%10
        n=n//10
        s=s*10+r
    return s==m
def sumofdigits(n,data):
    c=0
    for i in range(len(data)):
        if palindrome(data[i]):
            c+=1
    return c
n=int(input())
data=list(map(int,input().split()))
sumofdigits(n,data)
print(*data)

'''





























