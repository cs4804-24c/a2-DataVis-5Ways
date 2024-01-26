
![penguins](https://github.com/cs4804-24c/a2-DataVis-5Ways/assets/412089/accc5680-3c77-4d29-9502-d3ff8cd922af)

# 02-DataVis-5ways

Assignment 2 - Data Visualization, 5 Ways  
===

# altair + python + jupyter notebooj

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

## Design achievements: I matched the colors to the example by scanning for the exact RGB code. I used ggplot2's scale_color_manual and passed the RGB codes.

# VegaLite

![VegaLaite](img/<Vega.png>)

Vega-Lite is a high-level grammar of interactive graphics.

To visualize the penglings dataset, I used vega-lite's encoding function to define each data field and its type. Note, the dataset in vegalite is called penguins.csv
