def loading_data():
    # import required libraries
    import pandas as pd
    # code to load data
    train = pd.read_csv("dataset/train.csv")
    test = pd.read_csv("dataset/test.csv")
    return train, test

def preprocessing(train, test):
    # code for data preprocessing
    print("Train dataset\n",train.columns)
    print("Test dataset\n",test.columns)

    pass

def main():
    # main code
    # load the dataset
    train, test = loading_data()

    # preprocess the dataset
    preprocessing(train, test)

    pass

if __name__ == "__main__":
    main()