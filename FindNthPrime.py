'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def isprime(n):
    l=[2]
    x=2
    while(len(l)!=n):
        x=x+1
        for i in range(2,x):
            if x%i==0:
                 break
        else:
             l.append(x)
            
    print(l[n-1])
    
    
    
isprime(200)
    
    