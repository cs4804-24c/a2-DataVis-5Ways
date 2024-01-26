Note:
I used RStudio to code and create this graph and then attached the file here.


menu<-read.csv("https://raw.githubusercontent.com/cs4804-24c/a2-DataVis-5Ways/main/penglings.csv")
head(menu)

library(tidyverse)
library(ggplot2)
library(ggside)
library(ggiraph)
library(shiny)
library(plotly)

ui <- fluidPage(
  plotlyOutput("distPlot")
)

server <- function(input, output) {
  output$distPlot <- renderPlotly({
    ggplot(menu, aes(x = flipper_length_mm, y = body_mass_g)) +
      geom_point(aes(color = species, size=bill_length_mm), alpha=0.8) +
      scale_color_manual(values = c("darkorange","darkorchid","cyan4")) +
      labs(x="Flipper Length (mm)", y="Body Mass (g)")
  })
}

shinyApp(ui = ui, server = server)
