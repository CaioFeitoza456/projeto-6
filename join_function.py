
from copy import deepcopy

def join_lists(list_a, list_b):
    
    copy_list_a = deepcopy(list_a)
    
    copy_list_a += list_b
    
    return copy_list_a
