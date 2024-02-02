# Google Sheets

  I started off with Sheets just to get it out of the way. This is pretty much the only way I've ever graphed anything, with the exception of some Python and Matlab over the past couple years. It's been my go-to tool since I was in middle school. I wanted to start off with a baseline, something I knew I was comfortable with and wouldn't have to teach myself. Creating this visualization in Sheets was a very simple process.
  I'm not sure if I can call any part of the process difficult, maybe more like frustrating. The limited features and the whole spreadsheet aspect of Sheets made it a pain to get some details right. The bubble size in particular was a bit of a pain, and with the lack of customization I was left with something I knew I could improve on.
  I think there's always going to be a place for Sheets for making quick and easy graphs. It got me through my IQP. I think it's a very efficient way to whip up a bunch of figures based off a spreadsheet. I'd say it's probably better suited for more casual applications or for the user to boost their own understanding of the data they're working with. But for making something perfect, with specific requirements, it's definitely not ideal.
  Fortunately, as part of this I was able to get the data set all nice and clean by removing the rows that had NA's for all the relevant fields. I used the same cleaned csv for all my other visualizations.

![sheets](img/sheets.png)

# d3

What was easy?

  This one wasn't what I would call easy. d3 is very, very new to me, as is the whole process of working in that language and dealing with async functions and webservers and such. I was glad to have a starting point from a1, but this task was obviously much more substantial. I spent a lot of time going back and forth between learning and working, but I will say I got into a rhythm towards the end, since there was a lot of repetition between x and y and a lot of the final tweaks were about perfecting the positions of certain elements.
   What I found most difficult was the sheer number of steps involved in doing something so simple. I'm sure the more I do it the easier it'll get, but it took a while to build up the visualization from a collection of circles on the page. I would reach points where I thought I was finished, but there was another thing I forgot to add or tweak that normally I'd expect the tool to take care of for me. There's a lot of attention to detail required for this kind of stuff, and it definitely makes me appreciate the more complex things people are able to create using d3.
  I think this was a good one to do right after using Sheets. The two are so incredibly different, and both of them frustrated me in different ways, but they definitely both have their place. The level of control is both a blessing and a curse. I spent a while just tinkering around with where I thought the axis labels looked best, and little things like that, when in another tool I might not even think about the labels since they're done for me and they're "good enough". They definitely have it right on their site, this is perfect for bespoke data visualization.

![d3](img/d3.png)

# altair

  This one was definitely my favorite, because I still had to write code for it to work. I like Python. I'm not as used to it as other languages, but I enjoy its forgiving simplicity. Altair made it super straightforward to create what took hours longer in d3. After I completed the basic requirements, I felt compelled to explore a bit more before moving on, knowing that I'll definitely come back to this library at some point. I poked around some more tutorials and found the tooltip thing, which was neat, as well as the interactive zoom in/out feature. I was surprised at how achievable these things were, and how much was built in to just a simple chart. It did a lot of the work for me, which I can always appreciate. 
  I'm not exactly sure why, but for me the hardest bit, or at least the part that took the most time was actually importing my data. I'm not a pro at Jupyter notebooks yet, but even past that I got stuck on trying to import my csv using only Altair. I ended up going with pandas to help me out there, since that's what I remember from my previous experiences, and the rest of the Altair stuff went smoothly. 
  I think this would be incredibly useful for a whole lot of different visualization applications. And there's still so much more for me to learn about it. It was as simple and fast as I needed it to be, and it also left room for me to customize things and play around with different aspects without too much headache. I can see why it's so popular.

![altair](img/altair.png)

