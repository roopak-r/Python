#to find mean median and mode of a list of numbers
import statistics
n=int(input("Enter n:"))
a=[]
for i in range(n):
    a.append(int(input()))
print("Original list is:",a)
a.sort()
print("Sorted list is:",a)
print("Mean is:",statistics.mean(a))
print("Median is:",statistics.median(a))
print("Mode is:",statistics.mode(a))
