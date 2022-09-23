"""
https://076923.github.io/posts/Python-numpy-1/
-넘파이 강의
"""
import numpy as np
a=[1,2,3,4,5] #파이썬 리스트
b=np.array(a) #넘파이 리스트 -> ,가 없음
c=np.array([1,3,5])
print(a)
print(b)
print(c)

a=np.array([1,2,3,4,5])
b=a
c=a.copy() # 새로운 객체 생성

b[0]=99
print(a)
print(b) # 원본을 수정해도 같이 수정됨
print(c) # 새로운 객체 생성

print(b[2])
print(a[2])
print(c[-1])
print(c[0:2])

a = [1, 2, 3, 4, 5]
b = np.array(a)
c = np.array([1, 3, 5])

print(a*2) # 파이썬 리스트에 * n = n번 반복
print(b*2) # 값들을 2배씩 곱함
print(c+3) # 값마다 3씩 더함

