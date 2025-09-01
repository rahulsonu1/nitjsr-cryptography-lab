def euclidean(a, b):
    return a if b == 0 else euclidean(b, a % b)





a=60
b=48

print(euclidean(a,b))