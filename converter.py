import pandas as pd
import argparse

def convert_csv_to_excel(input_file, output_file):
    try:
        # Read CSV file
        df = pd.read_csv(input_file)

        # Handle missing values
        for col in df.columns:
            if df[col].dtype == "object":
                df[col] = df[col].fillna("Not Available")
            else:
                df[col] = df[col].fillna(0)

        # Parse Date column if it exists
        if "Date" in df.columns:
            df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

        # Rename columns
        rename_dict = {
            "Name": "Student_Name",
            "Age": "Student_Age"
        }

        df.rename(columns=rename_dict, inplace=True)

        # Save as Excel
        df.to_excel(output_file, index=False)

        print(f"✅ Success! Excel file saved as '{output_file}'")

    except FileNotFoundError:
        print("❌ Error: Input CSV file not found.")

    except pd.errors.EmptyDataError:
        print("❌ Error: CSV file is empty.")

    except Exception as e:
        print(f"❌ Error: {e}")


# Command Line Arguments
parser = argparse.ArgumentParser(
    description="Convert CSV file to Excel file"
)

parser.add_argument(
    "-i",
    "--input",
    required=True,
    help="Input CSV file path"
)

parser.add_argument(
    "-o",
    "--output",
    required=True,
    help="Output Excel file path"
)

args = parser.parse_args()

convert_csv_to_excel(args.input, args.output)