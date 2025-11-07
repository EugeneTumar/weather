import csv

def csv_write(data):
    with open('output.csv', 'w', newline='') as file:
        if len(data) > 0:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)