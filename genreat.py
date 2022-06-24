def generate():
    a=0
    b=1
    while True:
        yield b
        a,b=b,a+b

s=generate()
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))



