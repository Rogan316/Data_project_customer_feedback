from Data_loader import load_data
from data_analysis import get_basic_statistics, get_rating_counts
from visualizations import plot_category_counts_bokeh, plot_rating_histogram
import os

# Using relative path
data_path = os.path.join('data', 'customer_feedback.csv')

df = load_data(data_path)
print(get_basic_statistics(df))
print(get_rating_counts(df))

plot_rating_histogram(df)
plot_category_counts_bokeh(df)
