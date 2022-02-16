// COOL CATS -------------------------------------------------------------------------------

// Set graph & margin dimensions
const margin = {top: 80, right: 30, bottom:20, left: 80},
    width = 750 - margin.left - margin.right,
    height = 600 - margin.top - margin.bottom;

// append the svg object to the body of the page
const svg = d3.select("#CoolCats")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", `translate(${margin.left},${margin.top})`);

//Read in CSV data
d3.csv("CoolCats2.csv",
  // Format both variables (incl. convert date string -> date type)
  function(d){
    return { date : d3.timeParse("%Y-%m-%d")(d.date), price : d.price }
  })
  // Then draw graph
  .then(function(data) {

    // Add X axis --> it is a date format
    const x = d3.scaleTime()
      .domain(d3.extent(data, function(d) { return d.date; }))
      .range([ 0, width ]);
    svg.append("g")
      .attr("transform", `translate(0, ${height})`)
      .call(d3.axisBottom(x));

    // Add Y axis
    const y = d3.scaleLinear()
      .domain([0, d3.max(data, function(d) { return +d.price; })])
      .range([ height, 0 ]);
    svg.append("g")
      .call(d3.axisLeft(y));

    // Add the line
    svg.append("path")
      .datum(data)
      .attr("fill", "none")
      .attr("stroke", "midnightblue")
      .attr("stroke-width", 1.5)
      .attr("d", d3.line()
        .x(function(d) { return x(d.date) })
        .y(function(d) { return y(d.price) }));

        var mouseCircle = causation.append("g") // for each line, add group to hold text and circle
        .attr("class","mouseCircle"); 
  
    mouseCircle.append("circle") // add a circle to follow along path
      .attr("r", 7)
      .style("stroke", function(d) { console.log(d); return color(d.key); })
      .style("fill","none")
      .style("stroke-width", "1px"); 
    
    mouseCircle.append("text")
      .attr("transform", "translate(10,3)"); // text to hold coordinates

    // Add chart title
    svg.append('text')
        .attr('text-anchor', 'middle')
        .attr('y', -(margin.top/2))
        .attr('x', width/2)
        .text("'Cool Cats' Average Daily Transaction Price")
        .style('font', '22px Avenir')
        .attr('fill', '#2c3e50')
        .style('font-weight', 600);

    svg.append('text')
        .attr('text-anchor', 'middle')
        .attr('y', -(margin.top/5))
        .attr('x', width/2)
        .text("(September 2021 - January 2022)")
        .style('font', '18px Avenir')
        .attr('fill', '#2c3e50')
        .style('font-weight', 400);
        
    // Add Y-Axis label
    svg.append('text')
        .attr('text-anchor', 'middle')
        .attr('y', -(margin.left/2))
        .attr('x', -(height/2))
        .text('Price (ETH)')
        .style('font', '18px Avenir')
        .attr('fill', '#2c3e50')
        .attr('transform', 'rotate(-90)')
        .style('font-weight', 400);
})

// BORED APES ------------------------------------------------------------------------------

// const svg2 = d3.select("#BoredApes")
//   .append("svg")
//     .attr("width", width + margin.left + margin.right)
//     .attr("height", height + margin.top + margin.bottom)
//   .append("g")
//     .attr("transform", `translate(${margin.left},${margin.top})`);

// //Read in CSV data
// d3.csv("BoredApes2.csv",
//   // Format both variables (incl. convert date string -> date type)
//   function(d){
//     return { date : d3.timeParse("%Y-%m-%d")(d.date), price : d.price }
//   })
//   // Then draw graph
//   .then(function(data) {

//     // Add X axis --> it is a date format
//     const x = d3.scaleTime()
//       .domain(d3.extent(data, function(d) { return d.date; }))
//       .range([ 0, width ]);
//     svg2.append("g")
//       .attr("transform", `translate(0, ${height})`)
//       .call(d3.axisBottom(x));

//     // Add Y axis
//     const y = d3.scaleLinear()
//       .domain([0, d3.max(data, function(d) { return +d.price; })])
//       .range([ height, 0 ]);
//     svg2.append("g")
//       .call(d3.axisLeft(y));

//     // Add the line
//     svg2.append("path")
//       .datum(data)
//       .attr("fill", "none")
//       .attr("stroke", "midnightblue")
//       .attr("stroke-width", 1.5)
//       .attr("d", d3.line()
//         .x(function(d) { return x(d.date) })
//         .y(function(d) { return y(d.price) }));

//     // Add chart title
//     svg2.append('text')
//         .attr('text-anchor', 'middle')
//         .attr('y', -(margin.top/2))
//         .attr('x', width/2)
//         .text("'Bored Apes' Average Daily Transaction Price")
//         .style('font', '22px Avenir')
//         .attr('fill', '#2c3e50')
//         .style('font-weight', 600);

//     svg2.append('text')
//         .attr('text-anchor', 'middle')
//         .attr('y', -(margin.top/5))
//         .attr('x', width/2)
//         .text("(July 2021 - January 2022)")
//         .style('font', '18px Avenir')
//         .attr('fill', '#2c3e50')
//         .style('font-weight', 400);
        
//     // Add Y-Axis label
//     svg2.append('text')
//         .attr('text-anchor', 'middle')
//         .attr('y', -(margin.left/2))
//         .attr('x', -(height/2))
//         .text('Price (ETH)')
//         .style('font', '18px Avenir')
//         .attr('fill', '#2c3e50')
//         .attr('transform', 'rotate(-90)')
//         .style('font-weight', 400);
// })
