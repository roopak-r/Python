fname=input("Enter the file name:")
d=dict()
with open(fname)as f:
    for line in f.readlines():
        line=line.split()
        d.update({len(w):w for w in line})
print(d[max(d.keys())])
