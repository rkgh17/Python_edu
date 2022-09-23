class Order:

    def __init__(self):
        self.lorder=[]
        self.mobile=''

    def build(self,menulist):
        grandTotal=0#총 누적합
        #메뉴번호 읽기
        menu_num=input('주문할 메뉴의 번호를 입력하시오 : ')
        while menu_num!='':
            if not menu_num.isnumeric():#입력된 값이 숫자가 아닌경우
                menu_num=input('메뉴번호를 입력하시오 : ')
                continue
            menu_num=int(menu_num)
            #수량 읽기
            qty=input('수량을 입력하시오 : ')
            while not qty.isnumeric():
                qty=input('수량을 입력하시오 : ')
            qty=int(qty)
            #금액계산
            total=menulist[menu_num-1]['price']*qty
            print(f'금액 : {total}원')
            grandTotal+=total
            self.lorder.append({'menu':menulist[menu_num-1]['name'],'qty':qty,'total':total})
            menu_num=input('메뉴번호를 입력하시오 : ')
        print(f'주문총금액 : {grandTotal}원')
        self.mobile=input('적립 모바일 번호:')
