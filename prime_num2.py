
def isprime(n):
    if n<=1:
        return False
    
    
    c=2
    while c*c<=n:
        if n%c==0:
            return False
        
        c+=1
        
    return True

    
    
    




def printingprime(n):
    
    
    for i in range(1,n+1):
        if isprime(i)==True:
            
            print(i)
            
            
n=40

printingprime(40)
    
    