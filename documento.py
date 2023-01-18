import csv
with open('estudiantes.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print("{0},{1},{2},{3},{4},{5},{6}".format(row[0], row[1], row[2], row[3], row[4], row[5],row[6]))

