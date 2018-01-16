# -*- coding:utf-8 -*-
from utils import  *

def  merge_core(raw_list, left, middle, right):
    i=left
    j=middle+1
    tmp_list=[]
    while i<middle+1 and j<right+1:
        if raw_list[i]<raw_list[j]:
            tmp_list.append(raw_list[i])
            i+=1
        else:
            tmp_list.append(raw_list[j])
            j+=1
    while i<middle+1:
        tmp_list.append(raw_list[i])
        i+=1
    while j<right+1:
        tmp_list.append(raw_list[j])
        j+=1
    len_tmp=len(tmp_list)
    for i  in range(len_tmp):
        raw_list[left+i]=tmp_list[i]

def  merge_main(raw_list, left, right):
    if left<right:
        middle=(left+right)//2
        merge_main(raw_list, left, middle)
        merge_main(raw_list, middle + 1, right)
        merge_core(raw_list, left, middle, right)

@performance
def merge_sort(raw_list):
    len_raw=len(raw_list)
    merge_main(raw_list, 0, len_raw - 1)
