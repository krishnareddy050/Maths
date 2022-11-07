

def squareroot(n,p):
    s=0
    
    end=n
    root=0.0
    
    while s<=end:
        mid=s+(end-s)//2                       #the complexity is simply O(log n) because we are using simple binary search
            
        
        if mid*mid==n:
            return mid
        
        if  mid*mid>n:
            end=mid-1
            
        else:
            s=mid+1
            
    incr=0.1      
    for i in range(1,p+1):
        while root*root<=n:         
            root+=incr
            
        root-=incr
        incr/=10
        
        
    return root
            
            
            
print(squareroot(10,3))
            
            
            
            