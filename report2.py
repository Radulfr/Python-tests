rows = lambda x: "<td>" + str(x) + "</td>"

C1=0
C2=1
C3=2
C4=3
C5=4

columns = [C1,C2,C3,C4,C5]

p1 = [11,12,13,14,15]
p2 = [21,22,23,24,25]
p3 = [31,32,33,34,35]
reports = [p1,p2,p3]

table_h = "<table>"
table_f = "</table>"
row_h = "<tr>"
row_f = "</tr>"

row1 = lambda x: x[C1]
row2 = lambda x: x[C2]

rows_values = [row1, row2]

#row = lambda x,row: x[row]

row_1 = map(row1, reports)
row_2 = map(row2, reports)

#row_3 = map(row, reports,2)

print row_1
print row_2
#print row_3
#result_single_row = lambda x: table_h + row_h + ''.join(map(rows, x)) + row_f +

result_single_row = lambda x: table_h + row_h + ''.join(map(rows, x)) + row_f 

print result_single_row(row1)

#final_table = lambda x: table_h + ''.join(map(result_single_row(result_single_row, x))) + table_f

#res = final_table(rows_values)

print res

#print ''.join(map(result_row_C1,reports))
