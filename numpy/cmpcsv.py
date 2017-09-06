# compare 2 csv files and see if the content is different

'''
import csv
csv1 = open('data.csv')
csv2 = open('output.csv')
csv1_read=csv.reader(csv1)
csv2_read=csv.reader(csv2)

if csv1 != csv2:
    print ("not equal")
    
time_dict={}    
for row in csv1_read:
    print(type(row))
    #dkey=row[1]
    #time_dict[dkey]=time_dict[dkey].extend(aSourceDictionary[aKey])
    
'''

### convert xls to csv format

from xlrd import open_workbook
import csv
wb = open_workbook('./data/sample.xlsx')

sheet = wb.sheet_by_index(1)
with open("./data/%s.csv" %(sheet.name.replace(" ","")), "w") as file:
    writer = csv.writer(file, delimiter = ",")
    print
    print
    print sheet, sheet.name, sheet.nrows
    header = [cell.value for cell in sheet.row(0)]
    writer.writerow(header)
    for row_idx in range(1, sheet.nrows):
        row = [int(cell.value) if isinstance(cell.value, float) else cell.value for cell in sheet.row(row_idx)]
        writer.writerow(row)
            
