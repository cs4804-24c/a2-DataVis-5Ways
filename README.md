
![penguins](https://github.com/cs4804-24c/a2-DataVis-5Ways/assets/412089/accc5680-3c77-4d29-9502-d3ff8cd922af)


# Google Sheets

![Google Sheet](/img/google_sheets.png)
Google sheets provides a simple way to take a CSV of data and plot it on a graph with no programming experience. I found it very simple to create the graph. I first selected the range and pressed insert -> chart. I had to modify a few settings, as certain columns were used for wrong parts of the graph. Once selecting the correct column, the graph was almost complete. I then changed the styling of each series to match the colors in the README example, and ensured they had 80% opacity. I then added in labels and a legend. Unfortunately, it was not possible to have Google Sheets generate a size legend for the bubbles, which represent the bill length. Additionally, I was not able to scale the bubbles down. Currently, they are to large to make out the actual bill size of each bubble because of the large amount of overlapping. 

## Design Achievment using Google Sheets
I was able to use the color selector tool in Google Sheets to match the colors directly provided in the example screenshot provided by the Professor.

# Flourish

![Flourish](/img/FlourishGraph.png)

For Flourish, I was easily able to create a similar graph to the example provided. This tool provided more flexibility than Google Sheets, and I did not need to look at any guides on how to use the tool. One notable difference was the ease of modifying the scaling of each individual scatter point. This prevented the overcrowding issue which occured within Google Sheets. I was unable to add a legend for the scale of each scatter point, similarly to Google Sheets. After using Flourish, I think it's good for simple graphs that look better than Google Sheets, but it's still limited with what parts of the graph can be modified. 

## Technical Achievment
I was able to add a popup box when a scatter point is clicked on.

![Popup](/img/popupExample.png)

# matplotlib

![Matplotlob](/img/matplotlibfigure.png)

For the first coding based scatter plot, I utilized matplotlib, and used pandas to load the CSV into python. To prevent issue with matplotlib, I first dropped all rows that had NAN as a value. To get the correct colors per plot, I had to setup a dictionary that contained the species and the hex color from each. Then, I had to iterate through each species in the CSV, and plot each unique species with the color defined in the dictionary. It was very easy setting the labels, legend and grid as they only required one function call each. Once the setup was finished, calling the show function gave the popup of the chart. I think matplotlib can be useful to make quick graphs from collected data within a python script, as most of the difficulty came from reading in the file and manipulating it to be easily handled by matplotlib. Configuring the graph was simple. 

## Design Achievment

- Added gridlines
- Moved the default legend location to not coverup any datapoints

## Technical Achievment

- Output figure to a png file when script is ran

# Altair

![Altair](/img/visualization.png)

For the second library, I used Altair which also utilized Python as the programming language. Differently, this generates an html page that the user can interact with. The final generated webpage can be viewed at the following link: https://markou.dev/a2-DataVis-5Ways/altair/test.html. I found Altair to be the easiest programming focused visualization library as it took the least amount of code. There were many premade functions that took care of a lot of the hard parts (unlike d3), such as: aligning axis labels, generating the legend, coloring based on species and setting the domain and range of each axis. I was able to create the final visualization rather quickly compared to other tools, and seems to be a quick and useful tool to generate engaging visualizations without much coding. This library didn't require any hacks to get it to generate how I wanted. 

## Technical Achievment
- Output figure to an html file

# d3

![d3 Chart](/img/d3chart.png)

Resources used:
- https://d3-graph-gallery.com/graph/scatter_basic.html
- Used my a1 submission as starter code

View created chart: https://markou.dev/a2-DataVis-5Ways/d3/

d3 was the most challenging library to use to make a scatter plot. This complicated setup madeway to easily configure the graph to be more customizable, such as adding a tooltip option to every scatter point. Using the d3 library, I was able to easily load the csv file in and iterate over the rows to generate each scatter point. Comparatively to other parts of D3, the library made it simple to add scaling and axes for charts. The biggest challenge I encountered was generating the legend, and adding labels for each axis. To get everything to fit into the SVG easily, I utilized the idea of defining margins as demonstrated in the d3-graph-gallery webpage. Coloring was done in a similar way to other libraries using a JSON object with the species name as a key and the hex color as the value. 

## Technical Achievments
- Tool tip popup when each scatter point is hovered. This follows the cursor as it moves on the point, and disappears when no scatter point is under the cursor. 