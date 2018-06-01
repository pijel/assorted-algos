def compress(string):
    if not string:
        return 
    last_char = None
    string = string + " "
    out = ""
    i = 0
    while i < len(string)-1:
        count = 0
        last_char = string[i]
        while string[i] == last_char:
            i+=1
            count += 1
            
        
        if count > 1:
            out += last_char + str(count)
        else:
            out += last_char
            
    return out
        