
![penguins](https://github.com/cs4804-24c/a2-DataVis-5Ways/assets/412089/accc5680-3c77-4d29-9502-d3ff8cd922af)

# 02-DataVis-5ways

Assignment 2 - Data Visualization, 5 Ways  
===

# altair + python + jupyter notebook

![Altair graph](img/<altair.png>)

Python is a general-purpose programming language. Altair is a visualization library in Python. Jupyter Notebook is a web-based interactive computing platform that creates interactive notebook documents containing live code, equations, visualizations, media, and other computational outputs. 

To visualize the penglings dataset, I used altair's Chart.encode() method. This allows easy encoding of the data.

Documentation was easy to find, and my previous experience in Python also made this visualizion very easy to make. 

## Design achievements: I matched the colors to the example by scanning for the exact RGB code. I used altair's domain and range parameters with the scale method to assign my own colors. I also added a title and subtitle, which involved passing the title keyword argument with data.
## Technical achievements: My visualization is interactive. You can pan and zoom on the chart. This is done using interactive(). 

# ggplot2 + R + RStudio

![ggplot2](img/<ggplot2.png>)

R is a programming language for statistic programming and data visualization. RStudio is an integrated development environment for R and Python. ggplot2 is a R package dedicated to data visualization

To visualize the penglings dataset, I used ggplot2's geom_point() function. 

Documentation was easy to find, this visualizion was easy to make. 

## Design achievements: I matched the colors to the example by scanning for the exact RGB code. I used ggplot2's scale_color_manual and passed the RGB codes.

# VegaLite

![VegaLite](img/<Vega.png>)

Vega-Lite is a high-level grammar of interactive graphics.

To visualize the penglings dataset, I used vega-lite's encoding function to define each data field and its type. Note, the dataset in vegalite is called penguins.csv

Documentation was easy to figure out, and it was fun to figure out how to make the visualization.

# Flourish

Flourish provides templates to make data visualizations without code.

To visualize the penglings dataset, I selected scatterplot from flourish's list of templates and imported the csv in. 

Flourish was the easiest to use, but there were some parts I found difficult to customize. It is definitely helpful if you have to make a quick visualization. 

![Flourish](img/<flourish.png>)

# d3 + javascript + visual studio code

![d3](img/<d3.png>)

D3 is a free, open-source JavaScript library for visualizing data. JavaScript is a programming language used to develop web pages. Visual studio code is source code editor. 

To visualize the penglings dataset, I began with creating and svg. I then read the penglings csv with, d3.csv('penglings.csv').then(data => {...}. I then define the dimensions of the plot and create an SVG with those dimensions. Next, I create the scales for the x and y axis, color, size, and opacity. These give me control to map the data values to the corresponding need. Then, I append the x and y-axis, as well as its labels. I also have a species and size legend. 

This was the most difficult visualization to make, as I have no previous javascript experience. 
