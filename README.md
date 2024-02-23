
![penguins](https://github.com/cs4804-24c/a2-DataVis-5Ways/assets/412089/accc5680-3c77-4d29-9502-d3ff8cd922af)

# 02-DataVis-5ways
Abigail Boafo 
Assignment 2 - Data Visualization, 5 Ways  

# R + ggplot2 + R Markdown
<img width="708" alt="Screen Shot 2024-02-23 at 3 24 25 PM" src="https://github.com/Aoboafo/a2-DataVis-5Ways/assets/101887879/edf275e0-0851-4ca0-822b-977541ba0cc2">
<img width="611" alt="Screen Shot 2024-02-23 at 3 24 40 PM" src="https://github.com/Aoboafo/a2-DataVis-5Ways/assets/101887879/be585b2f-7a71-406b-9321-92df22d9fbd2">

I used R + ggplot2 to create a scatter plot with points representing penguins, where the x-axis is flipper_length_mm, the y-axis is body_mass_g. Pink, purple and teal represent different penguin species, size represents bill_length_mm, and shapes differentiate species. What is really unique about this is that it splits the data into 3 categories based on the 3 islands. The second scatter plot focused on the association between flipper length and body mass for penguins with a specific range of bill lengths. 

# Data wrapped
<img width="772" alt="image" src="https://github.com/Aoboafo/a2-DataVis-5Ways/assets/101887879/32117cc2-f4c4-4a2a-b9c3-e8ec3e25fe2f">

Link to data wrapped https://datawrapper.dwcdn.net/wKD6M/1/ 
The data wrapped scatter plot has different shapes for the species as well as colors. It also includes the bill length sizes. What I found difficult about this one was that it was hard getting the graph to look like the example graph. Every time I would put the data for the graph into data wrapped it would come out messed up. But I eventually got it to work with trial and error. 

# Flourish
<img width="772" alt="Screen Shot 2024-02-23 at 3 23 38 PM" src="https://github.com/Aoboafo/a2-DataVis-5Ways/assets/101887879/4cbc312c-19d4-43ed-9f28-a17877467a81">

Link to flourish https://public.flourish.studio/visualisation/16611481/
I found flourish to be the simply to use out of all the ones that required no code. It was easy and straight foward.


# d3
<img width="772" alt="image" src="https://github.com/Aoboafo/a2-DataVis-5Ways/assets/101887879/d479f88c-0495-4a71-ab99-234cf1971022">

Link to d3 http://localhost:8000/d3.html
This HTML code uses D3.js to generate a scatter plot visualizing penguin data. The dataset was loaded from a CSV file and then filtered to retain entries where the flipper length is equal to or exceeds 170. The script then constructs an SVG container with defined dimensions and margins. Scales ,for the x-axis (flipper length), y-axis (body mass), and circle size (bill length). I used the basic color scale  using D3's ordinal scale and color scheme. The scatter plot used circles that were determined by the mapped dataset values. Two legends were made one for the species and another, representing bill lengths.

# Python 
<img width="780" alt="Screen Shot 2024-02-23 at 3 26 45 PM" src="https://github.com/Aoboafo/a2-DataVis-5Ways/assets/101887879/4230dc77-9beb-4bd6-9363-9d96664e14f1">

I used the imports Pandas and Matplotlib libraries to load the csv and dataset. This code visualizes the relationship between flipper length, body mass, and bill length of different penguin species. The scatter plot is generated with flipper length on the x-axis, body mass on the y-axis, and circles based on species (Adelie in blue, Chinstrap in orange, and Gentoo in green).

## Technical Achievements
I created the island column which allows for a separate view of the data for each island, providing a more detailed understanding of the distribution of penguin characteristics across different environments. I added a legend on the top right side of the python graph and it displays the species and bill length all in one legend. For the R + ggplot2 + R graph I created two seperate legends for bill length and species. The data wrapped and flourish graphs have diffrent shapes for diffrent speices such as diamonds, triangles and squares.

### Design Achievements
For the design aspect I used the professors example as a starting point for R and I changed the colors to be purple, pink and teal. For my D3 and python code I used filtering based on flipper length and a grid to improve the plots readability.

