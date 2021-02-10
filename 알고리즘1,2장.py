'''
+와 -를 번갈아 출력하기
'''

# print('+와 -를 번갈아 출력합니다.')
# n = int(input('몇 개를 출력할까요?: '))

# for _ in range(n//2):
#     print("+-", end='')

# if n%2 :
#     print('+', end='')

# print()

'''
*를 n개 출력하되 w개마다 줄바꿈하기
print('*를 출력합니다.')
'''

# n = int(input('몇개를 출력할까요?: '))
# w = int(input("몇개마다 줄바꿈할까요?: "))

# for i in range(n):
#     print('*', end='')
#     if i%w == w-1:
#         print()

# if n%w:
#     print()

# for _ in range(n//w):
#     print('*'*w)

# rest = n%w
# if rest:
#     print('*'*rest)

'''
가로, 세로 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열
'''
# # 101 단계 수행
# area = int(input('직사각형의 넓이를 입력하세요: '))

# for i in range(1,area+1):
#     n = area/i
#     if area%i == 0 and i <= n:
#         print(f"{i} X {int(n)} = {area}")

# 24단계 수행
# area = int(input('직사각형의 넓이를 입력하세요: '))

# for i in range(1,area+1):
#     if i*i > area:
#         break
#     elif area%i:
#         continue
#     else:
#         print(f"{i} X {area//i} = {area}")

"""
5줄에 *을 이등변 삼각형으로 출력(for문 사용)
"""
# 46단계 수행

# for i in range(5):
#     for j in range(i+1):
#         print("*", end='')
#     print()

"""
5줄에 *을 이등변 삼각형으로 출력(while문 사용)
"""
# # 18단계 수행

# # i=0
# # while True:
# #     i += 1
# #     print("*"*i)
# #     if i == 5:
# #         break

"""
5줄에 *을 오른쪽이 직각인 이등변 삼각형으로 출력
"""

# for i in range(5):
#     for _ in range(5-i-1):
#         print(" ", end="")
#     for _ in range(i+1):
#         print("*", end='')
#     print()

"""
시퀀스 원소의 최댓값 출력
"""
# from typing import Any, Sequence

# def max_of(a: Sequence) -> Any:
#     maximum = a[0]
#     for i in range(1, len(a)):
#         if a[i] > maximum:
#             maximum = a[i]
#     return maximum

# if __name__=='__main__':
#     print("배열의 최댓값을 구합니다.")
#     num = int(input("원소 수를 입력하세요: "))
#     x = [None] * num
    
#     for i in range(num):
#         x[i] = int(input(f"x[{i}]값을 입력하세요: "))

#     print(f"최댓값은 {max_of(x)}입니다.")


# from typing import Any, Sequence

# def max_of(a: Sequence) -> Any:
#     maximum = a[0]
#     for i in range(1, len(a)):
#         if a[i] > maximum:
#             maximum = a[i]
#     return maximum

# if __name__=='__main__':
#     print("배열의 최댓값을 구합니다.")
#     x = (172,153,192,140,165)

#     print(f"최댓값은 {max_of(x)}입니다.")

"""
위 코드를 모듈로 만들어 사용할 시,
배열의 원솟값을 난수로 결정하기
"""

# from typing import Any, Sequence
# import random

# def max_of(a: Sequence) -> Any:
#     maximum = a[0]
#     for i in range(1, len(a)):
#         if a[i] > maximum:
#             maximum = a[i]
#     return maximum

# print('난수의 최댓값을 구합니다.')
# num = int(input('난수의 개수를 입력하세요: '))
# lo = int(input('난수의 최솟값을 입력하세요: '))
# hi = int(input('난수의 최댓값을 입력하세요: '))
# x = [None] * num

# for i in range(num):
#     x[i] = random.randint(lo,hi)

# print(f'{x}')
# print(f'이 가운데 최댓값은 {max_of(x)}입니다.')

"""
각 배열 원수의 최댓값을 구해서 출력하기(튜플, 문자열, 문자열리스트)
"""

# t = (4,7,5.6,2,3.14,1)
# s = 'string'
# a = ['DTS','AAC','FLAC']

# print(f'{t}의 최댓값은 {max_of(t)}입니다.')
# print(f'{s}의 최댓값은 {max_of(s)}입니다.')
# print(f'{a}의 최댓값은 {max_of(a)}입니다.')

"""
동일성(Identity) 판단
"""
# 같은 값을 가지고 있는 리스트지만 ID는 다름(즉, 서로 다른 객체)
# lst1 = [1,2,3,4,5]
# lst2 = [1,2,3,4,5]
# print(id(lst1))
# print(id(lst2))
# print(lst1 is lst2) #False

# 같은 리스트 객체를 바라보는 경우
# lst1 = [1,2,3,4,5]
# lst2 = lst1
# print(lst1 is lst2) #True

# print(id([1,2,3,4,5]))
# print(id(lst1))
# print(id(lst2))

# # 리스트 수정이 일어나도!?

# lst1[2] = 9
# print(lst1)
# print(lst2)
# print(id(lst1))
# print(id(lst2))

# int 경우 
# a = 1
# b = 1
# print(a)
# print(b)
# print(id(a))
# print(id(b))
# print(id(1))
# print(a is b)

#tuple 경우
# a = (1,2)
# b = (1,2)

# print(id(a))
# print(id(b))
# print(id((1,2)))
# print(a is b)

"""
리스트, 튜플 스캔 - 4가지 방법
"""
#리스트의 모든 원소를 스캔(원소수 미리 파악)

