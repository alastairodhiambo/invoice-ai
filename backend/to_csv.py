import json
import csv

CSV_FILE = 'Structured_Data.csv'


def json_to_csv(json_string):
    jsondata = []
    jsondata.append(json.loads(json_string))

    row_count = 0
    with open(CSV_FILE, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row if present

        for row in csv_reader:
            row_count += 1

    # # now we will open a file for writing
    data_file = open(CSV_FILE, 'a')

    # # create the csv writer object
    csv_writer = csv.writer(data_file)

    for data in jsondata:
        row = [row_count] + list(data.values())
        csv_writer.writerow(row)

    data_file.close()
