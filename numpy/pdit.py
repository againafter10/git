### merge xls sheets for quarterly maintenance

### convert xls to csv format

from xlrd import open_workbook
import csv,os

#print((os.listdir(os.getcwd()))) # returns a list

#['.DS_Store', 'cmpcsv.py', 'data', 'data.csv', 'datacsv.py', 'example.tsv', 'headerRemoved', 'numpy_version.py', 'output.csv', 'output2.csv', 'pdit.py', 'removeheader.py']
for i in os.listdir(os.getcwd()):
    print(i[:-3:])
    print
    if i[:-3:] == "xlsx":
        print("convert")
    else:
        print("not needed")







'''

wb = open_workbook('./data/sample.xlsx')

sheet = wb.sheet_by_index(1) #take each sheet by index
#sh = wb.sheet_by_name('Sheet1')  --- take each sheet by name
with open("./data/%s.csv" %(sheet.name.replace(" ","")), "w") as file:
    writer = csv.writer(file, delimiter = ",")
    print sheet, sheet.name, sheet.nrows
    header = [cell.value for cell in sheet.row(0)]
    writer.writerow(header)
    for row_idx in range(1, sheet.nrows):
        row = [int(cell.value) if isinstance(cell.value, float) else cell.value for cell in sheet.row(row_idx)]
        writer.writerow(row)


'''            
