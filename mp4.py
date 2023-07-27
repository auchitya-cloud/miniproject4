import csv

def add_marks(input_file, output_file):
    marks_dict = {}

    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) 
        for row in reader:
            if len(row) == 2:
                roll_number, marks = row[0].strip(), int(row[1].strip())
                marks_dict[roll_number] = marks_dict.get(roll_number, 0) + marks

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')
        writer.writerow(['Roll Number', 'Marks'])
        for roll_number, marks in marks_dict.items():
            writer.writerow([roll_number, marks])

if __name__ == "__main__":
    input_file = "/Users/auchitya/VS pro/summer school/input.csv"  
    output_file = "output.csv"  
    add_marks(input_file, output_file)
    print("Marks for each roll number have been summed and written to the output file.")

