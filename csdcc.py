import csv

def update_csv_file(input_file, output_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)  # Read all rows into a list

        # Copy the second row to the first row
        if len(rows) > 1:
            rows[0] = rows[1].copy()

        # Change the value of the third column (index 2) of the first row (header row)
        if len(rows) > 0:
            rows[0][2] = "ReqID"






        if len(rows) > 0 and len(rows[0]) > 0:
            rows[0][0] = "Detail"

        if len(rows) > 0 and len(rows[0]) > 1:
            rows[0][1] = "ReqKey"

        if len(rows) > 0 and len(rows[0]) > 3:
            rows[0][3] = "ReqName"

        if len(rows) > 0 and len(rows[0]) > 4:
            rows[0][4] = "BillRef"

        if len(rows) > 0 and len(rows[0]) > 5:
            rows[0][5] = "6"

        if len(rows) > 0 and len(rows[0]) > 6:
            rows[0][6] = "7"

        if len(rows) > 0 and len(rows[0]) > 7:
            rows[0][7] = "PayDate"

        if len(rows) > 0 and len(rows[0]) > 8:
            rows[0][8] = "CheckNum"

        if len(rows) > 0 and len(rows[0]) > 9:
            rows[0][9] = "PayMethod"

        if len(rows) > 0 and len(rows[0]) > 10:
            rows[0][10] = "Amount"

        if len(rows) > 0 and len(rows[0]) > 11:
            rows[0][11] = "AdjNotes"

        if len(rows) > 0 and len(rows[0]) > 12:
            rows[0][12] = "Payee"

        if len(rows) > 0 and len(rows[0]) > 13:
            rows[0][13] = "14"

        if len(rows) > 0 and len(rows[0]) > 14:
            rows[0][14] = "15"

        if len(rows) > 0 and len(rows[0]) > 15:
            rows[0][15] = "16"

        if len(rows) > 0 and len(rows[0]) > 16:
            rows[0][16] = "17"

        if len(rows) > 0 and len(rows[0]) > 17:
            rows[0][17] = "18"

        if len(rows) > 0 and len(rows[0]) > 18:
            rows[0][18] = "19"

        if len(rows) > 0 and len(rows[0]) > 19:
            rows[0][19] = "20"

        if len(rows) > 0 and len(rows[0]) > 20:
            rows[0][20] = "21"

        if len(rows) > 0 and len(rows[0]) > 21:
            rows[0][21] = "22"

        if len(rows) > 0 and len(rows[0]) > 22:
            rows[0][22] = "23"

        if len(rows) > 0 and len(rows[0]) > 24:
            rows[0][24] = "25"


        # Change the value of the 24th column (index 23) of the first row to "Account"
        if len(rows) > 0 and len(rows[0]) > 23:
            rows[0][23] = "Account"

        # Make changes to the desired columns starting from the second row
        for row in rows[1:]:
            # Copy first 8 characters of column P (16th column) to column I (9th column)
            if len(row) > 15:
                value_p = row[15]
                row[8] = value_p[:8]

            # Change value in column J (10th column) to "Check"
            if len(row) > 9:
                row[9] = "Check"

            # Add 1014 to column X (24th column)
            if len(row) > 23:
                value_x = row[23]
                if value_x.isdigit():
                    row[23] = str(int(value_x) + 1014)
                else:
                    row[23] = '1014'  # If the value is not a number, set it to 1014 directly

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print(f"Changes saved to {output_file}.")

# Example usage:
input_file = 'input.csv'
output_file = 'zBillPayReady.csv'
update_csv_file(input_file, output_file)







