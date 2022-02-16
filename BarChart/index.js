// Select canvas container and append SVG
const svg = d3.select('.canvas')
    .append('svg')
        .attr('width', 600)
        .attr('height', 600);

// Create margins and dimensions
const margin = {
    top: 80,
    right: 20,
    bottom: 100,
    left: 140
};

const graphWidth = 600 - margin.left - margin.right;
const graphHeight = 600 - margin.top - margin.bottom;
const graph = svg.append('g')
    .attr('width', graphWidth)
    .attr('height', graphHeight)
    .attr('transform', `translate(${margin.left}, ${margin.top})`);     // Displaces graph from being flush with top-left of screen

// Create axes groups
const xAxisGroup = graph.append('g')
    .attr('transform', `translate(0, ${graphHeight})`);
const yAxisGroup = graph.append('g');

// Add axis titles
svg.append('text')
    .attr('text-anchor', 'middle')
    .attr('x', graphWidth/2 + margin.left)
    .attr('y', graphHeight + margin.top + margin.bottom)
    .text('NFT Collections')
    .style('font', '18px Avenir')
    .attr('fill', '#2c3e50')
    .style('font-weight', 400);

svg.append('text')
    .attr('text-anchor', 'middle')
    .attr('y', margin.left/3)
    .attr('x', -(margin.top) + -(graphHeight/2))
    .text('Size of Collection (No. of NFTs)')
    .style('font', '18px Avenir')
    .attr('fill', '#2c3e50')
    .attr('transform', 'rotate(-90)')
    .style('font-weight', 400);

// Add axis graph title
svg.append('text')
    .attr('text-anchor', 'middle')
    .attr('y', margin.top/2)
    .attr('x', margin.left + graphWidth/2)
    .text('NFT Collections by Size')
    .style('font', '25px Avenir')
    .attr('fill', '#2c3e50')
    .style('font-weight', 600);

// Source data from JSON and plot bars
d3.json('collections.json').then(data => {
    // Create y-scale (linear scale)
    const y = d3.scaleLinear()
        .domain([0, d3.max(data, d => d.size)])             // Spread of actual datapoints (responseive not hard coded)
        .range([graphHeight, 0]);                           // Range of scale on graph

    // Create x-scale (bandscale)
    const x = d3.scaleBand()
        .domain(data.map(item => item.name))                // Map() cycles through the JSON array and returns an array of all the 'name' variables
        .range([0, 500])
        .paddingInner(0.2)
        .paddingOuter(0.2);

    // Join data to rects
    const rects = graph.selectAll('rect')
        .data(data);

    // Update the rectangle in the DOM
    rects.attr('width', x.bandwidth)                        // Sets standard bar width
        .attr('height', d => (graphHeight - y(d.size)))     // Sets height of bars (passed through the y scale)
        .attr('fill', 'midnightblue')                               // Sets fill for bars
        .attr('x', d => x(d.name))                         // Sets bar spacing
        .attr('y', d => y(d.size));

    // Append remaining bars
    rects.enter()
        .append('rect')
        .attr('width', x.bandwidth)
        .attr('height', d => (graphHeight - y(d.size)))
        .attr('fill', 'midnightblue')
        .attr('x', d => x(d.name))
        .attr('y', d => y(d.size));   
    
    // Create & call the axes
    const xAxis = d3.axisBottom(x);
    const yAxis = d3.axisLeft(y)
        .ticks(5)
        .tickFormat(d => d + ' NFTs');
    
    xAxisGroup.call(xAxis);                     // Runs the axis function on the group, generating the SVGs and adding them to group
    yAxisGroup.call(yAxis);

    xAxisGroup.selectAll('text')
        .attr('transform', 'rotate(-30)')
        .attr('text-anchor', 'end')
        .attr('fill', '#2c3e50')
        .style('font', '16px Avenir');

    yAxisGroup.selectAll('text')
        .attr('fill', '#2c3e50')
        .style('font', '16px Avenir');

    
    const rects = d3.selectAll('rect')
        .on('mouseover', handleMouseOver)
})


/* FIND MIN/ MAX/ EXTENT FROM JSONS

    const min = d3.min(data, d => d.size);      // Returns lowest 'size' count
    const max = d3.max(data, d => d.size);      // Returns highest 'size' count
    const extent = d3.extent(data, d=> d.size); // Returns thr lowest & highest 'size' count

*/

// Event handlers

const handleMouseOver = (d, i, n) => {
    console.log(n[i])
}