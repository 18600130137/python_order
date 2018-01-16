from utils import  *

# raw_list=[9,1,2,5,7,4,8,6,3,5]
#[1, 2, 3, 4, 5, 5, 6, 7, 8, 9]


def   heap_sort_ajust(raw_list, i, len_raw):
    child=2*i+1
    while child<len_raw:
        if child+1<len_raw and raw_list[child]<raw_list[child+1]:
            child+=1
        if raw_list[i]<raw_list[child]:
            raw_list[i],raw_list[child]=raw_list[child],raw_list[i]
            i=child
            child=2*i+1
        else:
            break
@performance
def  heap_sort(raw_list):
    len_raw=len(raw_list)
    for i  in range(len_raw//2-1,-1,-1):
        heap_sort_ajust(raw_list, i, len_raw)

    for i  in  range(len_raw-1,0,-1):
        raw_list[0],raw_list[i]=raw_list[i],raw_list[0]
        heap_sort_ajust(raw_list, 0, i)

