#sean's helper

from sklearn.model_selection import train_test_split
import pandas as pd



def helper1(X):
    """this will create new columns in the dataset
    for each time metric i.e. year, month, week, etc..."""
    
    # Prevent SettingWithCopyWarning
    X = X.copy()
    
    # Convert date_recorded to datetime
    X['Date'] = pd.to_datetime(X['Date '], infer_datetime_format=True)
    
    # Extract components from date_recorded, then drop the original column
    X['year'] = X['Date'].dt.year
    X['month'] = X['Date'].dt.month
    X['week'] = X['Date'].dt.week
    X['day'] = X['Date'].dt.day
    X['hour'] = X['Date'].dt.hour
    X['minute'] = X['Date'].dt.minute
    X['second'] = X['Date'].dt.second
    X = X.drop(columns='Date')

    # return the dataframe
    return X


def helper2(X):

    # Split train into train & val
    train_one, test = train_test_split(X, train_size=0.80, test_size=0.20,
                                   random_state=42)

    train, val = train_test_split(train_one, train_size=0.80, test_size=0.20, 
                          random_state=42)

    return train, val, test