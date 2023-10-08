def s(n):
    if  n==1:
            resultado=1
    elif n>1:
            resultado=n+s(n-1)
    return resultado

print(s(78))