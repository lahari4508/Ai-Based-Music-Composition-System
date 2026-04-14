import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def preprocess_data(df):
    # Remove filename (not useful for model)
    df = df.drop(['filename'], axis=1)

    # Features and labels
    X = df.drop('label', axis=1)
    y = df['label']

    # Convert text labels → numbers
    le = LabelEncoder()
    y = le.fit_transform(y)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Training data:", X_train.shape)
    print("Testing data:", X_test.shape)

    return X_train, X_test, y_train, y_test, le