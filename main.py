import csv
from functools import reduce

# ==================================================
# PERSON 1: Load CSV file and parse data
# Kayuza
# ==================================================

users = []

with open("user_data.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["Age"] = int(row["Age"])
        row["Purchase_Amount"] = float(row["Purchase_Amount"])
        users.append(row)

# ==================================================
# PERSON 2: Filter users over 30 with purchases
# Shamma
# greater than $100 and extract their emails
# ==================================================

filtered_users = list(
    filter(
        lambda user: user["Age"] > 30 and user["Purchase_Amount"] > 100,
        users
    )
)

emails = list(
    map(
        lambda user: user["Email"],
        filtered_users
    )
)

# ==================================================
# PERSON 3: List comprehension for New York users
# Nakubulwa
# ==================================================

new_york_users = [
    f"{user['Name']}: {user['Age']}"
    for user in users
    if user["City"] == "New York"
]

# ==================================================
# PERSON 4: Calculate total purchases using reduce
# and find the top 5 oldest users
# Stella
# ==================================================

total_purchase_amount = reduce(
    lambda total, user: total + user["Purchase_Amount"],
    users,
    0
)

top_5_oldest = sorted(
    users,
    key=lambda user: user["Age"],
    reverse=True
)[:5]

# ==================================================
# PERSON 5: Integrate everything and format output
# Brady
# ==================================================

print("=" * 50)
print("USERS OVER 30 WHO SPENT MORE THAN $100")
print("=" * 50)

for email in emails:
    print(email)

print("\n" + "=" * 50)
print("NEW YORK USERS (Name: Age)")
print("=" * 50)

for user in new_york_users:
    print(user)

print("\n" + "=" * 50)
print("TOTAL PURCHASE AMOUNT")
print("=" * 50)

print(f"${total_purchase_amount:.2f}")

print("\n" + "=" * 50)
print("TOP 5 OLDEST USERS")
print("=" * 50)

for user in top_5_oldest:
    print(f"{user['Name']} ({user['Age']} years old)")