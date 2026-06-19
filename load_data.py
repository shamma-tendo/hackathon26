import csv

users = []

with open("user_data.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["Age"] = int(row["Age"])
        row["Purchase_Amount"] = float(row["Purchase_Amount"])

        users.append(row)

print("Data loaded successfully!")
print("Number of records:", len(users))

print("\nFirst record:")
print(users[0])