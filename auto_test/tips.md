##Pandas
> pandas 常用的一些方法：操作excel 的时候，读取和写入的常规操作

#### 1. 读取excel文件使用read_excel()方法
```buildoutcfg
df = pandas.read_excel(filename)
```
#### 2.读取excel的headers
```buildoutcfg
cols = df.columns
headers = [i for i in cols]
print(headers)
```
#### 3.读取excel的每一行数据
```buildoutcfg
print(df.loc[1].values) #第二行数据，不算header行
```
