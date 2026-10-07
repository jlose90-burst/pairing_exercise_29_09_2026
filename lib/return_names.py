def return_names(input_names):
    if type(input_names) != list:
        raise Exception("Please enter a list")

    all_strings = all(isinstance(x, str) for x in input_names)
    if not all_strings:
        raise TypeError("Please only give 1 list of strings")

    if len(input_names) == 2:
        return f"{input_names[0]} & {input_names[1]}"
    elif len(input_names) ==1:
        return f"{input_names[0]}"
    elif len(input_names) == 0:
        return ""
    else:
        name_list = []
        list_length = len(input_names)
        for x in range(0,list_length-1):
            name_list.append(input_names[x])
        
        result = ", ".join(name_list)
        return result + f" & {input_names[-1]}"
    


# print(return_names(['tisha','jon', ['fictional_friend',"3"]]))