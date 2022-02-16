// Select SVG container
const svg = d3.select('svg');

// Grad data from JSON
d3.json('planets.json').then(data => {

    // Add circles (planets) to the DOM
    const circs = svg.selectAll('circle')
        .data(data);

    // Add attributes to circles in the DOM already
    circs.attr('cy', 200)
        .attr('cx', d => d.distance)
        .attr('r', d => d.radius)
        .attr('fill', d => d.fill);
    
    // Append the enter selection to the DOM
    circs.enter()
        .append('circle')
        .attr('cy', 200)
        .attr('cx', d => d.distance)
        .attr('r', d => d.radius)
        .attr('fill', d => d.fill);
})
