import os
"""
    为什么要有函数？函数可以封装公共的代码逻辑，减少重复代码的编写
    函数的定义：def 函数名(形参1:类型 , 形参2:类型):
"""


# def aaaa(bbb:str,ccc:str = " test"):
    # print("hello world" + bbb+ccc)

"""
    假设定义一个函数：def 函数名(形参1:类型 , 形参2:类型):
    函数的调用：函数名(形参1，形参2) 形参会按照指定的顺序依次传入函数
    python可以指定函数名传参 比如：函数名(形参2 = 'a') 此时函数的第一个形参1不会赋值，直接赋值给形参2
"""
# aaaa(bbb = "ccc")




# 函数命名要小驼峰 比如 create folder  createFolder
"""
    os 库 操作系统库 拥有操纵本机系统的能力
    判断路径在本机是否存在：os.path.exists(路径) -> bool
    在本机创建文件夹：os.makedirs(路径)
"""

def createFolder(dir:str):
    if os.path.exists(dir):
        return True
    os.makedirs(dir)
    return False

a = createFolder("test1")
print(a)
