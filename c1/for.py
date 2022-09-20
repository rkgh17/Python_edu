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


for i in range(10): #for i in range(0,10,1)
    print(i)

for i in range(10,4,-1):
    print(i)