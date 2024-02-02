library(ggplot2)
library(crayon)
data <- read.csv("C:\\Users\\alysh\\OneDrive - Worcester Polytechnic Institute (wpi.edu)\\Documents\\Junior Year\\C Term\\Assignment 2\\a2-DataVis-5Ways\\penglings.csv")

colors <- c('Adelie' = '#FF8C00', 'Chinstrap' = '#9932CC', 'Gentoo' = '#008B8B')

data$flipper_length_mm[is.na(data$flipper_length_mm)]<-mean(data$flipper_length_mm,na.rm=TRUE)
data$body_mass_g[is.na(data$body_mass_g)]<-mean(data$body_mass_g,na.rm=TRUE)
data$bill_length_mm[is.na(data$bill_length_mm)]<-mean(data$bill_length_mm,na.rm=TRUE)

ggplot(data, aes(x=flipper_length_mm, y=body_mass_g)) + 
  geom_point(aes(color = species, size = bill_length_mm), alpha=0.8) + 
  scale_color_manual(values = colors) +
  labs(
    title = 'Penguin Flipper Length vs Body Mass',
    x = 'Flipper Length (mm)',
    y = 'Body Mass (g)'
  ) +
  theme(plot.title = element_text(hjust = 0.5))
