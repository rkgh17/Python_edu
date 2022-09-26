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