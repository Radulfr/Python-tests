#HTML tags
table_h = "<table>"
table_f = "</table>"
row_h = "<tr>"
row_f = "</tr>"
cell_h = "<td>"
cell_f = "</td>"

#Rows index
ROW1=0
ROW2=1
ROW3=2
ROW4=3
ROW5=4

#Reports
r1 = [11,12,13,14,15]
r2 = [21,22,23,24,25]
r3 = [31,32,33,34,35]
reports = [r1,r2,r3]

#Functions
single_cell = lambda x: cell_h + str(x) + cell_f

#TODO - try to index too (not possible use 'row' function with 'map')

#row = lambda x,row: x[row]
function_row1 = lambda x: x[ROW1]
function_row2 = lambda x: x[ROW2]
function_row3 = lambda x: x[ROW3]
function_row4 = lambda x: x[ROW4]
function_row5 = lambda x: x[ROW5]

#Results
row_1 = map(function_row1, reports)
row_2 = map(function_row2, reports)
row_3 = map(function_row3, reports)
row_4 = map(function_row4, reports)
row_5 = map(function_row5, reports)

all_rows = [row_1, row_2, row_3, row_4, row_5]

#Formats
result_single_row = lambda x: "\n\t" + row_h + ''.join(map(single_cell, x)) + row_f 
result_final = lambda x: table_h +"\n\t" ''.join(map(result_single_row, x)) +"\n" + table_f

print result_final(all_rows)
