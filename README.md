
![penguins](https://github.com/cs4804-24c/a2-DataVis-5Ways/assets/412089/accc5680-3c77-4d29-9502-d3ff8cd922af)

# 02-DataVis-5ways

Assignment 2 - Data Visualization, 5 Ways  
===
Python

Pandas + Matplotlib + Seaborn

Python is considered as a popular programming language that has strong visualization capabilities. Matplotlib is the most widely used and the first library for plotting in Python. Seaborn is another Python visualization library based on the Matplotlib library.

Technical achievements 

One of the technical achievements was filtering the species we wanted and making a subset. At first, the legend was not shown in the correct part and was on the points of the scatterplot. I tried to solve this by using the ‘plt.legend’ function and  by specifying its location (‘loc’ command) to be upper right.


Design achievements 

Assigning colors to the species used in the graph. Styling with Seaborn to show a grid. Adding axes labels for increasing the plot interpretability.
--------------------------------------------------------------------------------------------
R

R + ggplot2 + R Markdown + RStudio

R is considered as a programming language for statistical computing and the visualization of data. R Markdown is a format of document that compiles to html or PDF and lets us include the output of R code in the document. ggplot 2 package is an open-source popular visualization package used in R. RStudio is another tool I used for working with the R programming language. I used ggplot2 in R to represent values for two different numeric variables and observe their relationship. ‘geom_point()’ function was also used for the functions for color and size.


Technical achievements 

One of the technical achievements was to filter the specific columns we wanted for the visualization. Doing the color-coding based on the penguin species and encoding the size of points with the ‘bill length’ variable were other technical achievements. 

Design achievements 

Providing x and y axis labels for a more informative visualization. Differentiating different colors for the different species we had. Adding the alpha for transparency to the points while maintaining their color.

--------------------------------------------------------------------------------------------
Matlab

Matlab is a programming language for analyzing and designing systems. Also, Matlab enables us to create custom charts and can be considered as a biovisualization tool for biomedical engineering fields. By the use of the ‘gscatter(x,y,g)’ command, I could plot a scatter plot of x and y grouped by g.
For visualizing this plot in Matlab, I used the ‘figure()’ command and specified the plot shape and size. Then, for creating the scatter plot, the gscatter() command was used and I specified the x (flipper length) and y (body mass) axis and differentiate the dots by different species. I tried to make the colors similar to the template we had by the use of RGB values for 'Adelie', 'Gentoo', and 'Chinstrap' species. Then it created the plot for me, but I had to add x and y labels. I also added the grid to be on and added a legend at the end. I found the process of visualizing this plot by Matlab not the easiest way, but a doable one by considering specifications and knowing the required commands.


Technical achievements

Creating a scatter plot using ‘gscatter’ function for seeing the relationship between flipper length and body mass of the penguins. Enabling a grid for this scatter plot for helping in a more precise analysis. Configuring Matlab plot with different dimensions to find the best choice.


Design achievements 

Differentiating the penguins by their species with the specific colors was a little challenging. Adding axis labels and title for a more informative plot for presenting. Adding legends for the interpretability of the plot. Adding a grid for a better layout.

--------------------------------------------------------------------------------------------
Tableau

Tableau is a data visualization tool that is used for data analysis and business intelligence. Tableau can be used when we are working with larger datasets. It has advanced visualization capabilities and I found it easy to understand, implement, and work with as a powerful visualization tool. It also takes much less time to create graphs with Tableau. 


Technical achievements 

I load the ‘penguin.csv’ file to Tableau, select the scatter plot, drag ‘Flipper Length’ to the columns and ‘Body Mass’ to the rows section. A challenge that I faced while plotting this graph was that after placing a measure in columns and rows shelf, I saw 3 single points (representing 3 species). Although I wanted all the values to show on the graph. I recognized the points as showing the sum of all values for both measures. So, I used the Analysis part of Tableau at the top of it and clicked on Aggregate measures.

Design achievements 

Trying to assign colors similar to the colors used in the template. I also specified the shape to be a circle. I also didn't know how to imply ‘bill length’ to the graph. I figured out that I can drag ‘bill length’ to the size shelf in the Marks section. My challenge was how we could color-code the species in the plot. I identified that I have to drag ‘Species’ columns to the color section. I also did not know how to change the ranges of the x and y axes. So I tried double-clicking an axis to open the edit axis and selected a custom option and added the ranges manually.

--------------------------------------------------------------------------------------------

D3

JavaScript + D3

Javascript is a widely used programming language that is mostly used in web development and works with html files. D3.js is an open source JavaScript library for visualizing data.
I think plotting this graph with D3 was the most challenging and time-consuming one. I used the template of plotting a scatter plot from the D3 website as my reference. 

Technical achievements 

The technical achievement I had was to be able to first give the input and load the penguin.csv data in JavaScript. I used several ways and with the use of d3.csv function, I was able to read the dataset. After loading the dataset, I only tried to modify the code I had to make the graph as similar to the reference image I had. Alao, I learned another way to open a new terminal in the visual code studio by writing ‘python3 -m http.server’. With this method, I was able to run my local web server and the output of my code.

Design achievements 

I tried to modify the x and y axes data ranges to be consistent with the reference image I had. I learned to use the ‘ticks()’ command to specify the ranges on the x and y axis. I added x and y labels for a better understanding of the plotted graph. Using ‘bill length’ for circle sizes was another implemented design. Also, plotting different species with a specified color was another design achievement I had regarding this plot.

--------------------------------------------------------------------------------------------
Flourish
Flourish can be used for creating interactive content and visualizations. Flourish visualizations are useful for web articles and when we want to have a creative data visualization. I found this software very helpful, easy to use, and understand. Flourish also has a high potential to form different creative visualizations in much less time.


Technical achievements 

I load the ‘penguin.csv’ file to Flourish, select the scatter plot, and assign the columns to the x and y axis. I assigned the x and y values by selecting the corresponding columns. My challenge was how to plot the species in the graph. So, I figured out I have to use the part named ‘color’ and specify the species column. Actually this was my achievement to utilize the ‘species’ column to color-code the points based on different species in a way that each species will be represented by a distinct color.

Design achievements 

Adjusting the dot colors to the colors to the template on the Dot styles section.e we had. Setting the scatter plot to show data points as dots (circles). Setting the opacity of dots to be 0.8 in the Dot styles section. Adding a legend to the graph. Adding the x and y labels in a way that x-label is at the bottom of the graph and y-label be vertical at the left side of the graph. 
















===============================================================================
===============================================================================
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

![ggplot2](img/ggplot2.png)

# d3...

(And so on...)


## Technical Achievements
- **Proved P=NP**: Using a combination of...
- **Solved AI Forever**: ...

### Design Achievements
- **Re-vamped Apple's Design Philosophy**: As demonstrated in my colorscheme...
