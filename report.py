rows = lambda x: "<td>" + str(x) + "</td>"
a = [11,12,13,14,15]
b = [21,22,23,24,25]
c = [31,32,33,34,35]

table_h = "<table>"
table_f = "</table>"
row_h = "<tr>"
row_f = "</tr>"
result_row = lambda x: table_h + row_h + ''.join(map(rows,x)) + row_f + table_f
matrix = [a,b,c]

print ''.join(map(result_row,matrix))
