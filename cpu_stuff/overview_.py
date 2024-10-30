# import binary 
# from binary import BinaryUnits, DecimalUnits, convert_units
# res = convert_units(1024, BinaryUnits.TB, BinaryUnits.PB); print(res)
# # https://pypi.org/project/binary/


import time

import cachesimulator


# CPU's caches are Static RAM (SRAM) 
# while the RAM (8,16,32,...gb) is Dynamic RAM (DRAM)

## Task 1: simulate a CPU cache

# cache hit - when the data needed by the CPU is already in the cache
# cache miss - when the data needed is not in the cache 
## 100% cache hit is impossible because when we start our PC/laptop, caches are empty and need to load everything from main memory 

## Locality of Reference: LoR refers to the tendency of the computer program to access instructions whose addresses are near one another.
    ### Temoral Locality: once executed/accessed, a data element will be used again soon 
    ### Spacial Locality: neighbors of some data element will also be used soon (cuz they're close in the memory)

# one word (DWORD) which stands for "double word," which is a data type used in computer programming. Dwords are commonly used in operating systems and other low-level software applications for storing memory addresses, file sizes, and other types of numerical data.
## how does the CPU decides what neighbors to get from main memory in case of cache miss? it uses Word ID
# caches are made up of 'lines' and they store memory in a form of:
    # 1) tag - it's like the ID of a memory line; it identifies where the data came from
    # 2) data itself

operands_addresses = [0b0101, 0b1110, 0b0001, 0b0111, 0b1101]; print(isinstance(operands_addresses[0], int))
instruction_addresses = [0b1000, 0b1100] # + - 
print(type(instruction_addresses[0]))


caches = ['L1', 'L2', 'L3']
# l1_time = 0.1, l2_time=0.3, l3_time=0.5
# ram_time = 3.4

avail_data = dict(l1=[operands_addresses[0]], l2=operands_addresses[:2], l3=operands_addresses[1:])
print(avail_data)



for c_id, cache in enumerate(caches):
    pass




## subtask: calculate the time it takes to do everything
### calculate the miss/hit rate (hits/total_lookups)




### direct cache mapping










# FPGA: 



