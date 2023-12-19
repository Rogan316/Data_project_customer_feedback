import matplotlib.pyplot as plt
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource

def plot_rating_histogram(df, column='Rating'):
    """
    Create a histogram of the specified column using Matplotlib.
    :param df: Pandas DataFrame containing the dataset.
    :param column: Column name to plot histogram for.
    """
    plt.hist(df[column], bins=range(1, 7), edgecolor='black', align='left')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.xticks(range(1, 6))
    plt.show()

def plot_category_counts_bokeh(df, column='Product Category'):
    """
    Create a bar chart of counts per category using Bokeh.
    :param df: Pandas DataFrame containing the dataset.
    :param column: Column name to plot bar chart for.
    """
    counts = df[column].value_counts()
    source = ColumnDataSource(data=dict(categories=counts.index.tolist(), counts=counts.values))
    
    p = figure(x_range=counts.index.tolist(), title=f"{column} Counts", toolbar_location=None, tools="")
    p.vbar(x='categories', top='counts', width=0.9, source=source)

    p.xaxis.axis_label = column
    p.yaxis.axis_label = "Count"
    
    show(p)

# This should be outside any function definitions
if __name__ == '__main__':
    import pandas as pd
    # Update this file path to the correct CSV file path
    df = pd.read_csv(r'C:\Users\Rogan\Documents\Rogans Python projects for Github\customer_feedback.csv')
    plot_rating_histogram(df)
    plot_category_counts_bokeh(df)
