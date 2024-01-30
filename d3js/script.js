// Set up the dximensions of the SVG container
const width = 600;
const height = 400;
const margin = { top: 20, right: 20, bottom: 40, left: 40 };
const colorScale = d3.scaleOrdinal()
    .domain(['Adiele', 'Gentoo', 'Chinstrap'])
    .range(['#1f77b4', '#ff7f0e', '#2ca02c']);
const xAxisLabel = 'Flipper Length (mm)';
const yAxisLabel = 'Body Mass (g)';


// Create an SVG container
const svg = d3.select('body').append('svg')
    .attr('width', width + margin.left + margin.right + 200)
    .attr('height', height + margin.top + margin.bottom)
    .append('g')
    .attr('transform', `translate(${margin.left + 50},${margin.top})`);

// Load CSV data
d3.csv('../penglings.csv').then(data => {
    // Convert string numbers to numeric values
    data.forEach(d => {
        d.flipper_length_mm = +d.flipper_length_mm;
        d.body_mass_g = +d.body_mass_g;
        d.bill_length_mm = +d.bill_length_mm;
    });

    // Create scales
    const xScale = d3.scaleLinear()
        .domain([d3.min(data, d => d.flipper_length_mm), d3.max(data, d => d.flipper_length_mm)])
        .range([0, width]);

    const yScale = d3.scaleLinear()
        .domain([d3.min(data, d => d.body_mass_g), d3.max(data, d => d.body_mass_g)])
        .range([height, 0]);

    const sizeScale = d3.scaleLinear()
        .domain([d3.min(data, d => d.bill_length_mm), d3.max(data, d => d.bill_length_mm)])
        .range([2, 5]); // Adjust the range as needed

    console.log(data.map(d => sizeScale(d.bill_length_mm)));
    // Create the scatter plot
    svg.selectAll('circle')
        .data(data)
        .enter()
        .append('circle')
        .attr('cx', d => xScale(d.flipper_length_mm))
        .attr('cy', d => yScale(d.body_mass_g))
        //.attr('r', 5)
        .attr('r', d => sizeScale(d.bill_length_mm))
        .attr('fill', d => colorScale(d.species)) // Define a color scale for species
        .attr('opacity', 0.8); // Set opacity

    // Create axes
    const xAxis = d3.axisBottom(xScale);
    const yAxis = d3.axisLeft(yScale);

    svg.append('g')
        .attr('transform', `translate(0, ${height})`)
        .call(xAxis)

    svg.append('text')
    .attr('class', 'axis-label')
    .attr('text-anchor', 'middle')
    .attr('x', width / 2)
    .attr('y', height + margin.top + 15)
    .text(xAxisLabel);


    svg.append('g')
        .call(yAxis);

    svg.append('text')
    .attr('class', 'axis-label')
    .attr('text-anchor', 'middle')
    .attr('x', -margin.left -180)
    .attr('y', height / 2 -220)
    .attr('dy', '-2.5em')  // Adjust position based on your preference
    .attr('transform', 'rotate(-90)')
    .text(yAxisLabel);

// Create size scale legend
const sizeLegend = svg.append('g')
    .attr('class', 'size-legend')
    .attr('transform', `translate(${width - 100},${height - 50})`); // Adjust the position

// Specify the desired labels for the size scale
const sizeLegendData = [40, 50];

// Define the size scale for the legend
const sizeLegendScale = d3.scaleLinear()
    .domain([d3.min(data, d => d.bill_length_mm), d3.max(data, d => d.bill_length_mm)])
    .range([2, 5]);

// Add a label above the size legend
sizeLegend.append('text')
    .attr('class', 'legend-label')
    .attr('x', 40)
    .attr('y', 40) // Adjust the vertical position
    .attr('text-anchor', 'middle')
    .text('bill_length_mm');

sizeLegend.selectAll('circle')
    .data(sizeLegendData)
    .enter()
    .append('circle')
    .attr('cx', 0)
    .attr('cy', (d, i) => -i * 20) // Adjust spacing between circles
    .attr('r', d => sizeLegendScale(d))
    .attr('fill', 'none')
    .attr('stroke', '#000');

sizeLegend.selectAll('text')
    .data(sizeLegendData)
    .enter()
    .append('text')
    .attr('x', 20)
    .attr('y', (d, i) => -i * 20)
    .attr('dy', '0.4em')
    .text(d => d + ' mm'); // Include 'mm' in the text label



    // Create legend
    const legend = svg.append('g')
        .attr('transform', `translate(${width + 10}, 10)`);

    const legendRectSize = 18;
    const legendSpacing = 4;

    const legendItems = legend.selectAll('.legend-item')
        .data([...new Set(data.map(d => d.species))])
        .enter()
        .append('g')
        .attr('class', 'legend-item')
        .attr('transform', (d, i) => `translate(0, ${i * (legendRectSize + legendSpacing)})`);

    legendItems.append('rect')
        .attr('width', legendRectSize)
        .attr('height', legendRectSize)
        .attr('fill', d => colorScale(d));

    legendItems.append('text')
        .attr('x', legendRectSize + legendSpacing)
        .attr('y', legendRectSize - legendSpacing)
        .text(d => d);

});