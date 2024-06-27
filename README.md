# CSV Processing Script

This Python script processes a CSV file by performing the following operations:
- Replaces NaN values with empty strings
- Deletes columns where all values are "0" or "0.0" after the first two rows
- Appends the second data row to column headers with a space
- Deletes the second data row (original third row)
- Converts values to numbers and rounds them to 2 decimal places for all columns except the first
- Saves the processed data to a new CSV file

## Installation

To install the necessary dependencies, run:

```bash
pip install pandas
