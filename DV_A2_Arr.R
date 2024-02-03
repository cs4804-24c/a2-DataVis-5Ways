# define 2 vectors
penguins=read.csv('/Users/Ned/Documents/CS Dava Vis. A2/penglings.csv') # change path if you run it yourself

# create a vector of colours based on species
species_colours <- c("Adelie" = "red", "Chinstrap" = "green", "Gentoo" = "blue")
colours <- species_colours[penguins$species]

# calculate size of plots based on bill length
size <- penguins$bill_length_mm * 0.1 - 2

# plot the two axis
plot(penguins$flipper_length_mm, penguins$body_mass_g, 
     xlab = "Flipper Length (mm)", ylab = "Body Mass (g)",
     main = "Body Mass vs Flipper Length",
     cex = size, col = colours, pch = 16)

# the myth
# for species colours
legend("topleft", legend = names(species_colours), fill = species_colours, title = "Species",
       pch = 16, pt.cex = 1.5)


# the legend
# for size of plots
legend("bottomright", legend = c("40", "34"), title = "Size",
       col = "black", cex = 1.8, pch = c(19, 20))


