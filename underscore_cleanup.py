def underscore_cleanup(string):
    out = ""
    string = string +"?"
    i = 0
    while i < len(string):
        if string[i] != "_":
            out+= string[i]
        else:
            j = 1
            while string[i+j] == "_":
                j+=1
            out += "_"
            i += j-1
        i+=1
    return out[:-1]
