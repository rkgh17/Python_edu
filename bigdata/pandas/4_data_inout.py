"""
CSV (Comma-Separtated Values) : ,로 구분 / .csv
Exel (MS) / .xlsx
JSON () : 키:값 쌍으로 구분 : .txt
"""
import numpy as np
import pandas as pd

#CSV
file_path = 'D:/AI_Class/Python/bigdata/pandas/read_csv_sample.csv'
df1 = pd.read_csv(file_path)
print(df1)
"""
   c0  c1  c2  c3
0   0   1   4   7
1   1   2   5   8
2   2   3   6   9
"""
print()

#옵션
# sep(또는 delimiter) : default ,
# header : default0
# index_col : 행 인덱스 열 번호
# names : 열 이름으로 사용할 문자열 리스트
# skiprows : 처음 몇 줄을 스킵할 것인지. 스킵범위 리스트 가능
# parse_dates : 날자 텍스트를 datetime64로 변환. default False
# skip_folder : 마지막 몇줄 skip
# encoding : 텍스트 인코딩 종류 지정
df2=pd.read_csv(file_path,header=None) 
print(df2)
print()