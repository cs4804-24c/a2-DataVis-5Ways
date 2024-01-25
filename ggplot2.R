# library (ggplot2)
# print(bills)
# #Creating basic plot
# ggplot2(bills, aes = (x = flipper_legnth_mm, y = body_mass_g)) + 
# geom_point()

library(ggplot2)

bills <- read.csv("penglings.csv")
#Basic Graph Additions (Minimum Requirements)
ggplot(bills, aes(x = flipper_length_mm, y = body_mass_g)) +
    geom_point(aes(color = species, size = bill_length_mm, alpha = 0.2, shape = island)) +
    xlab('Flipper Length (mm)') +
    ylab('Body Mass (g)') +
    ggtitle('Penguin Flipper Length vs Body Mass')

ggsave('ggplot2Graph.png',width=20,height=10)