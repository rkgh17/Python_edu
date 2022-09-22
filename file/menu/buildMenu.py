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
        
    # def run(self,x):
    #     if x==1:
    #         menu.addMenu()
    #         return
    #     elif x==2:
    #         print('-'*60)
    #         job=int(input('1. | 2. | 3. | 0'))
    #         menu.display()
    #         return
    #     elif x==3:
    #         pass
    #     elif x==0:
    #         print('프로그램 종료.')
    #         return
    #     else:
    #         x=int(input('올바르지 않은 번호입니다. 다시 입력해주세요 : '))
    #         return menu.run(x)

    def updateMenu(self):
        menu_num=int(input('수정할 번호 : '))
        name=input('새 메뉴명 : ')
        price=int(input('새 가격 : '))
        self.menu[menu_num-1]['name']=name
        self.menu[menu_num-1]['price']=price
        f=open('d:/AI_Class/Python/file/menu/menu.txt','w')
        for m in self.menu:
            f.write(m['name']+','+str(m['price'])+'\n')
        f.close()

    def deleteMenu(self):
        menu_num=int(input('삭제할 메뉴번호 : '))
        del self.menu[menu_num-1]
        f=open('d:/AI_Class/Python/file/menu/menu.txt','w')
        for m in self.menu:
            f.write(m['name']+','+str(m['price'])+'\n')
        f.close()
        print('삭제 완료')

#클래스 인스턴스 생성
menu=Menu() # 인스턴스, 변수, 지역변수. 메뉴정보를 읽어서 초기화.

print('-'*60)
num=int(input('1.주문입력 | 2.메뉴관리 | 3.실적보기 | 0.프로그램 종료 \n번호입력 : '))
while num!=0:
    if num==1:
        pass
    elif num==2:
        print('-'*60)
        job=int(input('메뉴관리 : 1.추가 | 2.조회 | 3.수정 | 4.삭제 | 0.종료\n번호입력 : '))
        type(job)
        while job!=0:
            if job==1:
                menu.addMenu()
                break
            elif job==2:
                menu.display()
                break
            elif job==3:
                menu.updateMenu()
                break
            elif job==4:
                menu.deleteMenu()
                break
    elif num==3:
        pass
    elif num==0:
        print('프로그램 종료.')
    else:
        num=input('올바르지 않은 번호입니다. 다시 입력해주세요 : ')