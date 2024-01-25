const width = 900;
const height = 500;

const adelieColor = "#FBA044"
const chinstrapColor = "#AA58D2"
const gentooColor = "#479F9F"

const scale = {
  x: d3.scaleLinear().domain([160, 240]).range([0, width]),
  y: d3.scaleLinear().domain([2000, 7000]).range([height, 0])
}

d3.csv("../penglings.csv").then(function(data) {
  // Set up the SVG container
  var svg = d3.select("body")
    .append("svg")
    .attr("width", width)
    .attr("height", height);

  appendLabels(svg)
  appendGrid(svg)
  appendTicks(svg)
  mapDots(svg, data)
  appendLegend(svg)
});

function appendLabels(svg) {
    // Title
    svg.append('text')
    .attr('x', width/2)
    .attr('y', 30)
    .attr('text-anchor', 'middle')
    .style('font-family', 'Helvetica')
    .style('font-size', 20)
    .text('Scatterplot of Flipper Length vs. Body Mass');
    
    // X label
    svg.append('text')
    .attr('x', width/2)
    .attr('y', height)
    .attr('text-anchor', 'middle')
    .style('font-family', 'Helvetica')
    .style('font-size', 12)
    .text('Flipper Length (mm)');
    
    // Y label
    svg.append('text')
    .attr('x', height/2) // We're rotated!!!
    .attr('text-anchor', 'middle')
    .attr('transform', 'translate(60,' + height + ')rotate(-90)')
    .style('font-family', 'Helvetica')
    .style('font-size', 12)
    .text('Body Mass (g)');
}

function appendGrid(svg) {
    // Create grid lines for the x axis
    svg.append("g")
    .attr("class", "grid")
    .attr("transform", "translate(0," + height + ")")
    .attr("color", "#e0e0e0")
    .call(d3.axisBottom(scale.x)
    .tickSize(-height)
    .tickFormat("")
    );
    
    // Create grid lines for the y axis
    svg.append("g")
    .attr("class", "grid")
    .attr("color", "#e0e0e0")
    .call(d3.axisLeft(scale.y)
      .tickSize(-width)
      .tickFormat("")
    );
}

/** Create a circle for each datapoint */
function mapDots(svg,data) {
  
  svg.selectAll("circle")
    .data(data)
    .enter()
    .append("circle")

    .attr("cx", function(d) {
      var value = +d["flipper_length_mm"];
      return isNaN(value) ? 0 : scale.x(value);
    })

    .attr("cy", function(d) {
      var value = +d["body_mass_g"];
      return isNaN(value) ? 0 : scale.y(value);
    })

    .attr("r", function(d) {
      var value = +d["bill_length_mm"];
      return isNaN(value) ? 0 : value / 6;
    })

    .attr("fill", function(d) {
      switch (d["species"]) {
        case "Adelie":
          return adelieColor+"99";
        case "Chinstrap":
          return chinstrapColor+"99";
        case "Gentoo":
          return gentooColor+"99";
        default:
          return "black";
      }
    })

    .attr("stroke", function(d) {
      switch (d["species"]) {
        case "Adelie":
          return adelieColor;
        case "Chinstrap":
          return chinstrapColor;
        case "Gentoo":
          return gentooColor;
        default:
          return "black";
      }
    })
    
    .attr("stroke-width", 2);
}

function appendTicks(svg) {
  svg.append("g")
  .attr("transform", `translate(${0}, ${height - 30})`)
  .call(d3.axisBottom(scale.x));

  svg.append("g")
  .attr("transform", `translate(${40}, ${0})`)
  .call(d3.axisLeft(scale.y));
} 

function appendLegend(svg) {
  const legencColors = [
    { species: "Adelie", color: adelieColor },
    { species: "Chinstrap", color: chinstrapColor },
    { species: "Gentoo", color: gentooColor }
  ];

  const legend = svg.append("g")
    .attr("transform", `translate(${width - 120}, ${height - 100})`);

  const legencColorItems = legend.selectAll()
    .data(legencColors)
    .enter()
    .append("g")
    .attr("transform", (d, i) => `translate(0, ${i * 20})`);

  legencColorItems.append("circle")
    .attr("r", 5)
    .attr("fill", d => d.color);

  legencColorItems.append("text")
    .attr("x", 20)
    .attr("y", 5)
    .text(d => d.species)
    .style("font-size", "0.75rem")
    .style("font-family", "Helvetica");
}