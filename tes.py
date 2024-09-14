# Get the number of rows for the top half of the diamond
rows = int(input("Enter the number of rows (for the top half of the diamond): "))

# Top half of the diamond (including middle)
for i in range(1, rows + 1):
    # Print leading spaces
    print(' ' * (rows - i), end='')
    # Print increasing numbers
    for j in range(1, i + 1):
        print(j, end='')
    # Print decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end='')
    # Move to the next line
    print()

# Bottom half of the diamond
for i in range(rows - 1, 0, -1):
    # Print leading spaces
    print(' ' * (rows - i), end='')
    # Print increasing numbers
    for j in range(1, i + 1):
        print(j, end='')
    # Print decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end='')
    # Move to the next line
    print()
