
![penguins](https://github.com/cs4804-24c/a2-DataVis-5Ways/assets/412089/accc5680-3c77-4d29-9502-d3ff8cd922af)

# 02-DataVis-5ways

Assignment 2 - Data Visualization, 5 Ways  
===
# Excel
Excel is a powerful spreadsheet application used for organizing, formatting, and calculating data in a tabular format. To visualize this data, I needed to create a bubble chart with three series, one for each species of pengling, with the x values being the flipper length and the y values being the body mass. Also, I needed to add the bill length to each series to correspond to the size of the data points.

Also, I kept the color of the circles similar to the original image, and also changed the opacity so that you could somewhat see the data points that overlapped each other.

![Excel_Penglings_Image](https://github.com/joshj339/a2-DataVis-5Ways/assets/91641190/82880001-d232-49b7-bb70-5ba6353bb91a)

# Matlab
Matlab is a high-level programming language and interactive environment used for numerical computing, data analysis, algorithm development, and visualization. This data is loaded into my script, then the important data is mapped into variables (species, flipper length, body mass, and bill length). Also, each species is seperated using the "unique function", and a color is mapped to them. In creating the plot, a for loop is run using each unique species. The logical index array is used to filter the data that corresponds to the current species being plotted. Then, a scatter plot is created for the flipper length vs body mass, and the bill length determines the size, which can be increased or decreased at your own disgression by multiplying it by an arbitrary number. Then, the points are filled in and a name for each species is set, which is used in the legend. Findally, the opacity of each point is determined by "MarkerFaceAlpha" and can also be changed by using an arbitrary number (between 0 and 1, in this case 0.65).

The value of each data point can be seen when hovering over it, including the flipper length, body mass, and bill length.

![Matlab_Penglings_Image](https://github.com/joshj339/a2-DataVis-5Ways/assets/91641190/5469532a-660e-4cae-8f78-30ff76f36050)

# R + ggplot2

R is a language primarily focused on statistical computing.
ggplot2 is a popular library for charting in R.

The code first loads the ggplot2 library, and then reads the data from the csv file. The function ggplot creates an object with the dataset, with flipper length mapped to the x-axis, body mass to the y-axis, species to the color of the points, and bill length to the size of the points. geom_point adds a layer of points, and this is where the transparency is changed. Finally, the plot is directly saved to a file within the code through the ggsave function.

![R_Penglings_Image](https://github.com/joshj339/a2-DataVis-5Ways/assets/91641190/11f21ef3-ac7f-44e6-82e0-44644a595e5d)

# Altair

# D3

d3.js is a powerful JavaScript library for creating complex and interactive data visualizations for web browsers.

I was able to use a CDN link to include the d3 library into my html file without have to download the library myself. This allowed me to code using d3 within my html file.
First, I need to defined the SVG container where the scatter plot was be rendered. Then, using d3.js, I loaded my dataset Finally, you create circles (or other shapes) for each data point by appending SVG elements to the container, positioning them based on the flipper length and body mass, and their size determined by the bill size.

![d3_pengling_image](https://github.com/joshj339/a2-DataVis-5Ways/assets/91641190/98cc9db6-22a8-403f-9a49-52c44c00b83d)


## Technical Achievements

### Design Achievements

