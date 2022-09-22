class Menu:
    def __init__(self):
        self.menu=[]
        try:
            f=open('d:/AI_Class/Python/file/menu/menu.txt','r')
        except Exception as e:
            print('파일이없기 때문에 새로 생성합니다.')
            return
        line=f.readline()

        while line!='':
            ar=line.split(',')
            m={'name':ar[0], 'price':int(ar[1])}
            self.menu.append(m)
            line=f.readline()
        
        f.close()
    
    def display(self):
        f=open('d:/AI_Class/Python/file/menu/menu.txt','r')
        ndx=1
        for m in self.menu:
            print('%2d | %-10s | %4d원'%(ndx, m['name'], m['price']))
            ndx+=1
        f.close()

    def addMenu(self):
        name = input('메뉴명 : ')
        while name!='':
            price = input('가격 : ')
            while not price.isnumeric():
                price=input('가격 : ')
            price=int(price)
            self.menu.append({'name':name,'price':price})
            name=input('메뉴명 : ')
        f=open('d:/AI_Class/Python/file/menu/menu.txt','w')
        for m in self.menu:
            f.write(m['name']+','+str(m['price'])+'\n')
        f.close()
        
        

#클래스 인스턴스 생성
menu=Menu() # 인스턴스, 변수, 지역변수. 메뉴정보를 읽어서 초기화.

# menu.display()
# menu.addMenu()
print('-'*80)
num=input('1.주문입력 | 2.메뉴관리 | 3.실적보기 | 0.프로그램 종료 \n번호입력 : ')

if num==1:
    menu.addMenu()
elif num==2:
    menu.display()
elif num==3:
    pass
elif num==0:
    print('프로그램 종료.')
else:
    num=input('올바르지 않은 번호입니다. 다시 입력해주세요 : ')