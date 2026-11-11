import csv
import sys


def main():
    if len(sys.argv) < 3:
        print("Usage: python reader.py <input_file> <output_file> <change_1> ...")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    changes = sys.argv[3:]

    try:
        with open(input_file_path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            data = [row for row in reader]
    except FileNotFoundError:
        print(f"Error: Input file '{input_file_path}' not found.")
        sys.exit(1)

    for change in changes:
        parts = change.split(",")
        if len(parts) != 3:
            continue

        x = int(parts[0])
        y = int(parts[1])
        value = parts[2]

        if 0 <= y < len(data):
            while len(data[y]) <= x:
                data[y].append("")
            data[y][x] = value

    for row in data:
        print(",".join(row))

    with open(output_file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)


if __name__ == "__main__":
    main()
