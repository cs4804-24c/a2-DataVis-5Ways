//Used a1 assignment for starter code, https://d3-graph-gallery.com/graph/scatter_basic.html as a resource to learn about building scatter plots in d3.
//Used this website to learn about buildings legends in d3 https://d3-graph-gallery.com/graph/custom_legend.html


console.log(d3); // test if d3 is loaded

var margin = {top: 10, right: 100, bottom: 50, left: 60},

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

    svg.append('text')
        .text("Flipper Length (mm)")
        .attr('x', width/2)
        .attr('y', height+margin.bottom-10)

    let y = d3.scaleLinear()
        .domain([2500, 6500])
        .range([height, 0]);
    svg.append("g")
        .call(d3.axisLeft(y));

        
    svg.append('text')
        .text("Body Mass (g)")
        .attr('x', -(height/2))
        .attr('y', -margin.left+15)
        .attr("transform", "rotate(-90)")

    let z = d3.scaleLinear()
        .domain([Math.min(...billLengthList), Math.max(...billLengthList)])
        .range([5, 20]);

    svg.append('g')
    .selectAll("dot")
    .data(inputData)
    .join("circle")
        .attr("cx", d => x(d.flipper_length_mm))
        .attr("cy", d => y(d.body_mass_g))
        .attr("r", d => z(d.bill_length_mm))
        .style("fill", d => colors[d.species])
        .style("opacity", 0.8)
        .on("mouseover", mouseOverEventHandler)
        .on("mousemove", mouseOverEventHandler)
        .on("mouseleave", () => document.getElementById('info').style.visibility="hidden")

    let mult=0
    Object.keys(colors).forEach(k => {
        mult++;
        svg.append("circle")
            .attr("cx", width)
            .attr("cy", 25*mult)
            .attr("r", 10)
            .style("fill", d=> colors[k])
        svg.append("text")
            .attr('x', width+25)
            .attr('y', 25*mult+5)
            .text(k)
    })
})

function mouseOverEventHandler(event, d) {
    let infoDiv = document.getElementById('info');
    infoDiv.style.position = 'absolute'
    infoDiv.style.left =  event.x+10
    infoDiv.style.top = event.y-50
    infoDiv.style.backgroundColor = 'white';
    infoDiv.style.border = "1px solid black";
    infoDiv.style.opacity = 0.75;
    infoDiv.style.padding = '5px'
    infoDiv.innerHTML="";
    infoDiv.style.visibility="visible";
    let div = document.createElement('div');
    let text = document.createElement('text');
    text.innerText=`Flipper Length: ${d.flipper_length_mm}mm\nBody Mass: ${d.body_mass_g}g\nBill length: ${d.bill_length_mm}mm`
    div.appendChild(text)
    infoDiv.appendChild(div)
}

