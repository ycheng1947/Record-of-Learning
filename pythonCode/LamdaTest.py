# g = lambda x:x+1
# print g(1)

# def f(x): return x%2!=0 and x % 3 !=0
# print filter(f,range(2,25))

# def g(x) : return x!='a'
# print filter(g,'asdfg')
# 

# def m(x):return x*x*x
# print map(m,(1,2,3,4))
# [1, 8, 27, 64]

def add(x,y): return x+y
print reduce(add,range(1,10),20)
