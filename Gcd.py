

def Gcd(a,b):
    if b==0:
        return a
    
    return Gcd(b,a%b)



print(Gcd(12,15))