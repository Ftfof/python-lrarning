# print("this is my python basic learning file")
# print("Ftfof"+"basic.py")
# a = input("请随机输入一个数字：")
# print(a)
# #---------------------("this is a basic file")--------------------
# b='hello Ftfof'
# print(b)
# print(a+b)
# print("\t")
# print("\\t")
# print(True and False)
# print(True or False)
# print(True & False)

# import numpy as np

# print(np.exp(3))
# print(1.6E3)
# print(True)
# print(False)
# print(type(True) and type(False))
# c = 1.25896
# print(type(c))
# print(str(c))
# print(type(str(c)))
# print(type(int(c)))
# print(isinstance(c,str))      #isintance(值，类型)
print(int(1.254689)**9)
print(58//8)
'''----------this is a circulation file----------'''
# if True:
#     print("执行条件真操作")
# else:
#     print("执行条件假操作")
# elif False:
#     print("执行条件假操作")
if True:
    result = "执行条件真操作"
elif False:
    result = "执行条件假操作"
else:
    result = "执行其他操作"
def demo():
    if True:
        return "执行条件真操作"
    elif False:
        return "执行条件假操作"
    else:
        return "执行其他操作"

print(demo())   # → 执行条件真操作  
'''------------this is a while circulation file------------'''
a = 2
while a ==2:
    print("a的值是：", a)
    a +=1 
print("a的值是：",a)
name = "Ftfof"
for i in name:
    print(i)
#for 循环
for u in range(1, 10):
    print("index:", u)
    print(f"这是第{u}次循环")
    continue  # 跳过当前循环的剩余部分，继续下一次循环
    print(f"nihao ftfof {u}")
    
    break

# ===================== range 函数 =====================
#range(start,stop,step)
print(list(range(2,45,3)))
print(list(range(10)))#不包含最后一位


'''---------------------random------------------------'''
import random
print(random.randint(2,45))
print(random.randrange(2,45))


x ,y = random.randint(10,35),random.randrange(3,67)
print(x,y)
d,f = x,y
print(d,f)




'''------------------list-------------------------'''
v = [1,2,3,45,4,4,4,"shi",False]
print(v[3])
print(v[-4])


# ... existing code ...
'''------------------list-------------------------'''
v = [1,2,3,45,4,4,4,"shi",False]
print(v[3])
print(v[-4])


#--------------------添加元素的方法-----------------------------
# 修复：append方法返回None，不应该赋值给g
v.append(5)
print(v)  # 查看添加元素后的列表
v.append(90)
print(v)

# 修复：extend方法需要传入一个可迭代对象，且返回None
v2 = [1, 2, 3]
v2.extend([4, 5])  # 传入一个列表
print(v2)

# 修复：insert方法返回None
v3 = [1, 2, 3]
v3.insert(2, 100)  # 在索引2处插入100
print(v3)  # 直接打印列表而不是insert方法的返回值

# 修复：列表没有delete方法，应该使用del或pop
v4 = [1, 2, 3, 4, 5]
# v4.delete(3)  # 错误：列表没有delete方法
del v4[3]  # 正确：使用del删除索引3处的元素
print(v4)

# 修复：remove方法正确，但应该直接调用而不是打印返回值
v5 = [1, 2, 3, 4, 4, 5]
v5.remove(4)  # 删除值为4的第一个元素
print(v5)  # 直接打印列表而不是remove方法的返回值

# 正确：del语句
v6 = [1, 2, 3, 4, 5]
del v6[0]
print(v6)

# 正确：pop方法
v7 = [1, 2, 3, 4, 5]
last_element = v7.pop()  # 删除并返回最后一个元素
print(last_element)
print(v7)

# 正确：pop方法带索引
v8 = [1, 2, 3, 4, 5]
element_at_2 = v8.pop(2)  # 删除并返回索引2处的元素
print(element_at_2)
print(v8)


#-----------------列表--------------------
c = [2,22,2,2,2,2,2,2,2,222,22,22,2]
print(c.count(2))
print(c.index(22))
c.sort()  # 对列表进行排序，该方法返回None
print(c)  # 打印排序后的列表
c.reverse()  # 反转列表，该方法返回None
print(c)  # 打印反转后的列表


#-----------------列表--------------------
c = [2,22,2,2,2,2,2,2,2,222,22,22,2]
print(c.count(2))
print(c.index(22))
print(c.sort())  # 对列表进行排序
print(c.reverse())#反转列表
d = range(2,45,2)
for i in d:
    squares = [i**2 for i in d]
print(squares)