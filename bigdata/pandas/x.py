import numpy as np
import pandas as pd
import html5lib
url='D:/AI_Class/Python/bigdata/pandas/sample.html'
tables = pd.read_html(url)
print(len(tables))
print()
for i in range(len(tables)):
    print('tables[%s]'%i)
    print(tables[i])
    print()