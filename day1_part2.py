id_list1 = []
id_list2 = []

with open("inputFile.txt", 'r') as f:
    for line in f:
        data = line.strip().split("   ")
        if len(data) >= 2:
            id_list1.append(data[0])
            id_list2.append(data[1])

set_id_list1 = set(id_list1)

number_of_dups = {}

for i,id1 in enumerate(set_id_list1):
    for j in range(len(id_list2)):
        if id1==id_list2[j]:
            if id1 not in number_of_dups:
                number_of_dups[id1]=1
            else:
                number_of_dups[id1] += 1
                
for i in range(len(id_list1)):
    if id_list1[i] in number_of_dups:
        sum += int(number_of_dups[id_list1[i]])*int(id_list1[i])

print(sum)