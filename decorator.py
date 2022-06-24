def dec(func):
    def ins(a):
        a = func(a)
        if a==100:
            return 200 + 200
    return ins





@dec
def sum(a):
    return a

print(sum(100))