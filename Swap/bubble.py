from utils import  *

@performance
def   bubble_sort(raw_list):
    len_list=len(raw_list)
    for i  in range(len_list):
        for j in range(1,len_list-i):
            if raw_list[j]<raw_list[j-1]:
                raw_list[j-1],raw_list[j]=raw_list[j],raw_list[j-1]
    return raw_list



