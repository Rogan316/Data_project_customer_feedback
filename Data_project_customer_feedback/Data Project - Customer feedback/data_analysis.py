import pandas as pd

def get_basic_statistics(df):
    return df.describe()

def get_rating_counts(df):
    return df['Rating'].value_counts()

if __name__ == '__main__':
    # Example usage
    data_path = os.path.join('data', 'customer_feedback.csv')
    df = pd.read_csv(data_path)
    print(get_basic_statistics(df))
    print(get_rating_counts(df))
