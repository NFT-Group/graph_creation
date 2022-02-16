// set the dimensions and margins of the graph
const margin = {top: 10, right: 30, bottom: 30, left: 60},
        width = 1500 - margin.left - margin.right,
        height = 1200 - margin.top - margin.bottom;
    
// append the svg object to the body of the page
const svg = d3.select("#Regression")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

//Read the data
d3.csv("BoredApes.csv").then( function(data) {

    // Add X axis --> it is a date format
    const x = d3.scaleLinear()
        .domain(d3.extent(data, function(d) { return +d.Actual; }))
      .range([ 0, width ]);
    svg.append("g")
      .attr("transform", `translate(0, ${height})`)
      .call(d3.axisBottom(x));

    // Add Y axis
    const y = d3.scaleLinear()
      .domain([0, d3.max(data, function(d) { return +d.Prediction; })])
      .range([ height, 0 ]);
    svg.append("g")
      .call(d3.axisLeft(y));

    // Add dots
    svg.append('g')
    .selectAll("dot")
    .data(data)
    .join("circle")
        .attr("cx", function (d) { return x(d.Actual); } )
        .attr("cy", function (d) { return y(d.Prediction); } )
        .attr("r", 1.5)
        .style("fill", "#69b3a2")

    var line = d3.svg.line()
        .x(function(d){
            return x(d.Actual);
        })
        .y(function(d){
            return y(d.Prediction);
        });
    svg.append("path")
        .datum(data)    
        .attr("class", "line")
        .attr("d", line)
        
})