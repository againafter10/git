
import csv

exampleFile = open('data.csv')
exampleReader = csv.reader(exampleFile)
data = list(exampleReader)
for i in data:
    print i

print
print
outputFile = open('output.csv', 'w')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputFile.close()

exampleFile = open('output.csv')
exampleReader = csv.reader(exampleFile)
data = list(exampleReader)
for i in data:
    print i
    
    
print
print




csvFile = open('example.tsv', 'w')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvWriter.writerow(['eggs', 'bacon', 'ham'])
csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
csvFile.close()