# 배열 정리

# 배열 만들기

# import  array # 넘파이 패키지
#
# arr = array.array('f',(1.0,1.5,2.0,2.5))
# print(arr[1]) # 1.5


# import array # 넘파이 패키지
#
# arr = array.array('f',(11,9,-77,8))
#
# for i in range(len(arr)):
#     print(f'{arr[i]:3}{id(arr[i])}')

# array = [11,9,-77,8]
# for i in range(len(array)):
#     print(f"{array[i]:3} {id(array[i])}")

# 0 옮기기

# def move_zero(a_list):
#
#     zeroIndex = 0
#
#     for index, v in enumerate(a_list):
#         if v !=0:
#             a_list[zeroIndex] = v
#
#             if zeroIndex != index:
#                 a_list[index] = 0
#
#             zeroIndex+=1
#
#     return (a_list)
#
# a_list = [5,0,8,0,11]
# move_zero(a_list)
# print(a_list)

# enumerate 사용하지 않고 0 옮기기

# def move_zero(a_list):
#
#     zero_Index = 0
#
#     for i in range(len(a_list)):
#         v = a_list[i]
#         if v != 0:
#             a_list[zero_Index] = v
#
#             if zero_Index != i:
#                 a_list[i] = 0
#
#             zero_Index+=1
#
#     return (a_list)
#
# a_list = [5,0,8,0,11]
# move_zero(a_list)
# print(a_list)

# l = [11, 9, -77, 8]
# for i, v in enumerate(l):
#     print(i, v)
#
# l = [11, 9, -77, 8]
# for i in range(len(l)):
#     print(i, l[i])

# # 리스트의 결합
# movie_list = ["Interstellar","Inception","The Prestige","Insomnia","Betman Begins"]
# ratings_list = [1,10,10,8,6]
#
# print(list(zip(movie_list,ratings_list)))
#
# groups = ['HOT','Seventeen','Black Pink',"NJZ"]
# ratings = [1,2,4,3,100]
# #ratings = [1,2,4,3]
# print(list(zip(groups,ratings)))
#

# 중복 요소 찾기

# a_set = set()
# a_set.add("Kanye West")
# a_set.add("Kanye West")
# a_set.add("Kendall Jenner")
# a_set.add("Justin Bieber")
# print(a_set)

# # city = ['Incheon','Incheon','Incheon','Gimpo','Seoul']
# # # city = {'Incheon', 'Incheon', 'Incheon', 'Gimpo', 'Seoul', 'Seoul'}
# # city = set(city)
# # print(city)

# 리스트에 중복이 있는지 확인하는 함수

# def return_dups(an_interable):
#     dups = []
#     a_set = set()
#
#     for item in an_interable:
#         l1 =len(a_set)
#         a_set.add(item)
#         l2 = len(a_set)
#
#         if l1 == l2:
#             dups.append(item)
#
#     return dups
#
# a_list = ["Susan Adams","Kwame Goodall","Jill Hampton","Susan Adams"]
# dups = return_dups(a_list)
# print(dups)

# def duplicate_city(cities):
#     result = list()
#     s = set()
#
#     for city in cities:
#         l1 = len(s)
#         s.add(city)
#         l2 = len(s)
#
#         if l1 == l2:
#             result.append(city)
#
#     return result
#
# cities = ['Incheon', 'Incheon', 'Incheon', 'Gimpo', 'Seoul', 'Seoul']
# cities.append('Anyang')
# cities.append('Seoul')
# print(cities)
# print(set(duplicate_city(cities)))

# 두 리스트의 교집합 찾기

# def return_inter(list1, list2):
#     list3 = [v for v in list1 if v in list2]
#     return list3
#
# list1 = [2,43,48,62,64,28,3]
# list2 = [1,28,42,70,2,10,62,31,4,14]
#
# print(return_inter(list1,list2))

# def intersection(l1,l2):
#     l3 = list()
#     for v in l1:
#         if v in l2:
#             l3.append(v)
#
#     return l3
#
# l1 = [45, 5, 22, 31, 7, 19]
# l2 = [2, 1, 5, 22, 7, 38, 27, 19, 13, 41]

# print(intersection(l1,l2))

# def return_inter(list1, list2):
#     set1 = set(list1)
#     set2 = set(list2)
#     return list(set1 .intersection((set2)))
#
# list1 = [2,43,48,62,64,28,3]
# list2 = [1,28,42,70,2,10,62,31,4,14]
#
# print(return_inter(list1,list2))

# def inters(l1,l2):
#     s1 =set(l1)
#     s2 =set(l2)
#     return list (s1&s2)
# l1 = [45, 5, 22, 31, 7, 19]
# l2 = [2, 1, 5, 22, 7, 38, 27, 19, 13, 41]
#
# print(inters(l1,l2))