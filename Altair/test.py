import altair as alt
import pandas as pd

url = '../penglings.csv'

# Load data
df = pd.read_csv(url)

# Convert 'bill_length_mm' to numeric
df['bill_length_mm'] = pd.to_numeric(df['bill_length_mm'], errors='coerce')

# Create a bar chart for 'bill_length_mm'
bar_chart = alt.Chart(df).mark_bar().encode(
    alt.X('bill_length_mm:Q', bin=True),
    alt.Y('count():Q'),
)

bar_chart.save('bill_length_distribution.html')
