var svg = d3.select("#chart");
var data = d3.csv("./penglings.csv", d => {

const x = d3.scaleLinear()
    .domain([168, 234])
    .range([0, 600]);
svg.append("g")
    .attr("transform", "translate(0, 600)")
    .call(d3.axisBottom(x));

const y = d3.scaleLinear()
    .domain([2600, 6450])
    .range([600, 0]);
svg.append("g")
    .call(d3.axisLeft(y));

svg.append("g")
    .selectAll("dot")
    .data(d)
    .enter()
    .append("circle")
    .attr("cx", d => x(d.flipper_length_mm))
    .attr("cy", d => y(d.body_mass_g))
    .attr("r", d => d.bill_depth_mm)
    .style("fill", d => {switch(d.species) {
        case "Adelie": return "#fda246";
        case "Chinstrap": return "#ac5ad4";
        case "Gentoo": return "#49a1a1";
    }});
});