def Gcd(a,b):               #this function will return the Gcd of a number
    
    if b==0:
        return a
    
    return Gcd(b,a%b)         




def Lcm(a,b):
    return  (a*b)//Gcd(a,b)     #the formula for lcm is a*b=lcm(a,b)*gcd(a,b)



print(Lcm(8,9))

