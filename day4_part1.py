with open("inputFile.txt", 'r') as f:
    text = [line.strip() for line in f.readlines() if line.strip()]  # Handle empty lines
    print(text)

xmax_count = 0
rows = len(text)
cols = len(text[0]) if rows > 0 else 0

for i in range(rows):
    for j in range(cols):
        if text[i][j] == 'X':
            # Check right (horizontal)
            if j + 3 < cols:
                if text[i][j+1] == 'M' and text[i][j+2] == 'A' and text[i][j+3] == 'S':
                    print(f"X:{i} {j} M:{i} {j+1} A:{i} {j+2} S:{i} {j+3}")
                    xmax_count += 1

            # Check down (vertical)
            if i + 3 < rows:
                if text[i+1][j] == 'M' and text[i+2][j] == 'A' and text[i+3][j] == 'S':
                    print(f"X:{i} {j} M:{i+1} {j} A:{i+2} {j} S:{i+3} {j}")
                    xmax_count += 1

            # Check bottom-right diagonal
            if i + 3 < rows and j + 3 < cols:
                if text[i+1][j+1] == 'M' and text[i+2][j+2] == 'A' and text[i+3][j+3] == 'S':
                    print(f"X:{i} {j} M:{i+1} {j+1} A:{i+2} {j+2} S:{i+3} {j+3}")
                    xmax_count += 1

            # Check top-left diagonal
            if i - 3 >= 0 and j - 3 >= 0:
                if text[i-1][j-1] == 'M' and text[i-2][j-2] == 'A' and text[i-3][j-3] == 'S':
                    print(f"X:{i} {j} M:{i-1} {j-1} A:{i-2} {j-2} S:{i-3} {j-3}")
                    xmax_count += 1

        if text[i][j] == 'S':
            # Repeat similar checks for "SAMX" (reverse pattern)
            if j + 3 < cols:
                if text[i][j+1] == 'A' and text[i][j+2] == 'M' and text[i][j+3] == 'X':
                    print(f"S:{i} {j} A:{i} {j+1} M:{i} {j+2} X:{i} {j+3}")
                    xmax_count += 1

            if i + 3 < rows:
                if text[i+1][j] == 'A' and text[i+2][j] == 'M' and text[i+3][j] == 'X':
                    print(f"S:{i} {j} A:{i+1} {j} M:{i+2} {j} X:{i+3} {j}")
                    xmax_count += 1

            if i + 3 < rows and j + 3 < cols:
                if text[i+1][j+1] == 'A' and text[i+2][j+2] == 'M' and text[i+3][j+3] == 'X':
                    print(f"S:{i} {j} A:{i+1} {j+1} M:{i+2} {j+2} X:{i+3} {j+3}")
                    xmax_count += 1

            if i - 3 >= 0 and j - 3 >= 0:
                if text[i-1][j-1] == 'A' and text[i-2][j-2] == 'M' and text[i-3][j-3] == 'X':
                    print(f"S:{i} {j} A:{i-1} {j-1} M:{i-2} {j-2} X:{i-3} {j-3}")
                    xmax_count += 1

print("XMAX COUNT:", xmax_count)
