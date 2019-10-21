import xlrd
def getarea():
    dir_case = './data.xlsx'
    data = xlrd.open_workbook(dir_case)
    table = data.sheets()[0]
    nor = table.nrows
    nol = table.ncols
    area = {}
    for i in range(1, nor):
        for j in range(nol):
            title = table.cell_value(i, 0)
            value = table.cell_value(i, 1)
            area[title] = value
    return area

area=getarea()

#print(area)
def getdata(filenum):
    dir_case = './data.xlsx'
    data1 = xlrd.open_workbook(dir_case)
    table1= data1.sheets()[filenum]
    nor1= table1.nrows
    nol1= table1.ncols
    area1 = {}
    for i in range(1, nor1):
        title1= table1.cell_value(i, 0)
        year = {}
        for j in range(1,nol1):
            title2 = table1.cell_value(0, j)
            value1= table1.cell_value(i, j)
            # print(value)
            year[title2] = value1
        area1[title1] = year
    return area1

areagdp = getdata(1)

areapopulation = getdata(2)

total={}
for name in area.keys():
    total[name]={}
    total[name]['面积']=area[name]
    total[name]['地区gdp(亿元)'] = areagdp[name]
    total[name]['人口(万人)'] = areapopulation[name]

import pandas as pd
sarea = pd.Series(area)
print(sarea)
pop = {}
gdp = {}
for name in total.keys():
    for year in total[name]['人口(万人)'].keys():
        pop[(name, int(year[:4]))] = total[name]['人口(万人)'][year]

    for year in total[name]['地区gdp(亿元)'].keys():
        gdp[(name, int(year[:4]))] = total[name]['地区gdp(亿元)'][year]

spop = pd.Series(pop)
sgdp = pd.Series(gdp)
print(spop)
print(sgdp)

data0 = pd.DataFrame({'人口(万人)':spop, '地区gdp(亿元)':sgdp})
data1 = pd.DataFrame({'面积':sarea})

data0.to_csv('pop_and_gdp.csv')
data1.to_csv('area.csv')
print(data1)



