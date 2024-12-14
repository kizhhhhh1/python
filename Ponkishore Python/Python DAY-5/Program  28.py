# Function to print the pattern
def print_pattern(rows):
    for i in range(1, rows + 1):
        # Generate the sequence for the current row
        row_values = [f"{j/10:.1f}" for j in range(1, i + 1)]
        # Print the row values joined by a space
        print(" ".join(row_values))

# Main execution
if _name_ == "_main_":
    try:
        num_rows = int(input("Enter the number of rows: "))
        print_pattern(num_rows)
    except ValueError:
        print("Please enter a valid integer.")
