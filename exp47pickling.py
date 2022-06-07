import pickle
mydict={'a':1,'b':2,'c':3}
with open('filename.pickle','wb')as f:
    pickle.dump(mydict,f)
print(mydict)
with open('filename.pickle','rb')as f:
    mydict2=pickle.load(f)
print(mydict2)
