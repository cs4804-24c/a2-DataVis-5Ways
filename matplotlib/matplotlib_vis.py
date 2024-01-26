import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import mplcursors

def main():
    df = pd.read_csv("penglings.csv").dropna()

    plt.figure(figsize=(15, 10))

    # Enable background grid
    sns.set_style("darkgrid")
    
    # Scatterplot
    penglings_plot = sns.scatterplot(
        data=df, 
        x='flipper_length_mm', 
        y='body_mass_g', 
        hue='species', 
        size='bill_length_mm',
        alpha=0.7)

    plt.title("Penglings")
    plt.xlabel("Flipper Length (mm)")
    plt.ylabel("Body Mass (g)")

    # Adjust Legend position
    penglings_plot.legend(loc='upper right', bbox_to_anchor=(1.133, 1.009))

    # Add an interactive hover over data points
    mplcursors.cursor(hover=True).connect(
        "add",
        lambda sel: (
            sel.annotation.set_text(f"Species: {df.loc[sel.target.index, 'species']}\nBill Length: {sel.artist.get_sizes()[0]}"),
            sel.annotation.set_backgroundcolor('#add8e6')
        ))

    plt.show()

if __name__ == "__main__":
    main()
