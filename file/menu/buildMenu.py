class Menu:
    # def __init__():
    #     pass
    def buildMenu(self):
        menu=[]
        name = input('메뉴명 : ')
        while name!='':
            price = input('가격 : ')
            while not price.isnumeric():
                price=input('가격 : ')
            price=int(price)
            menu.append({'name':name,'price':price})
            name=input('메뉴명 : ')

        f=open('d:/AI_Class/Python/file/menu/menu.txt','a')
        ndx=1
        for m in menu:
            f.write(m['name']+','+str(m['price'])+'\n')
            print('%2d | %-10s | %4d원'%(ndx, m['name'], m['price']))
            ndx+=1
        f.close()

#클래스 인스턴스 생성
menu=Menu() # 인스턴스, 변수, 지역변수

#buildMenu호출 생성
a=menu.buildMenu()