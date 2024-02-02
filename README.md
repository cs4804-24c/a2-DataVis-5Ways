
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

# Data Pre-Processing / Technical Achievment

Some of the records in the penguins data set contained missing values. There are many different ways one can handle missing values, some just as simple as disregarding these rows. I decided to research different imputation techniques and decided to implement KNN imputer with k = 3. This code can be found in the .ipynb file. KNN imputer calculates the distance between the points in a high dimensional space (as many dimensions as columns used), and assigns the average of the k closest points to the missing value. I standarized the data to ensure that one of the columns did not get overweighed. Once the imputator finished, I un-normalized the data to get back to the original scales. I then wrote to a new csv and used this as my data source for my visuals.

I also believe I achieved the technical achievements for the small aspects I added to the graphs. For d3 I went further astetaclly and added a key. Also for the graphs I went further with the shape to make the size of the dots to stand out more. A very small but important detail I did with all my graphs was changing the axis names to make them appear how humans read, as opposed to the string with the underscores in them. 

# Tableau

Tableau is a data visualiztion software that is often used in businesses. From my knowledge, powerBI and tableau are very similar and are some of the most popular business intelligence tools used in industry. It is no code so it is very easy for existing employees of companies to pick up.

I had past experience in this platform which made this visual straight forward to create. I connected to the csv, and then just dragged and dropped the columns onto the axes and features for color and size. For aspects I wished to change, for the most part it was just right click and edit.

Overall, I think Tableau is a good platform to create a viarety of visuals and combine them onto a dashboard with interactive filters. I think it lacks the capabilities of animation and complex visuals.

![TableauVis](img/TableauVis.png)

# Altair

Altair is a python library. I had not used or heard of altair before this assignment. The website has a lot of good resources to easily learn different aspects of the library. Definetley more technical than platforms like Tableau; however, more freedom and customization of the visual.

I created the visual in the python notebook in the cell after teh altair visual markdown. To create the visual I created an alt.chart using my data and filled the points with an opacity of .8. From there I customized the x, y, color, and size. For x and y I inputed the desired columns then set a custom scale and title. For color I had to create two lists that contained the different species and a list containing the corresponding color, then in the alt.color I inputted the column and custom scale for the colors. This library I had the easiest time setting the size scale to make the lower values small and larger values big. I inputted the colum and set the scale and min and max size. An aspect I liked was the legend automatically showing.

Overall, I think this library is very straight forwards and easy learn. It has more customization than tableau.

![AltairVis](img/AltairVis.png)

# Matplotlib

Matplotlib is another python library. I have had past expeirence with this library to create simple visualizations. It is simalar to Altair, but I think Altair is easier to use after learning a little about it.

I created the visual in the python notebook in the cell after the Matplotlib markdown. Customizing the color and size were more complicated in this library than Altair. I had to make a dictionary with the colors and then loop through my data to asign the colors. For sizing I normalized the data to try to emphasize the difference in size but could not do so as successfully or easily as in Altair. Other than this it was similar to altair where I create a plt.scatter and inputted my data. The legend for color is much more complicated to create than the auto generated one in Altair.

Overall, I would prefer to use Altair over Matplotlib as the Altair visual looks better with less customization by the user.

![MatplotlibVis](img/MatplotlibVis.png)



# D3

Link to my gh-pages site "http://BradyA25.github.io/a2-DataVis-5Ways/index.html".

D3 is a javascript library. This visual took me the longest to make as my only experience with javascript was from assignment 1. This method was the most technical out of all of the ways; however, this could mean that it is the most customizable. From the examples I have seen I think the capabilities of d3 with interactabliity and animations are top of the industry.

I created this visual in the index.html file. I first created a svg, then a background and filled it with a light grey to mimic the example. From here I used d3.csv to read in my data. I used this website for refence of my code: https://d3-graph-gallery.com/scatter.html. This helped me learn and took me step by step of what each line does to the visual. As mentioned this was the most technical visual I made. I had to explicitly declare the length and locations of everything. Adding the color to the visual was similar to python where I assigned the species to a color in a variable. After the graph aspects were all set i appended the points. It appends a lot of circles with the attributes derived from teh data and other declarations I made, such as the opacity. The legend was complicated to make compared to Altair, but I was able to create one and put it where ever I wanted.

Overall, this was the most technical visual; however, this usually means that it gives a lot of freedom to the user.

![D3Vis](img/D3Vis.png)

# Flourish

For my final method I created the visual using Flourish. I had never used this before. After using it I have learned that it is similar to use with tableau, but has more features in regards to animation. In the time playing with the platform I was able to create a simple visualization of the data over time.

This visual was created online so I included a screenshot of the visual, and the data inputs. Creating the visual was very simple. I hit create new visualization, selected scatter plot and then entered the columns in the side bar for visualization. I was surprised by how easy it was to create. I also like how you can import the visual to canva to allow for easy integration into presentations. There is also create a story option, so I think this platform would be very easy to use to combine visuals into a story telling. The most complicated aspect of this visual was to change the color pallete (all I had to do was explicity declare the colors). I did struggle with changing the size of teh dots to be exagerated. I think if I wanted to accomplish this I would have to normalize the column and enter that into size.

Overall, I was surprised by how easy this platform was to use, and think it has a lot of potential on the animation side of visuals.



![FlourishVis](img/FlourishVis.png)

![FlourishData](img/FlourishData.png)

# R + ggplot2 + R Markdown

R is a language primarily focused on statistical computing.
ggplot2 is a popular library for charting in R.
R Markdown is a document format that compiles to HTML or PDF and allows you to include the output of R code directly in the document.

To visualized the penguins dataset, I made use of ggplot2's `geom_point()` layer, with aesthetics functions for the color and size.

While it takes time to find the correct documentation, these functions made the effort creating this chart minimal.

![ggplot2](img/ggplot2.png)

## My Additions

To add to this visual I added the island to the shape of the points. I also used my imputed data. Adding shape was straight forward.

![ggplot2Shape](img/RVisWithShape.png)