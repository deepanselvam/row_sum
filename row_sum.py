a = int(input())
b = int(input())
matrix = []
for i in range(a):
    row = []
    for j in range(b):
        element = int(input())
        row.append(element)
    matrix.append(row)
l = []
for i in range(a):
    rowsum = 0
    for j in range(b):
        rowsum += matrix[i][j]
    l.append(rowsum)
print(l)
