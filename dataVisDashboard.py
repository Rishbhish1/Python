import matplotlib.pyplot as plt                     #  library for creating static, animated, and interactive visualizations 
import seaborn as sns                               # library based on Matplotlib that provides a high-level interface for drawing attractive statistical graphics
import pandas as pd                                 # data manipulation

# Load the Iris dataset
df = sns.load_dataset('iris')                       # add file path if needed in '' (csv file)

# Create a figure with multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 10))    # 2x2 grid of subplots, size of the entire figure to 15 inches by 10 inches.

# !Plot 1: Scatter plot of Sepal Length vs Sepal Width
sns.scatterplot(data=df, x='sepal_length', y='sepal_width', hue='species', ax=axes[0, 0])
axes[0, 0].set_title('Sepal Length vs Sepal Width')

# !Plot 2: Boxplot of Sepal Length
sns.boxplot(data=df, x='species', y='sepal_length', ax=axes[0, 1])
axes[0, 1].set_title('Boxplot of Sepal Length by Species')

# !Plot 3: Histogram of Petal Length
sns.histplot(data=df, x='petal_length', hue='species', multiple='stack', ax=axes[1, 0])
axes[1, 0].set_title('Histogram of Petal Length')

# !Plot 4: Pairplot
sns.pairplot(df, hue='species')
axes[1, 1].set_title('Pairplot')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
