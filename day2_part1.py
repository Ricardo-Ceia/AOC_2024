reports = []


with open("inputFile.txt", 'r') as f:
    for line in f:
        if line.strip():  
            reports.append(line.split())

print("Reports:", reports)

safe_reports = 0 

for level in reports:
    is_ascending = True
    is_descending = True
    
    for i in range(len(level) - 1):
        diff = abs(int(level[i]) - int(level[i + 1]))

        if diff > 3 or diff == 0:  
            is_ascending = False
            is_descending = False
            break
        
        if int(level[i]) >= int(level[i + 1]):
            is_ascending = False
        if int(level[i]) <= int(level[i + 1]):
            is_descending = False  
        
        if not is_ascending and not is_descending:
            break

    if is_ascending or is_descending:
        safe_reports += 1

print("Safe Reports:", safe_reports)