// Initialise data & svg
const data = [
    {width: 200, height: 200, fill: 'purple'},
    {width: 100, height: 60, fill: 'pink'},
    {width: 50, height: 30, fill: 'red'}
];
const svg = d3.select('svg');

/*  Edit SVG (not hard coding, linked instead)
d = data (with various attributes: width, height, fill)
i = index of element in the array (0)
n = current selection (type 'rect') */

// Join data to rects (array of rectangles)
const rects = svg.selectAll('rect')
    .data(data)
    
// Add attrs to rects already in the DOM (arrow functions)
rects.attr('width', (d, i, n) => {return d.width})
    // Simplified arrow format
    .attr('height', (d, i, n) => d.height)
    // Regular function format
    .attr('fill', function(d, i, n){return d.fill});

// Append the remaining rectsm and add attrs 
rects.enter()
    .append('rect')
    .attr('width', d => d.width)
    .attr('height', d => d.height)
    .attr('fill', d => d.fill);