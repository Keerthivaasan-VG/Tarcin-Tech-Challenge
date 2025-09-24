import csv

def clean_data(file_path):
    cleaned_records = []

    with open(file_path, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            record_id = row["ID"].strip()
            value = row["Value"].strip()

            # Validate value: must be a positive number
            if value.isdigit() and int(value) >= 0:
                cleaned_records.append({"ID": record_id, "Value": int(value)})

    return cleaned_records

if __name__ == "__main__":
    input_file = "records.csv"

    cleaned = clean_data(input_file)

    print("Cleaned Records (list of dicts):")
    for rec in cleaned:
        print(rec)

output
