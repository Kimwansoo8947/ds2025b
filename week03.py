# 3주차 배열
import array

arr = array.array ('f' ,[11,9,-77,8]) # 파이썬은 배열 개념이 없음

for i in range(len(arr)):
    print(f"{arr[i]:3}{id(arr[i])}")
