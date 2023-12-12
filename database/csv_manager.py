import csv
import os


class CSVManager:
    def __init__(self, filename):
        self.filename = filename
        self.file_exists = os.path.exists(filename)

    def store_data(self, **kwargs):
        with open(self.filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=kwargs.keys())
            if not self.file_exists:
                writer.writeheader()
                self.file_exists = True
            writer.writerow(kwargs)

    def read_data(self):
        with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)

    def write_data(self, data):
        with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