# tableau

  Once I figured out how to get set up with Tableau and import the data, this was incredibly simple to use. It basically did everything for me once I chose rows and columns. It was almost like it knew what I wanted to make. I did have to fiddle around with the scales and change the data types to dimensions, but that was pretty much it. Having a dedicated tool with sliders and tabs and explanations all organized in one place made it a very different experience from writing code. With other solutions, I had to spend a ton of time searching for examples or tutorials to try and get my bearings and understand the options at my disposal. With Tableau, I didn't leave the site once. I was able to figure out everything I wanted to do, either through trial and error or just plain intuition. It's a very pleasant tool to engage with and I'd love to use it again.
  The only things I can think of that presented any significant difficulty were the setup process, as I mentioned, as well as just the quantity of information on my screen at any given time. This layout definitely improves productivity and contributes to the power of the tool, but as a first-time user I was definitely a little lost at first. It was easy to wrap my head around it after spending some time, but I suppose this might just be a disadvantage of this type of tool. Everything is there on display to tinker with, it's not limited by what you need for your specific case. I think the differences between this and a code-based solution would become much less significant with time and experience.
  I think Tableau is especially nice for people who want to create clean, informative visualizations, who might not know how to code or are at least less comfortable with it. I'm pretty sure most people who can use a computer for typical productivity purposes could get started with Tableau without much hassle. Compared with something like Google Sheets, this brings similar simplicity and ease of use, but makes the power to change and improve the visualization much more accessible to the user. It kept up with everything else I used, and required much less investment.

![tableau](img/tableau.png)

# matlab

  Matlab was another pretty challenging one for me in this assignment. I will give it credit for being extremely powerful and requiring very few lines of code to accomplish this task. I also find the tutorials and examples from MathWorks to be some of the most helpful of any tool I've used. I had to go back and forth a lot, but reading those help pages saved me a lot of time and stress.
  Not all though, since Matlab is still a pain for me to work with. The interface is not something I'm eager to engage with again. Too much info, in strange and sometimes hidden spots, made the experience much less smooth than some of the other tools and libraries I used. For the most part, I tried to stick to the code editor tab once I had my data imported, since that's what made the most sense to me. I actually went through two versions of this visualization. The first, failed attempt was when I tried to use Matlab's bubblechart instead of a scatterplot. I was unable to properly map the colors I wanted to the species. I considered leaving it as it was and writing about the difficulty here, but through some additional investigation I found I could use a scatterplot and achieve a similar effect. This was a much easier solution and allowed me to move on to adding important details like labels, gridlines, and a colorbar. The finishing touch stage was actually smoother than d3, thanks to only needing one line of code per addition. It came together nicely and actually left me with a slightly more positive opinion of Matlab. 
  I know Matlab can be used for a ton of things, much more than creating the visualization for this assignment. So I think it might be better to let Matlab do its thing and use other tools and libraries to visualize data. I don't really see any advantages it has compared to anything else I used. But it's getting easier to use it the more I try, so maybe I can do other things with it in the future.

![matlab](img/matlab.png)

## Technical Achievements
- added mouse hover functionality for individual datapoints (altair)
- added interactive zoom in/out (altair)
- challenged myself to learn as many new tools/libraries as I could within the scope of this assignment
  - like avoiding ggplot2 (for now) to not get too close to the example
  - and not doubling up on languages
 
### Design Achievements
- I decided to do some research into the 3 species of penguins included in this dataset. I found out that Jules Dumont d'Urville discovered the Adélie penguin. Also, both the Gentoo and the Chinstrap penguin were discovered by Johann Reinhold Forster. I decided to incorporate this information into my color scheme. Jules was French and Johann was German, but since Johann discovered two of these species, I gave the Chinstraps to Graham Turbott of New Zealand (who transferred the species to a different genus) and left the Gentoos to Johann. When considering the flags of each of these countries, only one viable color scheme emerged: blue for Chinstrap, red for Adélie, and yellow for Gentoo. I considered using the exact color values of the official flags, but that would have looked AWFUL. So I mellowed it out a bit. This process not only left me with a consistent color scheme for this dataset, it also left me with more knowledge about penguins and taxonomy than I ever knew I needed. I feel more connected to this dataset.
