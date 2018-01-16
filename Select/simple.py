from utils import  *

# raw_list=[9,1,2,5,7,4,8,6,3,5]
#[1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

@performance
def  simple_sort(raw_list):
    len_list=len(raw_list)
    for i  in  range(len_list):
        cur_min = raw_list[i]
        min_index = i
        for j in range(i+1,len_list):
            if raw_list[j]<cur_min:
                cur_min=raw_list[j]
                min_index=j
        if min_index!=i:
            raw_list[i],raw_list[min_index]=raw_list[min_index],raw_list[i]
    return  raw_list

@performance
def  simple_sort1(raw_list):
    len_list=len(raw_list)
    for i  in  range(len_list):
        index = i
        for j in range(i+1,len_list):
            if raw_list[j]<raw_list[index]:
                index=j
        if index!=i:
            raw_list[i],raw_list[index]=raw_list[index],raw_list[i]
    return  raw_list


