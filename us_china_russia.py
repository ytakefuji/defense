import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
wb=openpyxl.load_workbook('SIPRI-Milex-data-1949-2020_0.xlsx')
sheet=wb['Constant (2019) USD']
sheet.delete_rows(sheet.min_row,5)
wb.save('result.xlsx')
d=pd.read_excel('result.xlsx',engine='openpyxl',sheet_name='Constant (2019) USD')
usa=d.loc[d.Country=='USA']
china=d.loc[d.Country=='China']
russia=d.loc[d.Country=='Russia']
us=[]
for i in range(2000,2021):
 us.append(int(usa[i]))
cn=[]
for i in range(2000,2021):
 cn.append(int(china[i]))
ru=[]
for i in range(2000,2021):
 ru.append(int(russia[i]))
x=[]
for i in range(2000,2021):
 x.append(i)
plt.plot(x,us,'k-',label="US")
plt.plot(x,cn,'k:',label="China")
plt.plot(x,ru,'k--',label="Russia")
plt.legend()
plt.savefig('result.png')
plt.show()
