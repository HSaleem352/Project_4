// #################################################################################################################
// ##                                                Timing                                                       ##
// #################################################################################################################

d3.json("/api/v1/AFR_timing_df").then(function(data) {

    var mild = data.mild;
    var labels = ["point 1", "point 2", "point 3", "point 4"];
  
    var trace = {
      x: labels,
      y: mild,
      marker:{
        color: "blue"},
        type: "bar"
    };

    var data = [trace];
  
    var layout = {
      title: "Mild Covid Outcomes at Each Time Point",
      margin: {
        l: 200,
        r: 200,
        t: 200,
        b: 200,
      }
      };
  
    Plotly.newPlot("afr_mild_bar", data, layout);
  
  });

  d3.json("/api/v1/AFR_timing_df").then(function(data) {

    var moderate = data.moderate;
    var labels = ["point 1", "point 2", "point 3", "point 4"];
  
    var trace = {
      x: labels,
      y: moderate,
      marker:{
        color: "blue"},
        type: "bar"
    };

    var data = [trace];
  
    var layout = {
      title: "Moderate Covid Outcomes at Each Time Point",
      margin: {
        l: 200,
        r: 200,
        t: 200,
        b: 200,
      }
      };
  
    Plotly.newPlot("afr_moderate_bar", data, layout);
  
  });

  d3.json("/api/v1/AFR_timing_df").then(function(data) {

    var severe = data.severe;
    var labels = ["point 1", "point 2", "point 3", "point 4"];
  
    var trace = {
      x: labels,
      y: severe,
      marker:{
        color: "blue"},
        type: "bar"
    };

    var data = [trace];
  
    var layout = {
      title: "Severe Covid Outcomes at Each Time Point",
      margin: {
        l: 200,
        r: 200,
        t: 200,
        b: 200,
      }
      };
  
    Plotly.newPlot("afr_severe_bar", data, layout);
  
  });

  