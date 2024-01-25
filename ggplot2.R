# library (ggplot2)
# print(bills)
# #Creating basic plot
# ggplot2(bills, aes = (x = flipper_legnth_mm, y = body_mass_g)) + 
# geom_point()

library(ggplot2)

bills <- read.csv("penglings.csv")
ggplot(bills, aes(x = flipper_length_mm, y = body_mass_g)) +
    geom_point(aes(color = species, size = bill_length_mm, shape = island)) +
    xlab('Flipper Length (mm)') +
    ylab('Body Mass (g)') +
    ggtitle('Penguin Flipper Length vs Body Mass') + 
    theme(panel.background = element_rect(fill='darkblue',color='darkblue'))

ggsave('ggplot2Graph.png',width=20,height=10)