from functools import wraps
# 需要使用functools，wraps在装饰器中的函数上把传进来的函数进行一个包裹，这样就不会丢失原来的函数的__name__等属性


# 装饰器实际上就是一个函数
# 在所有的函数执行之前，都要打印一个hello world
# def run():
#     print('run')
#
# def add(a,b):
#     c = a+b
#     print(c)

# 装饰器函数
# 有两个特别之处：
#   1.参数是一个函数
#   2.返回值是一个函数
# 带括号是执行这个函数，返回函数的结果

# *args 位置参数
# **kwargs 关系参数
# 可以表示任何参数（或者没有参数）
def my_log(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print('Hello World')
        function(*args,**kwargs)
    return wrapper

# run = my_log(run) = wrapper
# 执行print 'Hello World'
# 执行print 'run'
@my_log
def run():
    print('run')

# add = my_log(add)=wrapper
# add(1,2) = wrapper(1,2)
@my_log
def add(a,b):
    c= a+b
    print(c)


run()
add(1,2)