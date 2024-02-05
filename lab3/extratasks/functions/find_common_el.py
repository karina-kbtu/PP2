def find_common_el(list_1, list_2):
    common_list = []
    for el in list_1:
        if el in list_2:
            common_list.append(el)
    return common_list
list_1=[]
list_2=[]
print(find_common_el(list_1,list_2))
