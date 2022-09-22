class Menu:
    def __init__(self):
        self.menu=[]
        f=open('d:/AI_Class/Python/file/menu/menu.txt','r')
        line=f.readline()
        while line!='':
            ar=line.split(',')
            m={'name':ar[0], 'price':int(ar[1])}
            self.menu.append(m)
            line=f.readline()
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
        ndx=1
        for m in self.menu:
            f.write(m['name']+','+str(m['price'])+'\n')
            print('%2d | %-10s | %4d원'%(ndx, m['name'], m['price']))
            ndx+=1
        f.close()

#클래스 인스턴스 생성
menu=Menu() # 인스턴스, 변수, 지역변수. 메뉴정보를 읽어서 초기화.

#addMenu호출 생성
a=menu.addMenu()