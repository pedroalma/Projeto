r = []
for n in range(5): 
    v = int(input("numero "))
    if v > 0:
        r.append(v)     
print(sum(r))
print(sum(r) * (len(r)*1.6))
print(r)