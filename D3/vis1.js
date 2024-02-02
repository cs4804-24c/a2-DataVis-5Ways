const svg = d3.select('svg');

const width = +svg.attr('width');
const height = +svg.attr('height');

const render = data => {
  const title = 'Penglings Data';
  
  const xValue = d => d.flipper_length_mm;
  const xAxisLabel = 'Flipper Length mm';
  
  const yValue = d => d.body_mass_g;
  const yAxisLabel = 'Body Mass g';
  
  const margin = { top: 60, right: 200, bottom: 88, left: 150 };
  const innerWidth = width - margin.left - margin.right;
  const innerHeight = height - margin.top - margin.bottom;
  
  const xScale = d3.scaleLinear()
    .domain(d3.extent(data, xValue))
    .range([0, innerWidth])
    .nice();
  
  const yScale = d3.scaleLinear()
    .domain(d3.extent(data, yValue))
    .range([innerHeight, 0])
    .nice();

  function circleSize(billSize){
    return (billSize/5);
  }

  function color(species){
    if(species == "Adelie")
        return "#FF9900";
    if(species == "Chinstrap")
        return "#FF00FF";
    if(species == "Gentoo")
        return "#008080";
  }
  
  const g = svg.append('g')
    .attr('transform', `translate(${margin.left},${margin.top})`);
  
  const xAxis = d3.axisBottom(xScale)
    .tickSize(-innerHeight)
    .tickPadding(15);
  
  const yAxis = d3.axisLeft(yScale)
    .tickSize(-innerWidth)
    .tickPadding(10);
  
  const yAxisG = g.append('g').call(yAxis);
  yAxisG.selectAll('.domain').remove();
  
  yAxisG.append('text')
      .attr('class', 'axis-label')
      .attr('y', -93)
      .attr('x', -innerHeight / 2)
      .attr('fill', 'black')
      .attr('transform', `rotate(-90)`)
      .attr('text-anchor', 'middle')
      .text(yAxisLabel);
  
  const xAxisG = g.append('g').call(xAxis)
    .attr('transform', `translate(0,${innerHeight})`);
  
  xAxisG.select('.domain').remove();
  
  xAxisG.append('text')
      .attr('class', 'axis-label')
      .attr('y', 75)
      .attr('x', innerWidth / 2)
      .attr('fill', 'black')
      .text(xAxisLabel);
  
  g.selectAll('circle').data(data)
    .enter().append('circle')
      .attr('fill-opacity', '0.8')
      .attr('cy', d => yScale(yValue(d)))
      .attr('cx', d => xScale(xValue(d)))
      .attr('r', d => circleSize(d.bill_length_mm))
      .style('fill', d => color(d.species));
  
  g.append('text')
      .attr('class', 'title')
      .attr('y', -10)
      .attr('x', innerWidth/2 - 55)
      .text(title);
  
  g.append('text')
  .attr('class', 'legend')
  .attr('y', 35)
  .attr('x', innerWidth+35)
  .text("Bill Length (mm)");

  g.append('circle')
  .attr('class', 'legend')
  .attr('cx', innerWidth+35)
  .attr('cy', 50)
  .attr('r', circleSize(40));

  g.append('text')
  .attr('class', 'legend')
  .attr('y', 55)
  .attr('x', innerWidth+50)
  .text("40");

  g.append('circle')
  .attr('class', 'legend')
  .attr('cx', innerWidth+35)
  .attr('cy', 75)
  .attr('r', circleSize(50));

  g.append('text')
  .attr('class', 'legend')
  .attr('y', 80)
  .attr('x', innerWidth+50)
  .text("50");


  g.append('text')
  .attr('class', 'legend')
  .attr('y', 115)
  .attr('x', innerWidth+35)
  .text("species");

  g.append('circle')
  .attr('class', 'legend')
  .attr('cx', innerWidth+35)
  .attr('cy', 135)
  .attr("fill", color("Adelie"))
  .attr('r', circleSize(35));

  g.append('text')
  .attr('class', 'legend')
  .attr('x', innerWidth+50)
  .attr('y', 140)
  .text("Adelie");

  g.append('circle')
  .attr('class', 'legend')
  .attr('cx', innerWidth+35)
  .attr('cy', 160)
  .attr("fill", color("Chinstrap"))
  .attr('r', circleSize(35));

  g.append('text')
  .attr('class', 'legend')
  .attr('x', innerWidth+50)
  .attr('y', 165)
  .text("Chinstrap");

  g.append('circle')
  .attr('class', 'legend')
  .attr('cx', innerWidth+35)
  .attr('cy', 190)
  .attr("fill", color("Gentoo"))
  .attr('r', circleSize(35));

  g.append('text')
  .attr('class', 'legend')
  .attr('x', innerWidth+50)
  .attr('y', 195)
  .text("Gentoo");
};

d3.csv('../penglings.csv')
  .then(data => {
    data.forEach(d => {
      d.flipper_length_mm = +d.flipper_length_mm;
      d.body_mass_g = +d.body_mass_g;
      d.species = d.species;
      
    });
    render(data);
  });