import re

with open("inputFile.txt",'r') as f:
    text = f.read()

def get_numbers(mul):
    numbers = []
    for i in range(len(mul)):
        num=""
        if mul[i]=='(':
            count=i+1
            while mul[count]!=',':
                num+=mul[count]
                count+=1
            numbers.append(int(num))
        if mul[i]==',':
            count=i+1
            while mul[count]!=')':
                num+=mul[count]
                count+=1
            numbers.append(int(num))
    return numbers

enabled=True
sum=0
for elem in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)",text):
    match elem:
        case 'do()':
            enabled = True
        case "don't()":
            enabled = False
        case _:
            if enabled:
                numbers = get_numbers(elem)
                print(elem,numbers)
                sum += numbers[0]*numbers[1]

    

print(sum)

        
