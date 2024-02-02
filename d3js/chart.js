window.onload = () => {
    const margin = {top: 20, right: 20, left: 80, bottom: 50},
          width = (2 * 565) - margin.left - margin.right,
          height = (2 * 349) - margin.top - margin.bottom;

    var x = d3.scaleLinear().domain([168, 233]).range([0, width]);
    var y = d3.scaleLinear().domain([2400, 6450]).range([height, 0]);

    var svg = d3.select("body").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    const data = d3.csv("./penglings.csv").then(d => {
        d = d.filter(val => val.bill_length_mm !== "NA")

        svg.append("g")
            .selectAll("dot")
            .data(d)
            .enter()
            .append("circle")
            .attr("cx", d => x(d.flipper_length_mm))
            .attr("cy", d => y(d.body_mass_g))
            .attr("r", d => d.bill_length_mm / 3)
            .style("opacity", 0.8)
            .style("fill", d => {switch(d.species) {
                case "Adelie": return "#fda246";
                case "Chinstrap": return "#ac5ad4";
                case "Gentoo": return "#49a1a1";
            }});
    });
    
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));
  
    svg.append("g")
        .call(d3.axisLeft(y));

    svg.append("text")
        .attr("text-anchor", "middle")
        .attr("x", width / 2 + margin.left / 2)
        .attr("y", height + 35)
        .text("Flipper Length (mm)");

    svg.append("text")
        .attr("transform", "rotate(-90)")
        .attr("text-anchor", "middle")
        .attr("x", -(height / 2))
        .attr("y", -40)
        .text("Body Mass (g)");

    svg.selectAll("line.horizontalGrid")
        .data(y.ticks(7))
        .enter()
        .append("line")
        .attr("class", "horizontalGrid")
        .attr("x1", 0)
        .attr("x2", width)
        .attr("y1", d => y(d) + 1)
        .attr("y2", d => y(d) + 1)
        .attr("fill", "none")
        .attr("shape-rendering", "crispEdges")
        .attr("stroke", "#ebebeb")
        .attr("stroke-width", "1px");

    svg.selectAll("line.verticalGrid")
        .data(x.ticks(13))
        .enter()
        .append("line")
        .attr("class", "horizontalGrid")
        .attr("x1", d => x(d))
        .attr("x2", d => x(d))
        .attr("y1", margin.bottom)
        .attr("y2", height)
        .attr("fill", "none")
        .attr("shape-rendering", "crispEdges")
        .attr("stroke", "#ebebeb")
        .attr("stroke-width", "1px");

    var svg2 = d3.select("body").append("svg")
        .attr("width", 200)
        .attr("height", height);

    svg2.append("text")
        .attr("text-anchor", "middle")
        .attr("x", 100)
        .attr("y", 20)
        .text("bill_length_mm");

    svg2.append("text")
        .attr("text-anchor", "left")
        .attr("x", 100)
        .attr("y", 50)
        .text("40");

    svg2.append("circle")
        .attr("cx", 70)
        .attr("cy", 44)
        .attr("r", 12);

    svg2.append("text")
        .attr("text-anchor", "left")
        .attr("x", 100)
        .attr("y", 85)
        .text("50");

    svg2.append("circle")
        .attr("cx", 70)
        .attr("cy", 78.5)
        .attr("r", 15);

    svg2.append("text")
        .attr("text-anchor", "middle")
        .attr("x", 100)
        .attr("y", 150)
        .text("species");
    
    svg2.append("circle")
        .attr("cx", 80)
        .attr("cy", 175)
        .attr("r", 10)
        .attr("fill", "#fda246");
    svg2.append("circle")
        .attr("cx", 80)
        .attr("cy", 205)
        .attr("r", 10)
        .attr("fill", "#ac5ad4");         
    svg2.append("circle")
        .attr("cx", 80)
        .attr("cy", 235)
        .attr("r", 10)
        .attr("fill", "#49a1a1");

    svg2.append("text")
        .attr("text-anchor", "left")
        .attr("x", 100)
        .attr("y", 180)
        .text("Adelie");
    svg2.append("text")
        .attr("text-anchor", "left")
        .attr("x", 100)
        .attr("y", 210)
        .text("Chinstrap");
    svg2.append("text")
        .attr("text-anchor", "left")
        .attr("x", 100)
        .attr("y", 240)
        .text("Gentoo");
}