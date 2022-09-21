# """
# 같은 동작들의 모음

# def 함수명(매개변수1, ....매개변수n):
#     실행문
#     [return 반환값]

# """
# def displaymenu(menulist):#데이터 출력 함수
#     ndx=1
#     for m in menulist:
#         print('%2d | %-10s | %4d원'%(ndx, m['name'], m['price']))
#         ndx+=1

# menu=[]

# f=open('d:/AI_Class/Python/file/menu/menu.txt','w')
# while True:
#     name=input('메뉴를 입력하시오 : ')
#     if name=='':
#         break
#     price=int(input('가격을 입력하시오 : '))
#     f.write(name+', '+str(price)+'\n')
# f.close()

# print('-'*80)
# f=open('d:/AI_Class/Python/file/menu/menu.txt','r')
# line=f.readline()
# while line!='':
#     ar=line.split(',')
#     m={'name':ar[0], 'price':int(ar[1])}
#     menu.append(m)
#     line=f.readline()
# f.close()

# displaymenu(menu)

def f1(x):
    n=15
    print(f'x [{x}] | n [{n}]')
n=10
print(f'global : n [{n}]')
f1(5)