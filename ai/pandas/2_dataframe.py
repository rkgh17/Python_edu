import numpy as np
import pandas as pd

dict_data={'c0':[1,2,3],'c1':[4,5,6],'c2':[7,8,9],'c3':[10,11,12],'c4':[13,14,15]}
df = pd.DataFrame(dict_data)
print(df)
"""
   c0  c1  c2  c3  c4 ->헤더
0   1   4   7  10  13
1   2   5   8  11  14
2   3   6   9  12  15
"""

df=pd.DataFrame([[15,'남','덕영중'],[17,'여','수리중'],[14,'공','영창초']],
                index=['준서','예은','현지'],#행이름
                columns=['성별','나이','학교']#열이름
               )
print(df)
"""
    성별 나이   학교 --columns
준서  15  남  덕영중
예은  17  여  수리중
현지  14  공  영창초
 |
index
"""


df=pd.DataFrame([['John',44445555,'M','LA'],['Jane',43215452,'F','LV'],['Jacob',77778888,'M',None],['Johanson',12345432,'F','MI']],
                index=['1st','2nd','3rd','4th'],
                columns=['name','mobile','gender','city']
               )
print(df)
"""
         name    mobile gender  city
1st      John  44445555      M    LA
2nd      Jane  43215452      F    LV
3rd     Jacob  77778888      M  None
4th  Johanson  12345432      F    MI
"""

df.index=['1ST','2ND','3RD','4TH']
df.columns=['이름','모바일','성별','도시']
print(df)
"""
           이름       모바일 성별    도시
1ST      John  44445555  M    LA
2ND      Jane  43215452  F    LV
3RD     Jacob  77778888  M  None
4TH  Johanson  12345432  F    MI
"""

df.rename(index={'1ST':'첫줄','3ND':'셋째','2ND':'둘째'})
df.rename(columns={'도시':'City','모바일':'Mobile','성별':'Gender'})
"""
	이름	Mobile	Gender	City
1ST	John	44445555	M	LA
2ND	Jane	43215452	F	LV
3RD	Jacob	77778888	M	None
4TH	Johanson12345432	F	MI
"""

#행 (axis=0(default)) / 열 (axis=1)
#inplace=True : 진짜 삭제 / False(default) : 진짜 삭제x
df.drop(['2ND','3RD'])
"""
	이름	모바일	성별	도시
1ST	John	44445555	M	LA
4TH	Johanson12345432	F	MI
"""
df.drop({'모바일','도시'},axis=1)
"""
    이름	성별
1ST	John	M
2ND	Jane	F
3RD	Jacob	M
4TH	Johanson	F
"""
# loc/iloc
# 2개 이상일때 -> .loc[['a','b']]
# 인덱스 이름 ['a':'c'] -> a,b,c
df.loc['2ND'] #인덱스 이름이 2ND인것
df.loc[['2ND','3RD']] # 인덱스 이름이 2ND와 3RD
# 정수형 위치 인덱스 [3:7] -> 3,4,5,6
df.iloc[3] #위치 인덱스가 3인것