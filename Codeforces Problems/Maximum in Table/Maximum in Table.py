n = int(input())
rows = []
cols = []
for x in range(n):
    rows.append(1)
cols.append(rows)
print(cols)
for i in range(n-1):
    rows = []
    for j in range(n):
    	if j==0:
    	   rows.append(1)
    	else:
            a=rows[j-1]+cols[(len(cols)-1)][j]
            rows.append(a)
    cols.append(rows)
print(cols[n-1][n-1])

