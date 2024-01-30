#starter code http://www.sthda.com/english/wiki/ggplot2-scatter-plots-quick-start-guide-r-software-and-data-visualization
#helper code/resource http://monashbioinformaticsplatform.github.io/2015-11-30-intro-r/ggplot.html

library(ggplot2)

pengs <- read.csv("/home/taya/a2-DataVis-5Ways-yakovenko/penglings.csv")
#print(pengs)
ggplot(pengs, aes(y=body_mass_g, x=flipper_length_mm, size=bill_length_mm, color=species)) +
  geom_point()
