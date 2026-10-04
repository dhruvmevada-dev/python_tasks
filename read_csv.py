import csv
import sys


def read_csv_file(filename):
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        return list(reader)


def print_table(rows):
    if not rows:
        print("The file is empty.")
        return
    widths = [max(len(row[i]) for row in rows if i < len(row)) for i in range(len(rows[0]))]
    for n, row in enumerate(rows):
        print(" | ".join(cell.ljust(widths[i]) for i, cell in enumerate(row)))
        if n == 0:
            print("-+-".join("-" * w for w in widths))


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "students.csv"
    try:
        print_table(read_csv_file(filename))
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
