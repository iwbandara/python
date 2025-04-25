import openpyxl as xl

wb = xl.load_workbook('F:/Study/Python/Examples/sample.xlsx')

ws = wb.active

# reading data from a range of cells (from column 1 to 6)

my_list = list()

for value in ws.iter_rows(
    min_row=1, max_row=5, min_col=1, max_col=3, 
    values_only=True):
    my_list.append(value)
    
for ele1,ele2,ele3 in my_list:
    (print ("{:<8}{:<15}{:<10}".format(str(ele1),str(ele2),str(ele3))))
