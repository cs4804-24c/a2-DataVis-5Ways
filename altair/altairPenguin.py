import altair as alt
import pandas as pd

# Load the data
url = "https://raw.githubusercontent.com/cs4804-24c/a2-DataVis-5Ways/main/penglings.csv"
data = pd.read_csv(url)

# Print avg bill length, flipper length, and body mass
print("Average Bill Length:", penData["bill_length_mm"].mean())
print("Average Flipper Length:", penData["flipper_length_mm"].mean())
print("Average Body Mass:", penData["body_mass_g"].mean())

# Print population size of the 3 islands based on the species
print("Biscoe Adelie:", penData[(penData["island"] == "Biscoe") & (penData["species"] == "Adelie")].shape[0])
print("Biscoe Gentoo:", penData[(penData["island"] == "Biscoe") & (penData["species"] == "Gentoo")].shape[0])
print("Biscoe Chinstrap:", penData[(penData["island"] == "Biscoe") & (penData["species"] == "Chinstrap")].shape[0])

print("Dream Adelie:", penData[(penData["island"] == "Dream") & (penData["species"] == "Adelie")].shape[0])
print("Dream Gentoo:", penData[(penData["island"] == "Dream") & (penData["species"] == "Gentoo")].shape[0])
print("Dream Chinstrap:", penData[(penData["island"] == "Dream") & (penData["species"] == "Chinstrap")].shape[0])

print("Torgersen Adelie:", penData[(penData["island"] == "Torgersen") & (penData["species"] == "Adelie")].shape[0])
print("Torgersen Gentoo:", penData[(penData["island"] == "Torgersen") & (penData["species"] == "Gentoo")].shape[0])
print("Torgersen Chinstrap:", penData[(penData["island"] == "Torgersen") & (penData["species"] == "Chinstrap")].shape[0])

# Print total population size of the 3 islands
print("Biscoe Population:", penData[penData["island"] == "Biscoe"].shape[0])
print("Dream Population:", penData[penData["island"] == "Dream"].shape[0])
print("Torgersen Population:", penData[penData["island"] == "Torgersen"].shape[0])


# Chart dimensions
margin = {"top": 40, "right": 30, "bottom": 40, "left": 80}
width = 800 - margin["left"] - margin["right"]
height = 520 - margin["top"] - margin["bottom"]

# Create a selection for clicking on the chart
click_selection = alt.selection_multi(encodings=['color'])

# Create the Altair chart
chart = (
    alt.Chart(penData)
    .mark_point(filled=True, opacity=0.7)
    .encode(
        x = alt.X("flipper_length_mm", scale = alt.Scale(domain = [170, 235]), axis = alt.Axis(title = "Flipper Length (mm)", tickMinStep = 10)),
        y = alt.Y("body_mass_g", scale = alt.Scale(domain = [2500, 6300]), axis = alt.Axis(title = "Body Mass (g)", tickMinStep = 1000)),
        color = alt.Color("species:N", scale = alt.Scale(range = ["#4fb8b6", "#343483","#383b47"]), legend = alt.Legend(title="Species")),
        size = alt.Size("bill_length_mm:Q", scale = alt.Scale(range = [50, 600], type = "log")),
        shape = alt.Shape("island:N", scale = alt.Scale(range = ["circle", "triangle", "square"])),
        tooltip = ["species:N", "flipper_length_mm:Q", "body_mass_g:Q", "bill_length_mm:Q", "island:N"]
    )
    .properties(
        width = width + margin["left"] + margin["right"] + 150,
        height = height + margin["top"] + margin["bottom"] + 100,
        title = "Penguin Flipper Length(mm) vs. Body Mass(g)"
    )
    .configure_title(
        fontSize = 30,
        fontWeight = "bold",
        font = "Times New Roman",
        anchor = "start",
        offset = 30
    )
    .configure_axis(
        titleFont = "Times New Roman",
        titleFontSize = 20,
        labelFont = "Times New Roman",
        labelFontSize = 12,
        labelColor = "black",
        tickColor = "white"
    )
    .configure_legend(
        titleFont = "Times New Roman",
        labelFont = "Times New Roman",
        labelFontSize = 12
    )
    .add_selection(click_selection)
    .transform_filter(click_selection)
    .configure_view(
        strokeOpacity = 0,  # Remove the stroke around the points
        fill='#ededed'
    )
).interactive()

# Show the chart
chart