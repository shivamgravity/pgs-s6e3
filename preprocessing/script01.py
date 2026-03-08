import pandas as pd

def loading_data():
    # code to load data
    train = pd.read_csv("../../dataset/train.csv")
    test = pd.read_csv("../../dataset/test.csv")
    return train, test

def preprocessing(df, type):
    # code for data preprocessing
    # Drop unnecessary column
    df = df.drop(columns=['id'])

    # Convert TotalCharges to numeric
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # Fill missing values
    df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

    # Convert binary categorical variables
    if type == 'train':
        binary_cols = [
            'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling', 'Churn'
        ]
    else:
        binary_cols = [
            'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling'
        ]

    for col in binary_cols:
        df[col] = df[col].map({'Yes': 1, 'No': 0})

    # Encode gender
    df['gender'] = df['gender'].map({'Male': 1, 'Female': 0})

    # One-hot encode remaining categorical columns
    df = pd.get_dummies(df, drop_first=True)
    
    return df

def main():
    # main code
    # load the dataset
    train, test = loading_data()

    # preprocess the dataset
    preprocessed_train = preprocessing(train, 'train')
    preprocessed_test = preprocessing(test, 'test')

    # Add id column back to preprocessed test set
    preprocessed_test['id'] = test['id']

    return preprocessed_train, preprocessed_test

if __name__ == "__main__":
    main()