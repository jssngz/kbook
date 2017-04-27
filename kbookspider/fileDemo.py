import os
print(os.path.exists(r'E:\book\123\aaa.txt'))
print(os.path.dirname(r'E:\book\123\aaa.txt'))
os.makedirs(os.path.dirname(r'E:\book\123\aaa.txt'), exist_ok=True)

with open(r'E:\book\123\bbb.txt', 'r') as code:
    for eachLine in code:
        print(eachLine)
with open(r'E:\book\1234\ccc.txt', 'w') as fopen:
    fopen.write("this is write")

