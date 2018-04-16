def flip_dict_of_lists(d):    
    rang = []
    for k in d:
        for s in d[k]:
            if s not in rang:
                rang.append(s)
    flip_dic = {}
    for l in rang:
        for s in d:
            if l in d[s]:
                if l not in flip_dic:
                    flip_dic[l] = [s]
                else:
                    flip_dic[l].append(s)
    return flip_dic