##Pandas
> pandas ���õ�һЩ����������excel ��ʱ�򣬶�ȡ��д��ĳ������

#### 1. ��ȡexcel�ļ�ʹ��read_excel()����
```buildoutcfg
df = pandas.read_excel(filename)
```
#### 2.��ȡexcel��headers
```buildoutcfg
cols = df.columns
headers = [i for i in cols]
print(headers)
```
#### 3.��ȡexcel��ÿһ������
```buildoutcfg
print(df.loc[1].values) #�ڶ������ݣ�����header��
```
