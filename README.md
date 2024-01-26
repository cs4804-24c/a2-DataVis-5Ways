
# Assignment 2 - Data Visualization, 5 Ways

# R + ggplot2
![Screenshot 2024-01-25 at 11.11.35 PM.png](R%20%2B%20ggplot2%2FScreenshot%202024-01-25%20at%2011.11.35%20PM.png)
![Screenshot 2024-01-25 at 11.11.52 PM.png](R%20%2B%20ggplot2%2FScreenshot%202024-01-25%20at%2011.11.52%20PM.png)

For one of my language requirements I used R with ggplot 2. This was not that difficult to figure out, but I think I am
biased because we had a lot of help from Professor Harrison's example in class. Once I got the data loaded, I got the 
code working pretty easily. I was also able to get my technical feature working pretty easily because there were a lot 
of different ways I was able to try looking online. The only time I had to get more hacky was with my technical feature.
I had to make the graph go into the shiny app in order to get the tooltips to work correctly. I could see this tool 
being useful in the future because of how many options there are for it. You can create so many things, and I really 
like how the graph shows up right next to it in RStudio instead of appearing in a separate window. 

Technical Achievement:
I used tooltips to create an interaction with each of the data points. When the user mouses over each of the data
points, they are able to see the species, flipper length, body mass, and bill length. This allows the user to see all
the information about each individual point by simply mousing over it.

Design Achievement:
My tool tips are also my design achievement. Tooltips give the user additional functionality making the information they
are seeing more clear. With the tooltips the user is able to find out exact information about every point, making the
data extra meaningful and useful for them. I also kept consistent font throughout the graph. By keep the font the same
for all aspects of the vis, there are not any distractions from the data being presented.

Sources: 
Professor Harrison's example and
https://stackoverflow.com/questions/38917101/how-do-i-show-the-y-value-on-tooltip-while-hover-in-ggplot2

# d3
![Screenshot 2024-01-25 at 10.20.06 PM.png](d3%2FScreenshot%202024-01-25%20at%2010.20.06%20PM.png)
![Screenshot 2024-01-25 at 10.20.25 PM.png](d3%2FScreenshot%202024-01-25%20at%2010.20.25%20PM.png)

For one of my language requirements I used Javascript with d3. I think this was the most difficult to figure out. I had 
a hard time loading my data for a while, and am still not really sure how I fixed it. I was first trying to reference 
the csv that I have in the project folder instead of the one on GitHub, but I had to switch it to make it work. I feel 
like the tool is very useful for more experienced data vis creators because there is a lot of ways to personalize the 
content. I also think that this makes the tool a little more difficult to use, so in the future I think this tool is 
going to be good for more professional data vis creators. Some hacks I did use were manipulating the domain of the x and 
y-axis to make all the data fit on the visualization. The data was going off of the sides and the top and bottom, so I 
had to change them slightly, so it was all within the right area.

Sources:
https://stackoverflow.com/questions/37654596/d3-js-appending-tooltip-to-each-data-circle-point-and-finding-on-hover-event-for and
https://d3-graph-gallery.com/graph/custom_theme.html#ggplot2

Technical Achievement:
I used tooltips to create an interaction with each of the data points. When the user mouses over each of the data
points, they are able to see the species, flipper length, body mass, and bill length. This allows the user to see all
the information about each individual point by simply mousing over it.

Design Achievement:
My tool tips are also my design achievement. Tooltips give the user additional functionality making the information they
are seeing more clear. With the tooltips the user is able to find out exact information about every point, making the 
data extra meaningful and useful for them. I also kept consistent font throughout the graph. By keep the font the same 
for all aspects of the vis, there are not any distractions from the data being presented. 

# Altair
![Screenshot 2024-01-25 at 9.42.23 PM.png](Altair%2FScreenshot%202024-01-25%20at%209.42.23%20PM.png)
![Screenshot 2024-01-25 at 9.42.36 PM.png](Altair%2FScreenshot%202024-01-25%20at%209.42.36%20PM.png)

For one of the language requirements I coded in Python using Altair. I thought Altair was very easy to use once I had it 
set up. It was very difficult for me to get everything downloaded and working at first. I tried to code this originally 
in VSCode, but ended up having to switch to Jupyter Notebook because I was having too many installation issues. 
Thankfully everything worked once I transferred it over to Jupyter. I found it very easy to create the graph because 
there were many online resources explaining how to change features and utilize tooltips. One thing I wished I was able 
to fix was the size of the circles. They are mapped to the bill length, but it is not super obvious which are different
sizes. The circles are different sizes if you look closely, but none of my manipulations worked to make the difference
more apparent. Some hacks I did use were manipulating the domain of the x and y-axis to make all the data fit on the 
visualization. The data was going off of the sides and the top and bottom, so I had to change them slightly, so it was 
all within the right area. I could definitely see this tool being useful in the future given how easy it was to figure
out. I felt like I was able to accomplish a lot and add a lot of functionality without running into much trouble. 

