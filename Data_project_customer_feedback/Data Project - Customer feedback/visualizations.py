import matplotlib.pyplot as plt
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource
import os

def plot_rating_histogram(df, column='Rating'):
    plt.hist(df[column], bins=range(1, 7), edgecolor='black', align='left')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.xticks(range(1, 6))
    plt.show()

def plot_category_counts_bokeh(df, column='Product Category'):
    counts = df[column].value_counts()
    source = ColumnDataSource(data=dict(categories=counts.index.tolist(), counts=counts.values))
    
    p = figure(x_range=counts.index.tolist(), title=f"{column} Counts", toolbar_location=None, tools="")
    p.vbar(x='categories', top='counts', width=0.9, source=source)

    p.xaxis.axis_label = column
    p.yaxis.axis_label = "Count"
    
    show(p)

if __name__ == '__main__':
    import pandas as pd
    # Using relative path
    data_path = os.path.join('data', 'customer_feedback.csv')
    df = pd.read_csv(data_path)
    plot_rating_histogram(df)
    plot_category_counts_bokeh(df)
