#숫자 2개를 순서대로 읽어들여서 대소비교 결과를 출력

x=input('x를 입력하시오 : ')
y=input('y를 입력하시오 : ')

if x>y:
    print(f'x : [{x}] 가 y : [{y}] 보다 큽니다.')
elif x==y:
    print(f'x : [{x}] 는 y : [{y}] 와 동일합니다.')
else:
    print(f'x : [{x}] 는 y : [{y}] 보다 작습니다.')