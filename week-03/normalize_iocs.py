import csv

seen = set()

with open("IOC_Dataset.csv", "r") as f:
    reader = csv.reader(f)

    for row in reader:
        seen.add(row[0].lower())

print("Unique IOC:", len(seen))
