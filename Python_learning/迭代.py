'''
练习1：
有一个列表，其中包括10个元素，例如这个列表是[1,	2,	3,	4,	5,	6,	7,	8,	9,	0	]	，	要求将列表
中的每个元素一次向前移动一个位置，第一个元素到列表的最后，然后输出这个列表。最终
样式是[2,3,4,5,6,7,8,9,0,1]
'''
# 方法1
# tmp_lst = [1,2,3,4,5,6,7,8,9,0]
# tmp = []
# for i in range(1,len(tmp_lst)):
#     tmp.append(tmp_lst[i])
# tmp.append(tmp_lst[0])
# print(tmp)
#方法二
tmp_lst = [1,2,3,4,5,6,7,8,9,0]
tmp = tmp_lst.pop(0)  #删除后会改变原来的list
tmp_lst.append(tmp)

# print(tmp_lst)

'''
练习二
1.	   产生一个列表，其中有40个元素，每个元素是0到100的一个随机整数
2.	   如果这个列表中的数据代表着某个班级40人的分数，请计算成绩低于平均分的学生人数，并输出
3.	   对上面的列表元素从大到小排序
'''
import random
# 1.生成40个100以内的整数
score = []
for i in range(40):
    score.append(random.randint(0,100))
# 2.如果这个列表中的数据代表着某个班级40人的分数，请计算成绩低于平均分的学生人数，并输出
sum_score = sum(score) #直接对列表所有元素相加
avg_score = sum_score/len(score)
# print(avg_score)
count = len([each for each in score if each < avg_score])
# print(count)
# 3. 排序
sort_score = sorted(score,reverse=True)
# print(sort_score)

'''
如果将一句话作为一个字符串，那么这个字符串中必然会有空格（这里仅讨论英文），比 
如"How	are	you."，但有的时候，会在两个单词之间多打一个空格。现在的任务是，如果一个 
字符串中有连续的两个空格，请把它删除。
'''

list_str = 'How  are  you.  where are    you  from'
tmp_lst = list_str.split(' ')
# print(tmp_lst)
a = ' '.join([i for i in tmp_lst if i!=''])
# print(a)

'''
计算斐波那契数列100的值
'''

a = 0
b = 1

for i in range(2):
    a,b = b,a+b

print(a)