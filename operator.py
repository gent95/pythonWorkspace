# a = 1+2
# print(a)
#
# b = "good" + "job"
# print(b)
#
# a = -5
# print(a)
# b = -(-9)
# print(b)
#
# c = 9 -2
# print(c)
#
# d = 5 * 9
# print(d)

# b = "hello" * 6
# print(b)

#  a = 7 / 2
# print(a)

# a = 2 ** 3
# print(a)

# a = 3 < 7 > 9
# print(a)

# a = 2 != 3
# print(a)

#取余数部分
# a = 10 % 3
# print(a)

# 取整数部分
# a = 10 // 3
# print(a)

#1 0为0
# a = 7 & 18
# print(a)

#1 0为1
# a = 7 | 18
# print(a)

#抑或运算,相同为0,不同为1
# a = 7 ^ 18
# print(a)

#~ :按位反转 ~x = -(x +1)
# a = ~18
# print(a)

#向左移n位相当于乘以2的n次幂
# a = 18 << 2
# print(a)

#向右移n位相当于除以2的n次幂
# a = 18 >> 2
# print(a)

#and 其中一个为假则为假
# print (True and True)
# print(True and False)

#or其中一个为真则为真
# print(True or False)

#字符串加法 及 字符串索引
# s = "hello" + " world"
# print(s[0])
# print(s[-1])
#索引下标包括第一位,不包括最后一位
# print(s[0:5])
#字符串分割
# s = "hello world"
# s.split()
# print(s)

#查看字符串长度
# print(len(s))

#列表List
# a = [1,2.0,'hello',6+9]
# print(a)
# print(a[1])

#列表加法
# print(a+a)

#列表长度
# print(len(a))

#向列表汇总添加元素
# a.append("gent")
# print(a)

#集合set 集合中不含有相同元素(无序)
# s = {2,45,"gent"}
# print(s)
# s.add("gent")
# print(s)

#集合的交集
# a = {'a','b','c','d','e'}
# b = {'b','c','d','e','f'}
# print(a & b)
#集合并集
# print(a | b)
#集合的差
# print(a - b)
#对称差
# print(a ^ b)

#字典 Dictionary {key:value}
d = {'name':'gent','age':22,'hoby':['basketball','pingpang','code']}
# print(d)
#查看键对应的值
# print(d.get('hoby'))
#修改键值
# d['age'] = 23
print(d)
#所有键
print(d.keys())
#所有值
print(d.values())
#所有键值对
print(d.items())














