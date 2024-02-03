library(ggplot2)
penguins = read.csv("C:/Users/vince/Documents/College/23-24/Data Vis/a2-DataVis-5Ways/penglings.csv")
p<-ggplot(penguins, aes(x=flipper_length_mm, y=body_mass_g, col=species))
jGraph<-geom_jitter(aes(size = bill_length_mm, alpha = 0.8))
color<-scale_color_manual(values = c('Adelie' = 'orange', 'Gentoo' = 'cyan', 'Chinstrap' = 'purple'))
colorTitle<-labs(color = "species")
guide<-guides(alpha = FALSE)
label<-labs(x = "Flipper Length (mm)", y = "Body Mass (g)")
p+jGraph+color+colorTitle+guide+label