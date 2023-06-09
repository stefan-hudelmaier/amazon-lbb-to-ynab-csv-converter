import csv
import sys
import csv

filename = sys.argv[1]

if __name__ == '__main__':
    print('"Date";"Payee";"Memo";"Amount"')
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        line_number = 0
        for line in reader:
            if line_number == 0:
                line_number += 1
                continue
            for row in reader:
                if len(row) < 9:
                    continue
                date = row[1]
                month = date.split('.')[1]
                day = date.split('.')[0]
                year = date.split('.')[2]
                trader = row[3]
                amount = row[8].replace(',', '.')

                print(f'"{year}-{month}-{day}";"Amazon";"{trader}";"-{amount}"')
