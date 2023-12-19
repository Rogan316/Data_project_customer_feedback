from Data_loader import load_data
from data_analysis import get_basic_statistics, get_rating_counts
from visualizations import plot_category_counts_bokeh, plot_rating_histogram

df = load_data('C:\\Users\\Rogan\\Documents\\Rogans Python projects for Github\\Data Project - Customer feedback\\customer_feedback.csv')
print (get_basic_statistics(df))
print(get_rating_counts(df))

df = load_data('C:\\Users\\Rogan\\Documents\\Rogans Python projects for Github\\Data Project - Customer feedback\\customer_feedback.csv')
plot_rating_histogram(df)
plot_category_counts_bokeh(df)