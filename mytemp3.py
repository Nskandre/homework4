
def wrapper_mydec(a):
    def mydec(func):
        def wrapper(*args, **kwargs):
            mylist = [i * 2 for i in args]
            myres = sum(mylist)
            return myres
        return wrapper
    res_mydec = a * mydec()
    return res_mydec 


@wrapper_mydec(2)
def mytest(a, b):
    res = a + b
    return res

print(mytest(2, 3))