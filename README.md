# Google Sheets

  I started off with Sheets just to get it out of the way. This is the pretty much the only way I've ever graphed anything, with the exception of some Python and Matlab over the past couple years. It's been my go-to tool since I was in middle school. I wanted to start off with a baseline, something I knew I was comfortable with and wouldn't have to teach myself. Creating this visualization in Sheets was a very simple process.
  I'm not sure if I can call any part of the process difficult, maybe more like frustrating. The limited features and the whole spreadsheet aspect of Sheets made it a pain to get some details right. The bubble size in particular was a bit of a pain, and with the lack of customization I was left with something I knew I could improve on.
  I think there's always going to be a place for Sheets for making quick and easy graphs. It got me through my IQP. I think it's a very efficient way to whip up a bunch of figures based off a spreadsheet. I'd say it's probably better suited for more casual applications or for the user to boost their own understanding of the data they're working with. But for making something perfect, with specific requirements, it's definitely not ideal.
  Fortunately, as part of this I was able to get the data set all nice and clean by removing the rows that had NA's for all the relevant fields. I used the same cleaned csv for all my other visualizations.

![sheets](img/sheets.png)

# d3

What was easy?

This one wasn't what I would call easy. d3 is very, very new to me, as is the whole process of working in that language and dealing with async functions and webservers and such. I was glad to have a starting point from a1, but this task was obviously much more substantial. I spent a lot of time going back and forth between learning and working, but I will say I got into a rhythm towards the end. 
 
Difficult? 
 
Where could you see the tool being useful in the future? 

Did you have to use any hacks or data manipulation to get the right chart?

![d3](img/d3.png)

# altair

~

![altair](img/altair.png)

# tableau

~

![tableau](img/tableau.png)

# matlab

~

![matlab](img/matlab.png)

## Technical Achievements
- added mouse hover functionality for individual datapoints (altair, tableau)
- added interactive zoom in/out (altair)

### Design Achievements
- I decided to do some research into the 3 species of penguins included in this dataset. I found out that Jules Dumont d'Urville discovered the Adélie penguin. Also, both the Gentoo and the Chinstrap penguin were discovered by Johann Reinhold Forster. I decided to incorporate this information into my color scheme. Jules was French and Johann was German, but since Johann discovered two of these species, I gave the Chinstraps to Graham Turbott of New Zealand (who transferred the species to a different genus) and left the Gentoos to Johann. When considering the flags of each of these countries, only one viable color scheme emerged: blue for Chinstrap, red for Adélie, and yellow for Gentoo. I considered using the exact color values of the official flags, but that would have looked AWFUL. So I mellowed it out a bit. This process not only left me with a consistent color scheme for this dataset, it also left me with more knowledge about penguins and taxonomy than I ever knew I needed. I feel more connected to this dataset.
