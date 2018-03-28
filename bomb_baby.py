def answer(M, F):
    m = int(M)
    f = int(F)
    
    gen = 0
   
    while m>1 and f>1:
        if m>f:
            gen += m//f
            m = m % f
        if f>m:
            gen += f//m
            f = f%m
           
    if m == 1:
        return str(gen + f - 1)
    if f == 1:
        return str(gen + m - 1)
    return "impossible"