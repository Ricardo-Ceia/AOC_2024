import re

with open("inputFile.txt",'r') as f:
    text = f.read()


print(text)

pattern = "mul\(\d{1,3},\d{1,3}\)"

matches = re.findall(pattern,text)

print(matches)
numbers=[]
for match in matches:
    for i in range(len(match)):
        num=""
        if match[i]=='(':
            count=i+1
            while match[count]!=',':
                num+=match[count]
                count+=1
            numbers.append(num)
        if match[i]==',':
            count=i+1
            while match[count]!=')':
                num+=match[count]
                count+=1
            numbers.append(num)

print("numbers:",numbers)

sum = 0

for i in range(0,len(numbers),2):
    sum += int(numbers[i])*int(numbers[i+1])

print("sum:",sum)