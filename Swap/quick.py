# -*- coding:utf-8 -*-
from utils import *

def  quick_core(raw_list, low, high):

    if low>=high:
        return
    left=low
    right=high
    key=raw_list[left]
    while left<right:
        while left<right and raw_list[right]>=key:
            right-=1
        raw_list[left]=raw_list[right]
        while left<right and raw_list[left]<=key:
            left+=1
        raw_list[right]=raw_list[left]
    raw_list[left]=key
    quick_core(raw_list, low, left - 1)
    quick_core(raw_list, left + 1, high)

@performance
def quick_sort(raw_list):
    len_raw = len(raw_list)
    quick_core(raw_list,0,len_raw-1)

