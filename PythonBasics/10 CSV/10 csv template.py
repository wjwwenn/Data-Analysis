import csv

# there is a row spacing between
# -     writer.writerow(["Col 1", "Col 2"])
# -     writer.writerow(["Data 1", "Data 2"])
# The csv.writer writes \r\n into the file directly.
# If you don't open the file in binary mode, it will write \r\r\n because on Windows text mode will translate each \n into \r\n.
# solution: newline = ''

with open("data.csv", "w+", newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Col 1", "Col 2"])
    writer.writerow(["Data 1", "Data 2"])
    
with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

# ---------------------------------------------------------------------
with open("data.csv", "a") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Data 3", "Data 4"])
    
with open("data.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        
# ---------------------------------------------------------------------
with open("data.csv", "w", newline = '') as csvfile:
    fieldnames = ["id", "title"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"id":123, "title":"New title"})

with open("data.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
    