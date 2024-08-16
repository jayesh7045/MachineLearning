import csv
with open("example.csv", mode = "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow("Go away!");
    writer.writerow(['name', "Patil Saheb"])

with open("example.csv", mode = "r") as file:
    reader = csv.reader(file);
    for row in reader:
        print(row)
    