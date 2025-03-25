# 1차원 배열
# 파이썬은 배열은 존재하지 않다.

# 배열 만들기

# multi_array = [[1,2,3],[4,5,6],[7,8,9]]
# print(multi_array[1][2])

# array = [11,9,-77,8]
#
# for i in range(len(array)): # i=0부터 길이는 4 따라서 4가 되기 전까지
#     print(f"{array[i]:3} {id(array[i])}")

# import array
#
# arr = array.array('f',[11,9,-77,8])
# for i in range(len(arr)): # arr의 길이는4
#     print(f"{arr[i]:3} {id(arr[i])}")

# import array
#
# arr = array.array('f',(1.0,1.5,2.0,2.5))
# print(arr[1])

# # 0 옮기기
# def move_zeros(a_list):
#     zero_index = 0;
#     for index, n in enumerate(a_list):
#         if n!=0:
#             a_list[zero_index] = n
#
#             if zero_index != index:
#                 a_list[index] = 0
#             zero_index+=1
#
#     return (a_list)
#
# a_list = [8,0,3,0,12]
# move_zeros(a_list)
# print(a_list)

# 0 옮기기 enumerate 사용하지 않고

# def move_zeros(a_list):
#     zero_index = 0
#
#     for i in range(len(a_list)):
#
#         n=a_list[i] # 현재 index i의 값을 n에 저장
#         if n!=0:
#             a_list[zero_index] = n
#             if zero_index != i:
#                 a_list[i] =0
#
#             zero_index+=1
#
#     return (a_list)
#
# a_list = [8,0,3,0,12]
# move_zeros(a_list)
# print(a_list)

#  enumerate 사용하지 않고 index랑 value를 뽑는 법 (교수님)
# import array
# def move_zero(l):
#
#     zero_idx = 0
#     for i in range(len(l)):
#
#         n =l[i] # value = l[i]
#         if n !=0:
#             l[zero_idx] = n
#
#             if zero_idx != i:
#                 l[i] = 0
#
#             zero_idx+=1
#
#     return 1
#
# l = [11,0,9,0,-77]
# move_zero(l)
# print(l)

# 리스트의 결합

# movie_list = ["Interstellar","Inception","The Prestige","Insomia","Batman Begins"]
# rating_list = [1,10,10,8,6]
# # zip은 튜플 튜플은 값을 추가 또는 삭제할 수 없는 불변의 자료구조
# print(list(zip(movie_list,rating_list)))
#
# groups = ['HOT','Seventeen','Black Pink','NJZ']
# ratings = [1,2,4,3,100]
# #ratings = [1,2,4,3,100] # ratings의 길이가 groups 보다 길다면 초과된 값은 무시된다.
#
# group_rating = list(zip(groups,ratings)) # 튜플 타입을 리스트로 묶음
# print(group_rating)


# 중복 요소 찾기
# a_set = set()
# a_set.add("Kanye West")
# a_set.add("Kanye West") # 중복
# a_set.add("Kendall Jenner")
# a_set.add("Justin Bibber")
# print(a_set)

# city = ['Incheon','Incheon','Incheon','Gimpo','Seoul','Seoul']
# cit = set(city)
# print(city)

# 세트르 시용해 리스트에 중복이 있는지 확인

# def return_dups(an_iterable):
#     dups = []
#     a_set = set()
#
#     for item in an_iterable:
#         l1 = len(a_set)
#         a_set.add(item)
#         l2 = len(a_set)
#
#         if l1 == l2:  #세트의 길이가 그대로이면 요소가 중복임
#             dups.append(item)
#     return dups
#
# a_list = ["Susan Adams","Kawme Goodall", "Jill Hampton","Susan Adams"]
#
# dups = return_dups(a_list)
# print(dups)

# 교집합 찾기

# def return_inter(list1, list2):
#     list3 =[v for v in list1 if v in list2]  # list1의 각 요소 v가 list2에 존재하면 list3에 추가
#     return list3
#
# list1 = [2,43,48,62,64,28,3]
# list2 = [1,28,42,70,2,10,62,31,4,14]
# print(return_inter(list1,list2))


# def return_inter(list1, list2):
#    set1 = set(list1)
#    set2 = set(list2)
#
#    return list(set1.intersection((set2)))
#
# list1 = [2,43,48,62,64,28,3]
# list2 = [1,28,42,70,2,10,62,31,4,14]
# new_list = return_inter(list1,list2)
# print(new_list)

# cities = ['Incheon','Incheon','Incheon','Gimpo','Seoul','Seoul']
# cities.append('Anyang')
# cities.append('Seoul')
# print(cities)



# def intersection(l1,l2):
#     l3 =list() # 중복 된 데이터를 담을 리스트 생성
#     for v in l1:
#         if v in l2:
#             l3.append(v)
#
#     return l3
#
# def inters(l1,l2):
#     s1 = set(l1)
#     s2 = set(l2)
#     return list(s1 & s2)
#
# l1 = [45,5,22,31,7,19]
# l2 = [2,1,5,22,7,38,27,19,13,41]
# print(intersection(l1,l2))
# print(inters(l1,l2))

# 연습문제
an_array = [10,2,5,9,4]
arr1 =[]
arr2 = []
for i in range(len(an_array)):
    if an_array[i] % 2==0:
        arr1.append(an_array[i])
    else:
        arr2.append(an_array[i])

print(arr1)
print(arr2)