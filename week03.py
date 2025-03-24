# groups = ['HOT','Seventeen', 'Black Pink',"NJZ"]
# #ratings = [1,2,4,3,100]
# ratings = [1,2,4,3]
#
# groups_rating = list(zip(groups, ratings)) # zip 함수
# print(groups_rating)

def duplicate_city(cities):
    result = list()
    s = set()

    for city in cities:
        l1 = len(s)
        s.add(city)
        l2 = len(s)
        if l1 == l2: # 중복 값이 들어온 경우
            result.append(city)

    return result






cities =['Incheon','Incheon','Incheon','Gimpo','Seoul','Seoul']
# cities = {'Incheon','Incheon','Incheon','Gimpo','Seoul','Seoul'}
cities.append('Anyang')
cities.append('Seoul')
print(cities)
print(set(duplicate_city(cities)))