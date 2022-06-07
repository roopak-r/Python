#nth term of fibonacci using dictionary
previous={0:0,1:1}
def fibo(m):
    if m in previous:
        return previous[m]
    else:
        new_val=(fibo(m-1)+fibo(m-2))
        previous[m]=new_val
        return new_val
n=int(input("Enter n:"))
print(fibo(n))
