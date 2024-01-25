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

## Technical Achievements
- **Proved P=NP**: Using a combination of...
- **Solved AI Forever**: ...

### Design Achievements
- **Re-vamped Apple's Design Philosophy**: As demonstrated in my colorscheme...
