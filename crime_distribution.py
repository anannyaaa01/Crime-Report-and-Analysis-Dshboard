# crime_distribution.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_crime_distribution(state_name):
    df = pd.read_csv('crime_data.csv')
    state_df = df[df['State'] == state_name]

    plt.figure(figsize=(10, 5))
    sns.countplot(data=state_df, x='Crime_Type', order=state_df['Crime_Type'].value_counts().index)
    plt.title(f"Crime Type Distribution in {state_name}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'saved_models/{state_name}_crime_distribution.png')
    plt.close()
