def longestsub(s):
    current_string = ""
    max_ending_here = 0
    true_max = 0
    
    for i in range(len(s)):
        
        if s[i] not in current_string:
            max_ending_here +=1
            current_string += s[i]
            
        else:
            current_string = s[i]
            max_ending_here = 1
            for k in range(i-1,-1,-1):
                if s[k] not in current_string:
                    current_string = s[k] + current_string
                    max_ending_here +=1
                else:
                    break
                        
        if max_ending_here >= true_max:
                true_max = max_ending_here
        
        
    return true_max