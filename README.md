
![penguins](https://github.com/cs4804-24c/a2-DataVis-5Ways/assets/412089/accc5680-3c77-4d29-9502-d3ff8cd922af)

# 02-DataVis-5ways

Assignment 2 - Data Visualization, 5 Ways  
===

Now that you have successfully made a "visualization" of shapes and lines using d3, your next assignment is to successfully make a *actual visualization*... 5 times. 

The goal of this project is to gain experience with as many data visualization libraries, languages, and tools as possible.

I have provided a small dataset about penguins, `penglings.csv`.
Each row contains a penguin observation and several variables about it, including bill length, flipper length, and more.

Your goal is to use 5 different tools to make the following chart:

![](img/ggplot2.png)

These features should be preserved as much as possible in your replication:

- Data positioning: it should be a upward-trending scatterplot as shown.  Flipper Length should be on the x-axis and Body Mass on the y-axis.
- Scales: Note the scales do not start at 0.
- Axis ticks and labels: both axes are labeled and there are tick marks at a reasonable interval, e.g 10, 20, 30, etc.
- Color mapping to species.
- Size mapping to Bill Length.
- Opacity of circles set to 0.8 or similar for a semi-transparent effect.

Other features are not required. This includes:

- The background grid.
- The legends.

Note that some software packages will make it **impossible** to perfectly preserve the above requirements. 
Be sure to note where these deviate as you reflect on what a tool is good for.

Improvements are also welcome as part of Technical and Design achievements.

Libraries, Tools, Languages
---

You are required to use 5 different tools or libraries.
Of the 5 tools, you must use at least 3 libraries (libraries require code of some kind).
This could be `Python, R, Javascript`, or `Java, Javascript, Matlab` or any other combination.
Dedicated tools (i.e. Excel) do not count towards the language requirement.

Otherwise, you should seek tools and libraries to fill out your 5.

Below are a few ideas. Do not limit yourself to this list!
There are new tools coming out every year and we may not have an exhaustive list of the latest and greatest.

Some may be difficult choices, like Matlab or SPSS, which require large installations, licenses, and occasionally difficult UIs.

I have marked a few that are strongly suggested.

- R + ggplot2 `<- definitely worth trying`
- Excel
- d3 `<- since the rest of the class uses this, we're requiring it`
- Altair `<- hugely popular python library. highly recommended `
- three.js `<- well, it's a 3d library. not really recommended, but could be interesting and fun`
- p5js `<- good for playing around. not really a chart lib`
- Tableau
- PowerBI
- Vega-lite <- `<- very interesting formal visualization model; might be the future of the field`
- Flourish <- `<- popular in recent years`
- DataWrapper <- `<- popular in recent years`
- GNUplot `<- the former CS department head uses this all the time :)`
- SAS/SPSS/Matlab

You may write everything from scratch, or start with demo programs from books or the web. 
If you do start with code that you found, please identify the source of the code in your README and, most importantly, make non-trivial changes to the code to make it your own so you really learn what you're doing. 

Tips
---

- If you're using d3, key to this assignment is knowing how to load data.
You will likely use the [`d3.json` or `d3.csv` functions](https://d3js.org/d3-dsv) to load the data you found.

**Beware that these functions are *asynchronous*, meaning it's possible to "build" an empty visualization before the data actually loads. Figuring out how to do this properly can be a major hiccup if you haven't used async functions before. If this means you, start part of this project early so you don't end up in a rush!**

- *For web languages like d3* Don't forget to run a local webserver when you're debugging.
See my a1 video or online tutorials for how to do this.
Being able to host a local webserver is an essential web development skill and very common in visualization design as well.

Readme Requirements
---

A good readme with screenshots and structured documentation is required for this project. 
It should be possible to scroll through your readme to get an overview of all the tools and visualizations you produced.

- Each visualization should start with a top-level heading (e.g. `# d3`)
- Each visualization should include a screenshot. Put these in an `img` folder and link through the readme (markdown command: `![caption](img/<imgname>)`.
- Write a paragraph for each visualization tool you use. What was easy? Difficult? Where could you see the tool being useful in the future? Did you have to use any hacks or data manipulation to get the right chart?

Other Requirements
---

0. Your code should be forked from the GitHub repo.
1. Place all code, Excel sheets, etcetera in a named folder. For example, `r-ggplot, matlab, mathematica, excel` and so on.
2. Your writeup (readme.md in the repo) should also contain the following:

- Description of the Technical achievements you attempted with this visualization.
  - Some ideas include interaction, such as mousing over to see more detail about the point selected.
- Description of the Design achievements you attempted with this visualization.
  - Some ideas include consistent color choice, font choice, element size (e.g. the size of the circles).

GitHub Details
---

- Fork the GitHub Repository. You now have a copy associated with your username.
- Make changes to fulfill the project requirements. 
- To submit, make a [Pull Request](https://help.github.com/articles/using-pull-requests/) on the original repository.

Grading
---

Grades on a 120 point scale. 
24 points will be based on your Technical and Design achievements, as explained in your readme. 

Make sure you include the files necessary to reproduce your plots.
You should structure these in folders if helpful.
We will choose some at random to run and test.

**NOTE: THE BELOW IS A SAMPLE ENTRY TO GET YOU STARTED ON YOUR README. YOU MAY DELETE THE ABOVE.**

# R + ggplot2 + R Markdown

R is a language primarily focused on statistical computing.
ggplot2 is a popular library for charting in R.
R Markdown is a document format that compiles to HTML or PDF and allows you to include the output of R code directly in the document.

To visualized the cars dataset, I made use of ggplot2's `geom_point()` layer, with aesthetics functions for the color and size.

While it takes time to find the correct documentation, these functions made the effort creating this chart minimal.
# Tableau

Tableau is a visual analytics platform that makes the act of visualizing and interpreting data far easier for the general public, thereby giving people the ability to problem solve better. 

Tableau allows you to import data and it preprocesses it for you. All you need to do then is to select the kind of plot you wish to make, select which column of the data/variable you want as the x axis, and which you want represented on the y axis, and then add other columns as attributes. Then you hit the publish button and you will be taken to a separate webpage where the plot appears.

It took me about an hour to figure out how to use Tableau to get the desired results with the Penglings dataset, but the overall effort that went into making the visualization was minimal.

![Tableau Version](img/Tableau_Vis.png)

# Data Wrapper

Data Wrapper is a data compilation and visualization software that simplifies the process of representing large amounts of data. Data Wrapper is similar to Tableau in that the software allows you to import data, and it preprocesses it for you so that you can choose a type of chart and adjust the variables in the chart accordingly. I found that it was hard to show the differences in bill length in this particular software, even when I'd used it as a marker scaling factor. 

Unlike Tableau, I took about half an hour to figure out how to get the desired results with the Penglings dataset, so it took very little effort for me. 

![Data Wrapper Version](img/data-wrapper-visualization.png)

# Python + Matplotlib

In this method, I used the matplotlib package to create the desired visualization. It took me some time to figure out how to get the visualization to be close to what I wanted, but it was not impossible. Matplotlib allowed for me to have more free-range over what I could change about the plot, and therefore was more ideal in terms of accurately plotting the data. 

However, for whatever reason, I couldn't get the difference in Marker sizes show more obviously with this package. 

I used the following websites to help me:

- create a scatterplot
  https://www.geeksforgeeks.org/matplotlib-pyplot-scatter-in-python/
  https://stackoverflow.com/questions/55271471/plotting-some-third-variable-against-x-and-y-in-matplotlib-scatter
  
- determine marker color based on species
  https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html
  https://stackoverflow.com/questions/47684652/how-to-customize-marker-colors-and-shapes-in-scatter-plot

- determine marker size based on column data
  https://stackabuse.com/matplotlib-change-scatter-plot-marker-size/

![Python + Matplotlib Version](img/Matplotlib_Vis.png)

# Python + Altair

In this method, I used the Altair package with python to create the desired visualization. This one took about he same amount of time as Matplotlib did, however I got stuck because of a misalignment in package versions. I had installed the most recent version of Altair, not realizing that doing so would dissallow me from using Altair-Viewer. I did tons of research, trying to figure out why my Altair-Viewer package simply wouldn't update, and eventually came to the realization that I'd have to download a earlier version of Altair for the program to be able to use Altair-Viewer. 

Just like Matplotlib, Altair allowed for me to have more free-range over what I could change about the plot, however after having used Matplotlib, I found it challenging and almost counter-intuitive how I had to write things with Altair for the program to replicate what I'd been able to do with Matplotlib. 

I also had the same problem as with Matplotlib, where I couldn't get the difference in Marker sizes show more obviously. 

I used the following websites to help me:

- create a scatterplot
  https://www.geeksforgeeks.org/python-altair-scatter-plot/
  https://towardsdatascience.com/creating-interactive-scatter-plots-with-python-altair-e4b47e0aa8eb
    
- determine marker color based on species
  https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html
  https://stackoverflow.com/questions/47684652/how-to-customize-marker-colors-and-shapes-in-scatter-plot

- determine marker size based on column data
  https://stackoverflow.com/questions/67692708/set-size-of-individual-point-markers-in-altair
  
![Python + Altair Version](img/Altair_Vis.png)

# D3
I used the D3.csv function to read in the data and I used a variety of different websites to figure out how to create this same visualization in D3:

- color mapping:
  https://matplotlib.org/stable/users/explain/colors/colormaps.html

- scatter plot:
  https://d3-graph-gallery.com/graph/scatter_basic.html

  https://d3-graph-gallery.com/scatter

- marker size:
  https://stackoverflow.com/questions/18768236/marker-size-uniform-in-d3
  
  note: I really had to figure out based on how I set up the scatterplot itself how to make an attribute dependent on data.
  
  - legends:
  https://stackoverflow.com/questions/64914477/group-d3-legend-items

  https://stackoverflow.com/questions/13573771/adding-a-chart-legend-in-d3

- axes: 
  https://www.d3indepth.com/axes/#:~:text=To%20create%20an%20axis%3A%201%20make%20an%20axis,element%20and%20pass%20the%20axis%20generator%20into%20.call

  https://stackoverflow.com/questions/11189284/d3-axis-labeling

This particular one took me a very long time to get right. there were lots of little tweaks that had to be made, and in the beginning, I hadn't even set up an http server for the visualization so I was flying blind.

![D3 Version](img/D3_Vis.png)


## Technical Achievements
- **Plotted Data Accurately in all Chosen Formats**: Using a multitude of websites to help me along, I successfully created all of the required visualizations.

### Design Achievements
- **Fairly Accurate Replication**: Managed to display the graph in a way such that the markers weren't overlapping one another and hiding data. 

- **Made All Visualizations Presentable**: Managed to make the visualizations decent to look at.
