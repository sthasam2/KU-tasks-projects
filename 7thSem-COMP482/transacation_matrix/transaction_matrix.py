import csv

# Import data
with open("data/grocery_dataset.txt", "r") as input_file:
    transaction_data = [line[:-1].split(",") for line in input_file]

# Get items from imported data
item_set = set()
for doc in transaction_data:
    item_set = item_set.union(set(doc))
item_set = sorted(item_set)

# Create transaction matrix
final_matrix = []
for items in transaction_data:
    final_matrix.append([int(item in items) for item in item_set])

# Write matrix into file
with open("final_results.csv", "a") as output_file:
    writer = csv.writer(output_file, delimiter=",")
    writer.writerow(item_set)
    writer.writerows(final_matrix)
