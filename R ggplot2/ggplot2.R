library(ggplot2)
library(plotly)
library(extrafont)

# loaded the data into Rstudio first
data <- penglings

# importing the font to change the titles
font_import(pattern = "times new roman")

# defining which colors I would like to use
colors <- c('Adelie' = '#FF8C00', 'Chinstrap' = '#9932CC', 'Gentoo' = '#008B8B')

# filling in each of the blank values with the average from that row
data$flipper_length_mm[is.na(data$flipper_length_mm)]<-mean(data$flipper_length_mm,na.rm=TRUE)
data$body_mass_g[is.na(data$body_mass_g)]<-mean(data$body_mass_g,na.rm=TRUE)
data$bill_length_mm[is.na(data$bill_length_mm)]<-mean(data$bill_length_mm,na.rm=TRUE)

# using ggplot to create the scatterplot, text contains the contents of the tooltip
p <- ggplot(data, aes(x=flipper_length_mm, y=body_mass_g, text = paste("Flipper Length: ", flipper_length_mm, "mm<br>Body Mass: ", body_mass_g, "g<br>Species: ", species, "<br>Bill Length: ", bill_length_mm, "mm<br>Island: ", island, "<br>Sex: ", sex, "<br>Year: ", year))) + 
  geom_point(aes(color = species, size = bill_length_mm), alpha=0.8) + 
  scale_color_manual(values = colors) +
  labs(title = 'Penguin Flipper Length vs Body Mass', x = 'Flipper Length (mm)', y = 'Body Mass (g)') + 
  theme(plot.title = element_text(hjust = 0.5), text = element_text(family = "Times New Roman"))

# using plotly to classify the tooltip and make the background white (default was orange)
p <- ggplotly(p, tooltip = "text")
p <- style(p, hoverlabel = list(bgcolor = "white"))

# fixing the title of the legend (which was effected by converting to plotly)
p <- layout(p, legend = list(title = list(text = "Species")))

print(p)


