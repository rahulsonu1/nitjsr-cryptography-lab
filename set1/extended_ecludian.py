def egcd(a,b):
    if b==0:
        return a,1,0
    g,x1,y1=egcd(b,a%b)
    return g,y1,x1-(a//b)*y1



a=56
b=52
g, x, y = egcd(a,b)
if(a*x+b*y==g):
    print("Yes")

print(f"gcd={g}, x={x}, y={y}")





# def egcd(a, b):
#     if b == 0:
#         return a, 1, 0
#     g, x1, y1 = egcd(b, a % b)
#     return g, y1, x1 - (a // b) * y1