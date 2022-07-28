import csv
import datetime
import shutil
from tempfile import NamedTemporaryFile

def get_length(file_path):
    with open("data.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        return len(reader_list)

def append_data(file_path, name, email, amount):
    fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date']
    next_id = get_length(file_path)
    with open(file_path, "a", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
                "id": next_id,
                "name": name,
                "email": email,
                "sent": "",
                "amount": amount,
                "date": datetime.datetime.now()
            })

append_data("data.csv", "JW", "hello@gmail.com", 123.23)
