import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.widgets import Slider, Button, RadioButtons
import pandas as pd

# Load data
url = '../penglings.csv'
df = pd.read_csv(url)

# Convert 'bill_length_mm' to numeric
df['bill_length_mm'] = pd.to_numeric(df['bill_length_mm'], errors='coerce')

# Had help from GitHub Copilot to generate the math, but it is just normalizing the bill values to a range of 0-1
# by shifting each value such that the minimum value is 0 and the maximum value is equal to the range, the dividing by the range
df['bill_length_mm'] = (df['bill_length_mm'] - df['bill_length_mm'].min()) / (df['bill_length_mm'].max() - df['bill_length_mm'].min())
df['bill_length_mm'] = df['bill_length_mm'] * 10  # Adjust the constant as needed

colors = {
    'Adelie': '#ff8d05',
    'Chinstrap': '#9934cc',
    'Gentoo': '#048b8c'
}

df['color'] = df['species'].map(colors)

df['bill_length_mm'] = pd.to_numeric(df['bill_length_mm'], errors='coerce')

df['shape'] = df['island'].map({
    'Biscoe': 'o',
    'Dream': 's',
    'Torgersen': '^'
})

print(df)


# Plot scatter plot
scatterPolt = plt.scatter(df['flipper_length_mm'], df['body_mass_g'], s=df['bill_length_mm']*10, c=df['color'], alpha=0.7)
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')


# Legend
legend_elements = [Line2D([0], [0], marker='o', color='w', label='Adelie',
                          markerfacecolor='#ff8d05', markersize=10),
                   Line2D([0], [0], marker='o', color='w', label='Chinstrap',
                          markerfacecolor='#9934cc', markersize=10),
                   Line2D([0], [0], marker='o', color='w', label='Gentoo',
                          markerfacecolor='#048b8c', markersize=10)]

# Add legend
plt.legend(handles=legend_elements, loc='upper left')

# Add radio buttons for island
axcolor = 'lightgoldenrodyellow'
bounding_box = [0.75, 0.11, 0.15, 0.15]
radio_island = RadioButtons(plt.axes(bounding_box), ('Biscoe', 'Dream', 'Torgersen', 'All'))




# on click event for radio buttons
def radio_clicked(label):
    if label == 'All':
        print(df)
        scatterPolt.set_offsets(df[['flipper_length_mm', 'body_mass_g']])
        scatterPolt.set_sizes(df['bill_length_mm']*10)
        scatterPolt.set_color(df['color'])
        scatterPolt.set_alpha(0.7)
    else:
        filtered_df = df[df['island'] == label]
        print(filtered_df)
        scatterPolt.set_offsets(filtered_df[['flipper_length_mm', 'body_mass_g']])
        scatterPolt.set_sizes(filtered_df['bill_length_mm']*10)
        scatterPolt.set_color(filtered_df['color'])
        scatterPolt.set_alpha(0.7)
        
    plt.draw()

radio_island.on_clicked(radio_clicked)

plt.show()