Sources I used to help make the graph:
https://altair-viz.github.io/gallery/scatter_tooltips.html, 
https://altair-viz.github.io/altair-viz-v4/user_guide/troubleshooting.html#:~:text=If%20you%20are%20expecting%20a,display%20properly%20or%20at%20all, 
https://stackoverflow.com/questions/52223358/rename-tooltip-in-altair, and
https://stackoverflow.com/questions/57695261/changing-the-size-of-altair-plot-renders-in-jupyter-notebook

Technical Achievement: 
I used tooltips to create an interaction with each of the data points. When the user mouses over each of the data 
points, they are able to see the species, flipper length, body mass, and bill length. This allows the user to see all 
the information about each individual point by simply mousing over it. 

Design Achievement: 
I have legends on the graph. The legends add clarity to the graph allowing the user to see what the colors and sizes
of each point means. By adding a legend, a lot more information is conveyed to the user. I also used consistent styling
throughout the graph. By making sure all the text was the same font and presented the same way, there is additional 
clarity to the graph. 

# Excel

![Screenshot 2024-01-23 at 11.20.17 PM.png](img%2FScreenshot%202024-01-23%20at%2011.20.17%20PM.png)

For one of my tools I used Excel. It was pretty easy to create the plot after the initial learning curve of 
understanding how to use the tool. I first had to relearn how to put multiple different plots on the same graph which 
took some playing around with tools. I then had to figure out that I needed to make it with a bubble plot instead of a 
scatter plot in order to make the points different sizes based on bill length. I also had to play around with the scale
of the bubbles because if you scaled using the area of the bubbles, all the bubbles would look the same, so you had 
to make sure you were scaling by the width of the bubbles. Additionally, I had to guesstimate the colors for the bubbles
because it would not let me enter a hex value to make them the exact color as the example graph. Some things I was not 
able to do in Excel were adding additional margin lines.I was only able to have margins where there was an interval on
the axis, so my chart has less margin lines. I was also not able to make the first and last axis points (3000 and 6000)
start slightly after and end slightly before the end of the graph (mow there is extra room on the original graph), so 
on my graph the visual starts right at 3000 and ends right at 6000. I can see this tool being very useful because it is 
both easy to use and fairly easy to learn. Once you learn how to use the features, making a graph is easy. It is also 
useful because it does not require knowing how to code, so it can be used by the general public. 

Technical Achievement: 
My technical achievement for my Excel graph was adding a legend, background color, and changing the color of the 
margins. I was able to more closely replicate the original graph by figuring out how to add a legend to the side, change
the background to light gray, and change the margin lines to be white. 

Design Achievement: 
My design achievement for my Excel graph was using a consistent styling for the words within the graph. I made sure to 
keep my graph consistent by using Times New Roman for all the features within the graph. I also made sure the axis 
titles and legend titles were bold so that they drew more attention, while keeping the axis labels regular so they did
not have as much emphasis. 

# Tableau
![Screenshot 2024-01-25 at 11.20.21 PM.png](Tableau%2FScreenshot%202024-01-25%20at%2011.20.21%20PM.png)
![Screenshot 2024-01-25 at 11.20.38 PM.png](Tableau%2FScreenshot%202024-01-25%20at%2011.20.38%20PM.png)

For one of my tools I used Tableau. It was pretty easy to create the plot. The entire process of uploading the data and 
creating the different aspects of the graph were all very simple. I did not have to use any hacks because the site was
so simple. I could see this being very useful in the future because of how easy it was to use. It does not require any 
code, and you can create a very elegant visualization very simply. I found this much easier to create more interesting 
features than in Excel. 

Technical Achievement: 
My Tableau graph has popovers displaying details of each of the data points. This allows the user to see the exact 
information about each individual point. I was able to more closely replicate the original graph by having a legend on 
the side. 

Design Achievement:
I have legends on the graph. The legends add clarity to the graph allowing the user to see what the colors and sizes
of each point means. By adding a legend, a lot more information is conveyed to the user. I also used consistent styling
throughout the graph. By making sure all the text was the same font and presented the same way, there is additional
clarity to the graph.

# Technical Achievements
I had different technical achievements for each of my graphs, though most of them were very similar. Most of my 
technical achievements included adding tooltips to the graph so that all the data for each given point would appear when
it was hovered over. More details about the technical achievement for each graph can be found in the individual section
for each graph. 

# Design Achievements
I had different design achievements for each graph, though most of them are very similar. Most of my design achievements 
included adding tool tips and legends for user clarity. By adding these additional features, users are able to more 
easily and clearly understand the data they are looking at. Other design achievements I had included using consistent 
styling throughout the graph. By making sure all the text was the same font and presented the same way, there is 
additional clarity to the graph. Graphs need to be clear so there is no attention taken away from the data. More details 
about the design achievements for each graph can be found in the individual section for each graph. 


