# Altair + Python (PyCharm)

![Altair Visualization](img/<Altair.png>)

For this visualization, we utilized Altair, a declarative statistical visualization library in Python. Altair's concise and expressive syntax allowed us to create insightful visualizations with minimal code. Its seamless integration with Pandas made data manipulation and plotting straightforward. Altair is particularly beneficial for projects requiring quick and effective exploration of data through visualizations. No major challenges were faced during implementation, and Altair's simplicity positions it as a valuable tool for data visualization in Python.

# Technical Achievements
Successfully loaded the penglings dataset from a remote URL
Information about the species, flipper length, body mass, and bill length are displayed on hover

# Design Achievements
Customized the axes with titles with adjusted font sizes for clearer understanding of data
Customized the size of circles to scale to size of scatter plot too make the visual seem
consistent in scale

# HTML + d3.js

![D3.js Visualization](img/<d3.png>)

The D3.js scatter plot involved using D3.js version 5. The dataset was loaded asynchronously using `d3.csv`. Data cleaning included converting string values to numeric. Scales for x, y, color, and size were set up to map data to visual elements. Circles were created for each data point, and axes were added for context. A legend was included for species identification. Creating the scatter plot in D3.js provided flexibility but also posed challenges, particularly with the scales and positioning of elements. The legend and axes required careful adjustments. The dynamic nature of D3.js made it challenging but rewarding. While it has a steeper learning curve, the control it offers makes it worth it. In the future, it could be used for a wide range of applications since once you master it, you then have so much control over the visuals.

# Technical Achievements

Able to parse the CSV data, converting string values into numeric form in order to have appropriate scaling
# Design Achievements

Added legend with species and their color association
The SVG container adjusts its size based on the specified margins and dimensions

# Datawrapper

![Datawrapper Visualization](img/<Datawrapper.png>)
Datawrapper offered a user-friendly experience for creating a scatter plot with minimal effort. The websites intuitive interface allowed for easy uploading and visualization of the dataset. While customization options were somewhat limited compared to coding-based solutions, the available settings provided sufficient control over essential chart elements. Datawrapper excelled in automating the process, including axis scaling and labeling. Datawrapper prioritizes ease of use over having extensive control.

# Technical Achievements

# Design Achievements
Included a trend line, grid, and title
Overall easy to understand and the data is well positioned so that nothing seems
overcrowded

# Flourish

![Flourish Visualization](img/<Flourish.png>)


Flourish provided a visually intuitive platform for creating a scatter plot, making the process easy and accessible for users with varying levels of expertise. The tool's drag-and-drop interface simplified the selection of data attributes and made the process of creating a scatterplot more appealing. However, Flourish offered less control when compared to D3.js or Altair. Flourish's collaborative features make it well-suited for teams working on data-driven storytelling or reporting. Flourish could be used in the future by the media or people who are trying to create engaging visuals.

# Technical Achievements

# Design Achievements
Added a trend line for each species of penguin with its associative color
Added a title and subtitle too give the viewer a better understanding of the graph

# Matlab

![Matlab Visualization](img/<MatLab.png>)

Creating a scatter plot in MATLAB was relatively straightforward. MATLAB's built-in functions for handling categorical data and color assignments helped to simplify the process. The resulting static plot is suitable for inclusion in reports or presentations. The RGB color specification used for custom colors allowed precise control over the aesthetic aspects of the scatter plot. Overall, MATLAB is well-suited for users familiar with the platform and looking for a balance between simplicity and customization, making it seem useful for the academic field in the future.

# Technical Achievements
Able to load the pengling dataset from an external URL using readtable
Use of RGB value to associate penguin species
Use a loop that iterates through the dataset then creates individual scatter plot points

# Design Achievements
Include grid lines to help provide visual reference for the viewer
Created a colorbar using bill_length_mm which makes it easier to interpret the color representation with the bill length values
