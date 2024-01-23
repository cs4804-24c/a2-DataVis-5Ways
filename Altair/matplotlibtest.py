import pandas as pd

# Load data
url = '../penglings.csv'
df = pd.read_csv(url)

# Display basic statistics for 'bill_length_mm'
print(df['bill_length_mm'].describe())
