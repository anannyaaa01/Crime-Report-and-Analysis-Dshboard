import pandas as pd
import glob

path = r"C:/Users/HP/Downloads/incidents/crime/crime"  # or your correct path

csv_files = glob.glob(path + "/*.csv")

print(f"CSV Files Found: {csv_files}")

if not csv_files:
    print("No CSV files found. Check your path and file extension!")
else:
    merged_df = pd.concat([pd.read_csv(f, on_bad_lines='skip') for f in csv_files])
    merged_df.to_csv("merged_data.csv", index=False)
    print("Merging complete!")
