import pandas as pd

def load_data():
    df = pd.read_csv("Data/features_30_sec.csv")  # capital D
    
    print("Shape:", df.shape)
    print("\nColumns:\n", df.columns)
    print("\nFirst rows:\n", df.head())

    return df

if __name__ == "__main__":
    load_data()