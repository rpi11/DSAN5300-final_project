import os
import pandas as pd

def read_datasets():
    retDict = {}

    for file in os.listdir("data"):
        if file != "winequality.csv":
            with open(f"data/{file}", "r") as f:
                df = pd.read_csv(f)
            retDict[file.split(".")[0]] = df
    
    return retDict

def get_subsets(df):
    train = df[df["train_test"] == "train"]
    test = df[df["train_test"] == "test"]

    X_train, y_train = train[[c for c in train.columns if c not in ["quality","train_test"]]], train["quality"]
    X_test, y_test = test[[c for c in test.columns if c not in ["quality","train_test"]]], test["quality"]

    return X_train, X_test, y_train, y_test