# Read data from input file

with open("input.txt", "r") as file:
    lines = file.readlines()

# Count lines
print("Number of lines:", len(lines))

# Extract first two lines
first_two = lines[:2]

print("First two lines:")
for line in first_two:
    print(line, end="")

# Write first two lines to new file
with open("output.txt", "w") as file:
    file.writelines(first_two)

print("\nFirst two lines written to output.txt")
