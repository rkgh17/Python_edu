"""
while 조건:
    실행문1
    ...
    실행문n
    continue/break
"""
i=0
while i<10:
    j=0
    while j<5:
        if j>3:
            break
        print(f'i : [{i}] j : [{j}]')
        j+=1
    i+=1
print('Program terminated')

"""
i=0
while i<10:
    j=0
    while j<5:
        if j>3:
            continue # 무한루프 -> control c
        print(f'i : [{i}] j : [{j}]')
        j+=1
    i+=1
print('Program terminated') 
"""

i=2
while i<10:
    j=1
    while j<10:
        print(f'{i} * {j} = {i*j}')
        j+=1
    i+=1
    print()
print('구구단 종료')