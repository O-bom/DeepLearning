print("파이썬 리스트를 사용한 연산:")
a = [1,2,3]
b = [4,5,6]
print("a+b:", a+b)
try:
    print(a+b)
except TypeError:
    print("a+b 파이썬 리스트에 대해 a+b와 같은 연산을 할 수 없음")

import numpy as np
print()
print("넘파이 배열을 사용한 연산:")
a = np.array([1,2,3])
b = np.array([4,5,6])
print("a+b:", a+b)

a = np.array([[1,2,3],
              [4,5,6]])
b = np.array([10,20,30])
c = np.array([1, 3, 5])
d = np.array([3])
print('a:')
print(a)
print('a.sum(axis=0):', a.sum(axis=0))
print('a.sum(axis=1):', a.sum(axis=1))
print("a+b:\n", a+b)
print("a*b:", a*b)
print("c+d:\n", c+d)
print("c*d:\n", c*d)