import csv

def delete_every_3rd_line(input_file, output_file):
    """
    Deletes every 3rd line from a CSV file.

    :param input_file: Path to the input CSV file.
    :param output_file: Path to the output CSV file with filtered lines.
    """
    try:
        with open(input_file, 'r', newline='', encoding='utf-8') as infile:
            reader = list(csv.reader(infile))  # Read the entire file into memory
            filtered_rows = [row for i, row in enumerate(reader, start=1) if i % 3 != 0]  # Exclude every 3rd row
            
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(filtered_rows)
        
        print(f"Processed file saved to {output_file}")
    
    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_csv = 'C:\\Users\\yezda\\OneDrive\\IOT\\FOP\\assignment4\\ratings.csv'  # Replace with your input file path
output_csv = 'C:\\Users\\yezda\\OneDrive\\IOT\\FOP\\assignment4\\ratings_shortened.csv'  # Replace with your desired output file path
delete_every_3rd_line(input_csv, output_csv)