# x = ['John', 'George', 'Paul', 'Ringo']

# for i in range(len(x)):
#     print(f"x[{i}] = {x[i]}")

# enumerate() 함수 사용

# for i, name in enumerate(x):
#     print(f"x[{i}] = {name}")

# enumerate() 함수 사용2(start를 1부터 지정하여 시작)

# for i, name in enumerate(x, 1):
#     print(f'{i}번째 = {name}')

# 리스트의 모든 원소 스캔(인덱스값 사용 X)

# for i in x:
#     print(i)

"""
iter()와 next()를 이용한 스캔
"""

# x = ['John', 'George', 'Paul', 'Ringo']
# x = iter(x)
# print(next(x))  #John
# print(next(x))  #George
# print(next(x))  #Paul
# print(next(x))  #Ringo
# print(next(x))  #StopIeration 에러 발생

'''
배열 원소의 역순 정렬 알고리즘 구현
'''

# from typing import Any, MutableSequence

# def reverse_array(a: MutableSequence) -> None:
#     #뮤터블 시퀀스 a의 원소를 역순으로 정렬

#     n= len(a)
#     for i in range(n//2):
#         a[i] , a[n-i-1] = a[n-i-1], a[i]

# if __name__ == "__main__":

#     x = [2,5,1,3,9,6,7]

#     reverse_array(x)
#     print(x)

"""
역순정렬 함수 reverse(), reversed()
"""
# # reverse는 리스트를 역순 정렬(리스트 수정)
# x = [1,2,3,4,5,6,7]
# print(id(x))

# x.reverse()
# print(id(x))
# print(x)

# # reversed는 역순으로 정렬한 새로운 객체 생성하여 반환
# x = [1,2,3,4,5,6,7]
# print(id(x))

# print(id(list(reversed(x))))
# print(list(reversed(x)))

# print(id(x))

# # 따라서 이뮤터블 객체에도 사용 가능
# x = (1,2,3,4,5,6,7)
# print(id(x))

# print(id(list(reversed(x))))
# print(list(reversed(x)))

# print(id(x))

"""
immutable과 mutable 자료형
"""

# immutable: int

# a = 1
# print(id(a))
# print(id(1))

# a += 1
# print(a)
# print(id(a))
# print(id(1))
# print(id(2))

# immutable: stirng

# a = 'a'
# print(id(a))
# print(id('a'))

# a += 'b'
# print(a)
# print(id(a))
# print(id('a'))
# print(id('ab'))
# print(id('a'+'b'))


# immutable: tuple

# a = (1,)
# print(id(a))
# print(id((1,)))

# a += (2,)
# print(a)
# print(id(a))
# print(id((1,2)))

# mutable : list

# a = [1]
# print(id(a))
# print(id([1]))

# a.append(2)
# print(a)
# print(id(a))
# print(id([1,2]))

# b = a
# b.append(3)
# print(a)
# print(b)
# print(id(a))
# print(id(b))
# print(id([1,2,3]))

# mutable: dictionary

# a = {1:'a'}
# print(id(a))
# print(id({1:'a'}))

# a[2] = 'b'
# print(a)
# print(id(a))
# print(id({1:'a',2:'b'}))

# b = a 
# b[3] = 'c'
# print(a)
# print(b)
# print(id(a))
# print(id(b))
# print(id({1:'a',2:'b',3:'c'}))

"""
함수사이에 인수 주고 받기
"""

# 인수가 int(immutable)인 경우

# def sum_of(n):
#     print(id(n))
#     s = 0
#     while n > 0:
#         s += n
#         print(n)
#         print(id(n))
#         n -= 1
#     return s

# print(sum_of(5))

# 인수가 list(mutable)인 경우

# def change(l,i,val):
#     print(id(l))
#     l[i] = val
#     print(id(l))
#     return l

# l = [1,2,3,4,5]
# change(l,2,33)
# print(l)
# print(id(l))

"""
1000이하의 소수 나열
"""

# 첫번째 방법

# counter = 0

# for n in range(1,1001):
#     for i in range(2,n):
#         counter += 1
#         if n%i == 0:
#             break
#     else:    
#         print(n)

# print(f"총 연산횟수: {counter}")

# 알고리즘 개선 버전 1

# counter = 0
# ptr = 0
# prime = [None]*500

# prime[ptr] = 2
# ptr += 1

# for n in range(3,1001,2):
#     for i in range(1, ptr):
#         counter += 1
#         if n%prime[i] == 0:
#             break
#     else:
#         prime[ptr] = n
#         ptr += 1

# for i in range(ptr):
#     print(prime[i])

# print(f"총 연산횟수: {counter}")



# n=1000
# a = [False,False] + [True]*(n-1)
# primes=[]

# for i in range(2,n+1):
#   if a[i]:
#     primes.append(i)
#     for j in range(2*i, n+1, i):
#         a[j] = False
# print(primes)


# 알고리즘 개선 2

# counter = 0
# ptr = 0
# prime = [None]*500

# prime[ptr] = 2
# ptr += 1

# prime[ptr] = 3
# ptr += 1

# for n in range(5,1001,2):
#     i = 1
#     while prime[i]*prime[i] <= n:
#         counter += 2
#         if n%prime[i] == 0:
#             break
#         i += 1
#     else:
#         prime[ptr] = n
#         ptr += 1
#         counter += 1
    
# for i in range(ptr):
#     print(prime[i])

# print(f"총 연산횟수: {counter}")
