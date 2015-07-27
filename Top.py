def read_file():
    with open(Nelisa_Sales_History.csv, 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    return data
