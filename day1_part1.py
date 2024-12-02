id_list1 = []
id_list2 = []

with open("inputFile.txt",'r') as f:
    while True:
        data = f.readline()
        if not data:
            break
        data = data.split("   ")
        data[1] = data[1].replace('\n','')
        id_list1.append(data[0])
        id_list2.append(data[1])
sum = 0
id_list1.sort()
id_list2.sort()

for id1,id2 in zip(id_list1,id_list2):
    print(f"id1:{id1} id2:{id2}")
    diff = abs(int(id2)-int(id1))
    sum += diff
print(sum)