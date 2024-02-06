#starter code http://www.sthda.com/english/wiki/ggplot2-scatter-plots-quick-start-guide-r-software-and-data-visualization
#helper code/resource http://monashbioinformaticsplatform.github.io/2015-11-30-intro-r/ggplot.html
#https://www.yan-holtz.com/PDF/Ggplot2_advancedTP_correction.html

library(ggplot2)

pengs <- read.csv("/home/taya/a2-DataVis-5Ways-yakovenko/penglings.csv") #maybe add filtering (?)
pengs <- na.omit(pengs) #ommit NA values in any of the fields because they are used for viz
#print(pengs)
ggplot(pengs, aes(y=body_mass_g, x=flipper_length_mm, size=bill_length_mm, color=species, shape=island)) + #change the shape of points based on each island
  geom_point(alpha = 0.5) + #change oppacity of points to see the lines better
  stat_smooth(method="lm") + #regression lines for each species
  xlab("Flipper Length (mm)") +  # Changing the labels for x and y axis
  ylab("Body Mass (g)")  + 
  facet_grid(year ~ sex) + #separate based on sex of penguins and year of the data
  scale_shape_manual(values = c(1, 2, 3)) +  # Define shapes for each island
  labs(shape = "Island")  # Change the legend title to 'Island'
