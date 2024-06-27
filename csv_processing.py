import pandas as pd

def process_csv(input_file_path, output_file_path):
    # Load the CSV file
    df = pd.read_csv(input_file_path)

    # Replace NaN values with empty strings
    df.fillna('', inplace=True)

    # Convert data to string
    df_str = df.astype(str)

    # Find and delete columns where all values are "0" or "0.0" after the first two rows
    subsequent_rows_str = df_str.iloc[2:]
    columns_to_delete = subsequent_rows_str.columns[(subsequent_rows_str == '0').all() | (subsequent_rows_str == '0.0').all()]
    df = df.drop(columns=columns_to_delete)

    # Take the second data row and append it to column headers with a space
    second_data_row = df.iloc[0]
    column_headers = df.columns.astype(str) + " " + second_data_row.astype(str)
    df.columns = column_headers

    # Delete the second data row (original third row)
    df = df.drop(df.index[0])

    # Convert values to numbers and round to 2 decimal places for all columns except the first
    df.iloc[:, 1:] = df.iloc[:, 1:].applymap(lambda x: round(float(x), 2) if isinstance(x, str) and x.replace('.', '', 1).isdigit() else x)

    # Save the result as a CSV file
    df.to_csv(output_file_path, index=False)

    print(f"Processed CSV data has been successfully saved to {output_file_path}")

if __name__ == "__main__":
    input_file_path = "path/to/your/input_file.csv"  # Change this to the path of your input CSV file
    output_file_path = "path/to/your/output_file.csv"  # Change this to the path where you want to save the output CSV file
    process_csv(input_file_path, output_file_path)
