def with_previous(it, fill_value= None):
    answer = []
    if not it:
        return []
    iterator = iter(it)
    prev_value = fill_value
    current_value = next(iterator)
    
    for i in range(len(it)-1):
        answer.append((current_value,prev_value))
        prev_value = current_value
        current_value = next(iterator)
    answer.append((current_value,prev_value))
    return answer 
    