# R + ggplot2 + R

R is a language primarily focused on statistical computing.
ggplot2 is a popular library for charting in R.
R Markdown is a document format that compiles to HTML or PDF and allows you to include the output of R code directly in the document.

To visualized the cars dataset, I made use of ggplot2's `geom_jitter()` layer, with aesthetics functions for the size. For the color I mapped the species names directly to the colors of my choice 

It took some time to get used to all the syntax and figure out an approach to creating the chart by this was the easiest of the languages for me to pick up.

In order for it to pull the correct data, the path to `penglings.csv` will need to be adjusted since it is a global path for my personal laptop at the moment.

![ggplot2](img/ggplot2.png)

# d3

d3 was a bit more of a struggle for me. I spent lining up all the grid lines and doing the math with the margins to make sure everything lined up together. I used `d3.scaleLiner` to set up the chart axis. For the dots I used circles which were adjusted based on the data and placed within reference to the linear scale axis.

![d3](img/d3.png)

# Matlab

Matlab felt very similar to R but with some of it simplified to make it more straightforward. I used `scatter` to create the chart with surprisingly did not need much tinkering to work. I simply had to prepare some of the data because creating the chart. The only issue that I ran into with that was the color option for the chart would only accept numbers so I made a new array assigning each species to a number and I got it to work.

![matlab](img/matlab.png)

# Excel

Since excel is primarily for raw data and numbers, I had to manipulate the data a bit to make sure that it produce the chart I wanted. I separated the species into three different columns, only keeping the weight for the specifally species. I then used this to make three different series in the chart which could have different colors. To do the different sizes I used a bubble chart.

Excel was my least favorite to work with for creating the chart. Although it was create for viewing and manipulating the data, when it came to actually creating the chart it felt confusing and unintuitive.

![excel](img/excel.png)

# Tableau

Tableau was by far my favorite to work with. It did not take long for me to get the chart created once I started to understand the basics of the program. I simply uploaded the data, selected the scatter plot, and chose the axis. Then I dragged the corresponding tables onto color and size and was down after a bit of touch up.

My only issue with the program is it requires a license to use but that seems understandable with how straightforward it was to work with.

![tableau](img/tableau.png)


### Design Achievements
- When adjusting the size of the dots, I tried to keep the noticeable difference threshold in mind and make sure that there was a noticable difference by proportionally adjusting the data.
