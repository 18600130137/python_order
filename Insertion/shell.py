from utils import  *
# raw_list=[9,1,2,5,7,4,8,6,3,5]
#[1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

@performance
def   shell_sort(raw_list):
    len_raw=len(raw_list)
    gap=len_raw//2
    while  gap>=1:
        for i  in   range(gap,len_raw):
            if raw_list[i]<raw_list[i-gap]:
                tmp=raw_list[i]
                j=i-gap
                while j>=0 and tmp<raw_list[j]:
                    raw_list[j+gap]=raw_list[j]
                    j-=gap
                raw_list[j+gap]=tmp

        gap=gap//2
    return  raw_list
