# Matplotlib
Matplotlib is the library that, as of beginning this assignment, I have the most experience with through my machine learning / AI classes.

I was able to create one legend that maps species to colors, but I was unable to get the size legend to be consistent with the dots.

I did my best to match the given scatterplot's colors by augmenting the axis labels, ticks, and title:
```python
plt.xlabel("Flipper Length (mm)", color="#5B5B5B")
plt.ylabel("Body Mass (g)", color="#5B5B5B")
plt.tick_params(axis='x', colors="#5B5B5B")
plt.tick_params(axis='y', colors="#5B5B5B")
```

I also added background grid:
```python
plt.grid(True, linestyle='--', linewidth=0.5, color='#DEDEDE')
```

And I scaled up the entire figure:
```python
plt.figure(figsize=(12, 8))
```

[!Matplotlib](./img/matplotlib.png)

# d3
I actually had a lot of trouble with d3. I'm sure I'll figure it out soon enough, but I felt like I had too many options. The first thing I tried to do was plot the points, but I ended up not framing my scatterplot well and then everything else just feels like an overlay.

Everything got so busy, so I abstracted all of my drawing to functions and passed in the svg.

```javascript
appendLabels(svg)
appendGrid(svg)
appendTicks(svg)
mapDots(svg, data)
appendLegend(svg)
```

If I were to make this in d3 again, I would start by creating the grid, labels, and legend. That way I can frame my data and then, hopefully, create an SVG inside the frame where I place my points according to a slightly smaller scale.

Hypothetically, I could make a wrapper around this plot and move the labels, but I'd like to move on to another library.

![d3](./img/d3.png)

## Technical Achievements
- **Proved P=NP**: Using a combination of...
- **Solved AI Forever**: ...

### Design Achievements
- **Re-vamped Apple's Design Philosophy**: As demonstrated in my colorscheme...
