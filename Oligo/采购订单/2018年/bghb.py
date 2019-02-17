import pandas as pd
import os

absdir=os.path.abspath('.')

alldata = pd.DataFrame()


files=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.xlsx']

for file in files:
    absfile = os.path.join(absdir,file)
    newdata = pd.read_excel(r'%s'%absfile,
                            skiprows=[0,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16],)    
    alldata = alldata.append(newdata)
alldata.set_index(['序号'],inplace=True)
del alldata['Unnamed: 14']
#alldata=alldata.reset_index()
alldata.to_excel(r'%s.xlsx'%absdir,encoding='utf-8-sig')
