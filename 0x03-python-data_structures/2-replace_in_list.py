#!/usr/bin/python3
def replace_in_list, idx, lement):
    if idx < 0:
        return (my_list)
    elif idx >= len(my_list):
        return (my_list)
    else:
        for i in range(len(my_list)):
            if i == idx:
                del my_list[i]
                my_list.insert(idx, element)
                return (my_list)
            return (None)