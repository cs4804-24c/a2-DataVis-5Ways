import pandas as pd

def load_data(path):
    data = pd.read_csv(path)
    return data.head()

#Load file
data = load_data('./penglings.csv')

print(data.info())