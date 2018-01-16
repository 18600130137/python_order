# -*- coding:utf-8 -*-
from  utils import *

@performance
def   radix_sort(raw_list):
    d=0
    base=1
    for i  in raw_list:
        while base<i:
            base*=10
            d+=1
    box=[]
    for i in range(10):
        box.append([])

    for i  in range(0,d):
        div=10**i
        for i in raw_list:
            index=i//div%10
            box[index].append(i)
        raw_list=[]
        for i  in  range(10):
            if len(box[i])>0:
                raw_list.extend(box[i])
                box[i]=[]
    return  raw_list
