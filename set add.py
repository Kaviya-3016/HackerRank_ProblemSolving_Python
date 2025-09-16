# Read the number of inputs (total number of country stamps)
n = int(input())

# Create an empty set to store unique country names
# A set automatically removes duplicates
stamp = set()

# Loop through 'n' times to read each country name
for i in range(n):
    country = input()     # take a country name as input
    stamp.add(country)    # add it to the set (duplicates are ignored automatically)

# Finally, print the total number of unique countries
print(len(stamp))
