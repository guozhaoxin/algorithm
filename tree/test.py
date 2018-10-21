#encoding:utf8
__author__ = 'gold'

class room:
    def __init__(self,area=120,usedfor='sleep'):
        self.area = area
        self.usedfor = usedfor

    def display(self):
        print("this is my house")

class babyroom(room):
    def __init__(self,area=40,usedfor="son",wallcolor='green'):
        super(babyroom,self).__init__(area,usedfor)
        self.wallcolr = wallcolor

    def display(self):
        super(babyroom,self).display()
        print("babyroom area:%s wallcollor:%s"%(self.area,self.wallcolr))

class Test:
    def __init__(self,value):
        self.value = value

    def __len__(self):
        return len(self.value)

if __name__ == '__main__':
    class Foo(object):

        def __init__(self):
            self.name = 'abc'

        def func(self):
            return 'ok'


    obj = Foo()
    # 获取成员
    ret = getattr(obj, 'func')  # 获取的是个对象
    r = ret()
    print(r)
    # 检查成员
    ret = hasattr(obj, 'func')  # 因为有func方法所以返回True
    print(ret)
    # 设置成员
    print(obj.name)  # 设置之前为:abc
    ret = setattr(obj, 'name', 19)
    print(obj.name)  # 设置之后为:19
    # 删除成员
    print(obj.name)  # abc
    delattr(obj, 'name')
    # print(obj.name)  # 报错