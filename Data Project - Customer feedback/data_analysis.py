import pandas as pd
def get_basic_statistics(df):
    """
    Count the number of occurrences of each rating.
    :param df: Pandas DataFrame containing the dataset.
    :return: Series with rating counts.
    """
    return df.describe()

def get_rating_counts(df):
    """
    Count the number of occurrences of each rating.
    :param df: Pandas DataFrame containing the dataset.
    :return: Series with rating counts.
    """
    return df['Rating'].value_counts()
    
# Optional main section for testing
if __name__ == '__main__':
    # Example usage
    df = pd.read_csv(r'\Users\Rogan\Documents\Rogans Python projects for Github')
    print(get_basic_statistics(df))
    print(get_rating_counts(df))