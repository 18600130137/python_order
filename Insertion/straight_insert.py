from utils import  *


# raw_list=[9,1,2,5,7,4,8,6,3,5]
@performance
def   straight_insert_sort(raw_list):
    len_list=len(raw_list)
    for i in  range(1,len_list):
        if raw_list[i]<raw_list[i-1]:
            tmp=raw_list[i]
            j=i-1
            while j>=0 and tmp<raw_list[j]:
                raw_list[j+1]=raw_list[j]
                j-=1
            raw_list[j+1]=tmp
    return raw_list

