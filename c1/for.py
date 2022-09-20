"""
for 변수 in 리스트/튜플/딕셔너리/셋:
    실행문1
    ...
    실행문n
    continue/break
실행문

range(시작값, 종료값, 증감)
range(종료값) = range(0,종료값,1)
range(시작값, 종료값+1) = range(시작값, 종료값,1)
"""


# for i in range(10): #for i in range(0,10,1)
#     print(i)

# for i in range(10,4,-1):
#     print(i)

# for i in range(5):
#     for j in range(3):
#         print(i,j)

#1부터 100까지 합
# sum=0
# for i in range(101):
#     sum+=i
# print(sum)

# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)

# sum=0
# i=0
# while i<101:
#     sum+=i
#     i+=1
# print(sum)


# 구구단 2단부터 9단까지 출력
for i in range(2,10):
    for j in range(1,10):
        print(f'{i} * {j} = {i*j}')
    print()