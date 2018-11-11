import csv

with open('elements.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
       
            print(f'Column names are {", ".join(row)}')
          
       
    print(f'Processed {line_count} lines.')