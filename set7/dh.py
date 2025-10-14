def power(a,b):
    if b==1:
        return a
    else:
        return pow(a,b)

P=23 
G=31
A=6
B=23

x=power(G,A)%P
y=power(G,B)%P

secretKeyA=power(y,A)%P
sectetKeyB=power(x,B)%P
print(secretKeyA," ",sectetKeyB)