import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
print('\n')
print(np.shape(a)) # 3행 4열
a.shape=(6,2) # 6행 2열로 변경 - 행열의 곱이 같아야함
print('\n')
print(a)