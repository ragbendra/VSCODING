"""def marks(**kwargs):
    print(kwargs)
    total=0
    for items in kwargs.values():
        total+=items
    return sum(kwargs)+total
print(marks(1,2,3,name=12,age=18))"""

"""a = 1
def confusion(a):
    a+=1
    return a
print(a)
print(confusion(5))
"""
"""def outer():
    x = 'local'
    def inner():
        nonlocal x
        x='non local'
        print('inner: ',x)
    inner()
    print('outer: ',x)
outer()"""
l = [1,2,3,4]
def od(item):
    return item % 2 != 0
print(list(filter(od,l)))  # filters or ignores the value which doesnot satisfy the condition

a = [1,2,3,4]
b = [5,6,7,8]
print(list(zip(a,b)))