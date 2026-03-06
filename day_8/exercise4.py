def example(a,b,*argd,**kwargs):
    print("a",a)
    print("b",b)
    print("argd",argd)
    print("kwargs",kwargs)
example(1,2,3,4,name="babar",score=95)