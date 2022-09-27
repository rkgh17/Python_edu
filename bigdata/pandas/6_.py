import pandas as pd
df = pd.read_excel('D:/AI_Class/Python/bigdata/pandas/남북한발전전력량.xlsx',engine='openpyxl')
df_ns=df.iloc[[0,5],3:]#남북 발전량 합계 데이터 추출
df_ns.index=['South','North']#행 인덱스 변경
#print(df_ns)
df_ns.columns=df_ns.columns.map(int)#열 이름의 자료형을 정수형으로 변경
print(df_ns.head())
df_ns.plot()

tdf_ns=df_ns.T
print(tdf_ns.head())
tdf_ns.plot()#행/열 전치하여 다시 그리기