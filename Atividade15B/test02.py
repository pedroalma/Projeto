nome = False
while not nome:
    f1 = int(input("um numero ?"))
    f2 = int(input("outro numero ?"))
    from numpy import zeros,ones,empty
    a = ones([f1,f2], dtype=object)
    a.fill(0)
    print("A primeira matriz é")
    print(a)

'''
f1 = input("um numero ?")
f2 = input("outro numero ?")
from numpy import ones
a = ones( [f1,f2])
a = empy
print("A primeira matriz é")
print(a)
'''