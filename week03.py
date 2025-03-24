def move_zeros(a_list):
    zero_index = 0

    for index,  n in enumerate(a_list):
        if n != 0:
            a_list[zero_index] = n
            if zero_index != index:
                a_list[index] = 0
            zero_index += 1

    return (a_list)
a_list = [8,0,3,0,12]
move_zeros(a_list)
print(a_list)



# for i,v in enumerate(l): # unpacking
   # print(i,v)
# for i in enumerate(l): # packing
   #  print(i) # 인덱스랑 값을 동시에 리턴 (튜플)


# l = [11,9,-77,8]
# for i in range(len(l)):
    # print(i, l[i])
