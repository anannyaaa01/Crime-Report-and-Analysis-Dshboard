# add_new_crime.py

import pandas as pd

def add_new_crime(state, year, crime_type):
    new_record = {
        'State': state,
        'Year': year,
        'Crime_Type': crime_type
    }

    file_path = "C:\Users\HP\Downloads\crime_data.csv"

    # Append the new record to the dataset
    df = pd.read_csv(file_path)
    df = df.append(new_record, ignore_index=True)
    df.to_csv(file_path, index=False)

    print(f"[+] New crime added: {new_record}")
