//Used a1 assignment for starter code, https://d3-graph-gallery.com/graph/scatter_basic.html as a resource to learn about building scatter plots in d3.


console.log(d3); // test if d3 is loaded

var margin = {top: 10, right: 30, bottom: 30, left: 60},

width = 1280 - margin.left - margin.right,
height = 720 - margin.top - margin.bottom;

let svg = d3.select("#svg-holder")
    .append('svg')
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

let colors = {
    'Adelie': '#f8a452',
    'Gentoo': '#4ea0a1',
    'Chinstrap': '#b056cf'
}

d3.csv("penglings.csv").then( (inputData) => {

    let billLengthList = inputData.map( x => parseFloat(x.bill_length_mm)).filter( x => !isNaN(x))

    let x = d3.scaleLinear()
        .domain([170, 235])
        .range([ 0, width ]);
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x))

    let y = d3.scaleLinear()
        .domain([2500, 6500])
        .range([height, 0]);
    svg.append("g")
        .call(d3.axisLeft(y));

    let z = d3.scaleLinear()
        .domain([Math.min(...billLengthList), Math.max(...billLengthList)])
        .range([ 5, 20]);

    svg.append('g')
    .selectAll("dot")
    .data(inputData)
    .join("circle")
        .attr("cx", d => x(d.flipper_length_mm))
        .attr("cy", d => y(d.body_mass_g))
        .attr("r", d => z(d.bill_length_mm))
        .style("fill", d => colors[d.species])
})
