student=[]
print('-'*80)
f=open('d:/AI_Class/Python/todayLunch/lunch.txt','r', encoding='UTF-8')
line=f.readline()
while line!='':
    ar=line.split(',')
    str={'name':ar[0], 'math':int(ar[1])}
    student.append(str)
    line=f.readline()
f.close()

for str in student:
    print(str['name'], str['math'])