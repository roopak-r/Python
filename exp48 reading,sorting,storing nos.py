#to read numbers from a file and store after sorting and removing duplicates
import pickle
n=int(input("Enter limit:"))
a=[]
for i in range(n):2
    a.append(int(input("Enter the number:")))   
with open('number.pickle','wb')as f:
    a=pickle.dump(a,f)
with open('number.pickle','rb')as f:
    a=pickle.load(f)
print(a)
b=[]
for i in a:
    if i not in b:
        b.append(i)
b.sort()
with open('sortednumber.pickle','wb')as f:
    pickle.dump(b,f)
with open('sortednumber.pickle','rb')as f:
    b=pickle.load(f)
print(b)
