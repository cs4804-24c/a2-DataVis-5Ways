//used chat gpt for some and the following links
//https://d3-graph-gallery.com/graph/custom_legend.html
//https://stackoverflow.com/questions/23703089/d3-js-change-color-and-size-on-line-graph-dot-on-mouseover

var margin = { top: 10, right: 30, bottom: 30, left: 60 },
    width = 700 - margin.left - margin.right,
    height = 650 - margin.top - margin.bottom;

var svg = d3.select("#graph")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// Read the data
d3.csv("penglings.csv", function(data) { //if running the python server.py we are also able to get access to the data at localhost:8000/penglings.csv

    // Convert string data to numeric
    data.forEach(function(d) {
        d.flipper_length_mm = +d.flipper_length_mm;
        d.body_mass_g = +d.body_mass_g;
    });

    // Add X axis
    var x = d3.scaleLinear()
        .domain([d3.min(data, function(d) { return d.flipper_length_mm; }), d3.max(data, function(d) { return d.flipper_length_mm; })])
        .range([0, width]);
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));


    // Handmade legend
    /*svg.append("circle").attr("cx",200).attr("cy",130).attr("r", 6).style("fill", "#69b3a2")
    svg.append("circle").attr("cx",200).attr("cy",160).attr("r", 6).style("fill", "#404080")
    svg.append("text").attr("x", 220).attr("y", 130).text("variable A").style("font-size", "15px").attr("alignment-baseline","middle")
    svg.append("text").attr("x", 220).attr("y", 160).text("variable B").style("font-size", "15px").attr("alignment-baseline","middle")*/

    // Add X axis label
    svg.append("text")
        .attr("transform", "translate(" + (width / 2) + " ," + (height + margin.top + 20) + ")")
        .style("text-anchor", "middle")
        .text("Flipper Length (mm)");

// Add Y axis label
    svg.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left)
        .attr("x", 0 - (height / 2))
        .attr("dy", "1em")
        .style("text-anchor", "middle")
        .text("Body Mass (g)");

    // Add Y axis
    var y = d3.scaleLinear()
        .domain([d3.min(data, function(d) { return d.body_mass_g; }), d3.max(data, function(d) { return d.body_mass_g; })])
        .range([height, 0]);
    svg.append("g")
        .call(d3.axisLeft(y));


    //color scales
    var color = d3.scaleOrdinal()
        .domain(["Adelie", "Chinstrap", "Gentoo"]) // Assuming these are your three species categories
        .range(["#ff7f0e", "#2ca02c", "#1f77b4"]); // Define colors for each category

    // Add dots
    svg.selectAll("dot")
        .data(data)
        .enter().append("circle")
        .attr("cx", function(d) { return x(d.flipper_length_mm); })
        .attr("cy", function(d) { return y(d.body_mass_g); })
        .attr("r", 1.5)
        .style("fill", function(d) { return color(d.species); })
        .style("opacity", 0.8); // Set opacity to 80%

});
