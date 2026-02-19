import csv
import random
from datetime import datetime, timedelta

NUM_ROWS = 10000  # change to 20000 if you want bigger

accounts = [f"A{i}" for i in range(1, 2001)]
start_time = datetime(2025, 1, 1, 10, 0, 0)

rows = []
t = start_time

# Normal random transactions
for i in range(NUM_ROWS - 500):
    sender = random.choice(accounts)
    receiver = random.choice(accounts)
    while receiver == sender:
        receiver = random.choice(accounts)
    amount = round(random.uniform(5, 500), 2)
    rows.append([f"t{i}", sender, receiver, amount, t.strftime("%Y-%m-%d %H:%M:%S")])
    t += timedelta(seconds=random.randint(1, 30))

# Add some cycles
for i in range(100):
    a, b, c = random.sample(accounts, 3)
    rows.append([f"c{i}_1", a, b, 50, t.strftime("%Y-%m-%d %H:%M:%S")])
    rows.append([f"c{i}_2", b, c, 40, (t + timedelta(seconds=5)).strftime("%Y-%m-%d %H:%M:%S")])
    rows.append([f"c{i}_3", c, a, 30, (t + timedelta(seconds=10)).strftime("%Y-%m-%d %H:%M:%S")])
    t += timedelta(seconds=20)

# Add fan-in (smurfing)
hub = "HUB_MAIN"
for i in range(200):
    sender = random.choice(accounts)
    rows.append([f"s{i}", sender, hub, random.uniform(1, 10), t.strftime("%Y-%m-%d %H:%M:%S")])
    t += timedelta(seconds=2)

# Add fan-out
src = "SRC_MAIN"
for i in range(200):
    receiver = random.choice(accounts)
    rows.append([f"f{i}", src, receiver, random.uniform(1, 10), t.strftime("%Y-%m-%d %H:%M:%S")])
    t += timedelta(seconds=2)

with open("large_test_dataset.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["transaction_id", "sender_id", "receiver_id", "amount", "timestamp"])
    writer.writerows(rows)

print("Generated large_test_dataset.csv with", len(rows), "rows")
