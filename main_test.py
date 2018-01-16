from  utils import *
#插入排序
from  Insertion.straight_insert import straight_insert_sort
from  Insertion.shell import shell_sort

##比较排序
from Select.simple import simple_sort
from Select.simple import simple_sort1
from Select.heap import heap_sort

##交换排序
from Swap.bubble import bubble_sort
from Swap.quick import quick_sort

##其它排序
from  Other.merge import merge_sort
from  Other.radix import radix_sort

@performance
def sys_oder(raw_list):
    return sorted(raw_list)

if __name__=='__main__':
    random_list=random_array(1e4)
    #系统排序
    sys_oder(random_list.copy())

    #插入排序
    straight_insert_sort(random_list.copy())
    shell_sort(random_list.copy())

    #比较排序
    simple_sort(random_list.copy())
    simple_sort1(random_list.copy())
    heap_sort(random_list.copy())

    ##交换排序
    bubble_sort(random_list.copy())
    quick_sort(random_list.copy())

    ##其它排序
    merge_sort(random_list.copy())
    radix_sort(random_list.copy())

##1e4
# call random_array() in 0.000000s
# call sys_oder() in 0.003006s
# call straight_insert_sort() in 7.670425s
# call shell_sort() in 0.083223s
# call simple_sort() in 5.030348s
# call simple_sort1() in 8.723427s
# call heap_sort() in 0.100069s
# call bubble_sort() in 16.564174s
# call quick_sort() in 0.045148s
# call merge_sort() in 0.097233s
# call radix_sort() in 0.037338s
