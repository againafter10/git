# remove headers of all CSV files in a directory

import csv, os


os.makedirs('headersRemoved')


# Loop through every file in the current working directory.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue    # skip non-csv files
    print('Will Remove header from ' + csvFilename + '...')

    # TODO: Read the CSV file in (skipping first row).
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue    # skip first row
        csvRows.append(row)
    csvFileObj.close()
    
    #Now that csvRows contains all rows but the first row, the list needs to be written out to a CSV file in the headerRemoved folder. 

    csvFileObj = open(os.path.join('headersRemoved', csvFilename), 'w')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
    



       
