# chcemy wybrac wierzcholki w drzewie o maksymalnej sumie tak by zadne dwa sie byly poloczone krawedzia

class employee:
    def __init__(self,fun):
        self.emp=[]
        self.fun=fun
        self.f=-1
        self.g=-1

    def f(v):
        if v.f>=0: return v.f
        x=v.fun
        for ui in v.emp:
            x+=employee.g(points[ui])
        y=employee.g(v)
        v.f=max(x,y)
        return v.f

    def g(v):
        if v.g>=0: return v.g
        x=0
        for ui in v.emp:
            x+=employee.f(points[ui])
        v.g=x
        return v.g


adjacency_list = [(10,[1, 2]),(5,[3, 4]),(8,[]),(2,[]),(7,[])]

points=[]
for i,tab in adjacency_list:
    x=employee(i)
    x.emp=tab
    points.append(x)

print(employee.f(points[0])) # 0 - root
