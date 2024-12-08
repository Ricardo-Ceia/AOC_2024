def is_ordered(level):
    for i in range(len(level)-1):
        diff = abs(level[i]-level[i+1])
        if diff>3 or diff==0:
            return False
        
    ascending = all(level[i]<=level[i+1] for i in range(len(level)-1))
    descending = all(level[i]>=level[i+1] for i in range(len(level)-1))
    return ascending or descending


def is_valid_with_removal(level):
    if is_ordered(level):
        return True
    for i in range(len(level)):
        modified = level[:i]+level[i+1:]
        if is_ordered(modified):
            return True
    return False

reports = []

with open("inputFile.txt",'r') as f:
    for line in f:
        if line.split():
            reports.append(list(map(int,line.split())))

print("Reports:",reports)

safe_reports = 0

for level in reports:
    if is_valid_with_removal(level):
        safe_reports+=1

print("Safe Reports:",safe_reports)