import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from the CSV file into a DataFrame
df = pd.read_csv('/home/taya/a2-DataVis-5Ways-yakovenko/penglings.csv')

# Plot the data using Seaborn
sns.scatterplot(data=df, x='bill_length_mm', y='bill_depth_mm')

# Add title and labels
plt.title('Line Plot of Data from CSV')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()
