# Python + Altair

Python is a popular language for data analysis and visualization. It is useful for quick prototyping and readable code.</br>
Altair is a very popular data visualization library for Python.</br></br>

To visualize the Penglings dataset, the Chart(url) function. From here I was able to add a chain of function calls including </br>
.mark_circle() to specify that I want my makers for the scatter plot to be circles.</br>
.encode( parameters ) to specify parameters like, what data to use for the x and y axes, what data to use to control the size marker, and more.</br>
.interactive() to make the the plot click-and-draggable as well as give it the ability to zoom in and out</br>
.transform_filter() to interface with the linked count of records vs year graph.</br>
and more</br></br>

Technical Achievements: </br>
- Ability to control the years that are included the scatter plot through the linked count of records vs year graph</br>
- Ability to filter the results by species using the radio buttons in combination with the above</br>
- Ability to click and drag and zoom in and out of the scatter plot</br>
- Tooltip functionality

Design Achievements: </br>
- I think the choice to control the scatter plot, with the linked count of records vs year graph is intuitive and useful for the viewer/user. While this data set did not have much granular data over time (all of the data points only had year information over only 3 years), I think for a different data set this linked control could be even more useful/intuitive</br>
- Legends</br>
- Consistent color scheme (throughout all graphs in this project)

Demo Video:</br>


https://github.com/cehrensperger/a2-DataVis-5Ways/assets/19954402/be303680-2e24-4852-9025-034f452641f1






# Python + Matplotlib
Python is a popular language for data analysis and visualization. It is useful for quick prototyping and readable code.</br>
Matplotlib is a popular, Matlab-like library often used for more mathematical visualization but works for simple scatter plots as well</br></br>

The main idea of this visualization was to use pandas, a very popular data analysis library, to structure, access, and modify the data, plt.scatter() for the main scatter plot, and RadioButtons() for the radio buttons in the bottom right corner. Pandas was very useful for accessing and modifying data. Specifically, it was useful for easily normalizing and scaling the bill_length data so that the sizes of the circles were acceptable. </br></br>

### Difficulties
- It was somewhat effort intensive to get used to matplotlib specific practices like calling plt.scatter() and then plt.xlabel() as a separate call. I assume after calling plt.scatter(), matplotlib internally keeps track of which plot you were working with last and applies the xlabel() to it, but this was an unfamiliar concept to me.
- I also tried to alter the shape of the markers according to sex or island, but upon further investigation, it seems like this is relatively difficult to do in this library. The problem is that matplotlib is not designed to show multiple marker types in one plot so it would involve making a new plot for each marker type and combining them in some way.</br></br>

Technical Achievements: </br>
- Radio buttons to filter the data by island type
- Utilizing matplotlib and its unfamiliar practices
- Using pandas to alter the data
  -  ```df['bill_length_mm'] = (df['bill_length_mm'] - df['bill_length_mm'].min()) / (df['bill_length_mm'].max() - df['bill_length_mm'].min())```</br>
  -  ```df['bill_length_mm'] = df['bill_length_mm'] * 10  # Adjust the constant as needed```</br></br>
- Matplotlib functionality of panning, zooming, and saving the figure
  
Design Achievements: </br>
- Giving the user the option to filter by island type
- Consistent color scheme (across all graph type)
- Legend
- Displaying the circle sizes such that they are noticeably different but not very large or small</br></br>

Demo Video: </br>


https://github.com/cehrensperger/a2-DataVis-5Ways/assets/19954402/56549879-b2b3-4e35-806a-cd7ca2859923



# JavaScript + d3

JavaScript is a popular programming language used for web development.</br>
d3 is a popular JavaScript library used for data visualization at a relatively low level.</br></br>

To visualize the dataset in d3, the main parts were:</br>
- Asynchronously loading the data using d3.csv()
- Structuring the document with calls like select(), and append()
- Styling through .style() and changing attributes with .attr()
- Structuring the scatter plot itself with scaleLinear() and .append()'ing circles
- Using a label to act as a tooltip
- Implementing interactivity using .on()

Technical Achievements:
- Using a label tag as a tooltip, showing and hiding as necessary (as well as moving out of the way because even a hidden label blocks mouseover events) upon mouseover and mouseover and mouseout events.
- Scaling and square rooting bill_lengths so that the radius attribute does not vary too wildly (since adjusting the radius adjusts circle area non-linearly)
- Creating a legend for both species and bill length
</br></br>

Design Achievements:
- Color of the tooltip flows well with the other colors
- Consistent fonts
- Scaling the circle sizes so that they don't change too drastically
- Outlining the circle that currently has the tooltip
- Using the same color for the circle outline as the tooltip background</br></br>

Demo Video:</br>


https://github.com/cehrensperger/a2-DataVis-5Ways/assets/19954402/a6674b80-39ca-4d57-94c9-34e078faf364

# Power BI

The motivation for choosing Power BI came from multiple internship positions that I wanted to apply for, but required some form of Power BI or Microsoft Power Platform experience. It wasn't all that often that I saw this requirement, but it was often enough that this felt worth-while. I did not know what Power BI was at the time and this class introduced me to it with near perfect timing.</br>

It is a popular data visualization tool that does not require coding.</br></br>

The main idea for this was to simply upload the csv file and design a visualization from their default scatter plot.

### Difficulties
This got me pretty far very quickly in the beginning, but, like with both of the no-code tools I used, got much more difficult as I wanted to make small, specific changes. In both Flourish and Power BI, I found it very difficult to edit the data in any meaningful way within the software itself. This led to me creating a new csv with the proper scaled bill_lengths as I did for the previous visualizations using excel and re-uploading my data. Power BI seems to also have some other way of displaying transparent objects and so there a higher-degree of overlapping than desired.</br></br>

Technical Achievements:
- Scaleable x- and y-axis
- Linked, body mass by year visualization
- Scaling the bill_length data

Design Achievements:
- Color of body mass by year bars flow with other colors
- Thicker dashed tick marks to get a sense of the dimensions (the default tick marks were barely visible)
- Scaleable x- and y-axis
- Consistent color scheme (throughout all visualizations)</br></br>

Demo Video:</br>


https://github.com/cehrensperger/a2-DataVis-5Ways/assets/19954402/17fa5170-7ff3-4d72-a06f-8800330dd03d


# Flourish


Flourish a popular, online, no-code data visualization tool.</br>
The idea for using Flourish was similar to the idea for using Power BI. Use the default scatter plot and tweak as needed.</br></br>

Technical Achievements:
- Normalizing and scaling the bill length so that the circle sizes in the visualization are reasonable
- Automatic timeline slider
- Creating three separate charts for each island
- Species legend/filterer

Design Achievements:
- Allowing the user to toggle between 2007-2009 and all years combined (this was not default and took some doing)
- Consistent color scheme (throughout all visualizations)
- Three side-by-side charts for each island

Demo Videos:</br>
- Regular:

  
https://github.com/cehrensperger/a2-DataVis-5Ways/assets/19954402/54e49ef0-0040-411b-8798-76d3a353cc2c
- Three Islands:


https://github.com/cehrensperger/a2-DataVis-5Ways/assets/19954402/c1686715-3cda-437e-8de3-3d43c930b794

