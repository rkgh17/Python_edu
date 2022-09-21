menu=[]
print('-'*80)
f=open('d:/AI_Class/Python/file/menu/menu.txt','r')
line=f.readline()
while line!='':
    ar=line.split(',')
    m={'name':ar[0], 'price':int(ar[1])}
    menu.append(m)
    line=f.readline()
f.close()

for m in menu:
    print(m['name'], m['price'])