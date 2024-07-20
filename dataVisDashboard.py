import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the Iris dataset
df = sns.load_dataset('iris')

# Create a figure with multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

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
