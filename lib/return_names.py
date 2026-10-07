def return_names(list):
    if len(list) == 2:
        return f"{list[0]} & {list[1]}"
    elif len(list) ==1:
        return f"{list[0]}"
    elif len(list) == 0:
        return ""
    else:
        name_list = []
        list_length = len(list)
        for x in range(0,list_length-1):
            name_list.append(list[x])
        
        result = ", ".join(name_list)
        return result + f" & {list[-1]}"
    


return_names(['tisha','jon','fictional_friend'])