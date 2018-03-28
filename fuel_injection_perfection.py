def newfuel(n):
    counter = 0
    
    while n!=1:
        if n%2 == 0:
            n = n//2
            counter +=1
        else:
            if n == 3:
                n = n-1
                counter +=1
            else:
                if bin(n)[-1] == '1' and bin(n)[-2] == '1':
                    n = n+1
                    counter +=1
                else:
                    n = n-1
                    counter +=1
    return counter