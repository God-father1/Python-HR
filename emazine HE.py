'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
b,c=0,0
a = input()
for _ in range(len(a)):
    if a[_] == "U":
        b+=1
    elif a[_] == "D":
        b-=1
    elif a[_] == "L":
        c-=1
    elif a[_] == "R":
            c+=1
    else:
        continue
print(str(c)+ " " +str(b))
