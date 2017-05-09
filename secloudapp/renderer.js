// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// All of the Node.js APIs are available in this process.

function run(file){
  if(file==""){
    dialog.showErrorBox('File Error','Select a file before running the classifier.');
    return;
  }
  const path = require('path');
  const scriptFilename = path.join(__dirname, '../', 'svm.py');
  var py = require('child_process').spawn('python', [scriptFilename, '-f', file]);

  // Read python output line by line and append to array
  readline = require('readline');
  global.neither = []
  global.sinks = []
  global.sources = []
  rl = readline.createInterface(py.stdout, py.stdin);
  rl.on('line', function (data) {
    // Get the last word to find out the class.
    // Classes saved on different arrays for color based on class.
    last = data.split(" ").splice(-1);
    // Populate the array for neither class
    if(last=="Neither"){
      var lastIndex = data.lastIndexOf(" ");
      str = data.substring(0, lastIndex);
      global.neither.push(str);
    }
    // Populate the array for sources class
    if(last=="Source"){
      var lastIndex = data.lastIndexOf(" ");
      str = data.substring(0, lastIndex);
      global.sources.push(str);
    }
    // Populate the array for sinks class
    if(last=="Sink"){
      var lastIndex = data.lastIndexOf(" ");
      str = data.substring(0, lastIndex);
      global.sinks.push(str);
    }
  });

  py.on('close', ()=>{
    // Python ends, fill html with the data
    let result = document.querySelector('#result');
    create_pie(global.sources.length, global.sinks.length, global.neither.length);
    result.innerHTML = populate_html_array(global.sources, global.sinks, global.neither);
    global.neither = [];
    global.sinks= [];
    global.sources = [];
  })
}

function populate_html_array(m_sources, m_sinks, m_neither){
  // Create the array holding the html elements
  html_array = [];
  html_array.push('<table class="table"><thead><tr><th>#</th><th>Method Name</th><th>Class</th></thead>');
  html_array.push('<tbody>');
  var counter = 1;
  for(var i=0;i<m_sources.length;i++){
    html_array.push('<tr class="tr_source"><td>'+counter+'</td><td>'+m_sources[i]+'</td><td>Source</td>');
    counter++;
  };
  for(var i=0;i<m_sinks.length;i++){
    html_array.push('<tr class="tr_sink"><td>'+counter+'</td><td>'+m_sinks[i]+'</td><td>Sink</td>');
    counter++;
  };
  for(var i=0;i<m_neither.length;i++){
    html_array.push('<tr class="tr_neither"><td>'+counter+'</td><td>'+m_neither[i]+'</td><td>Neither</td>');
    counter++;
  };

  html_array.push('</tbody></table>');
  return html_array.join("");
}

function create_pie(sources, sinks, neither){
  let over = document.querySelector('#overview');
  over.textContent='Chart';
  let cl = document.querySelector('#classification');
  cl.textContent='Classification Results';
  let st = document.querySelector('#startpage');
  st.style.display="none";
  let chart_cont = document.querySelector('#chartContainer');
  //clear previous chart cause it breaks the app
  chart_cont.innerHTML = "&nbsp;";
  chart_cont.innerHTML = '<canvas id="myChart" width="250" height="100"></canvas>';
  var ctx = document.getElementById("myChart").getContext("2d");
  var data = {
    labels: [
        "Sources",
        "Sinks",
        "Neither"
    ],
    datasets: [
        {
            data: [sources, sinks, neither],
            backgroundColor: [
                'rgba(255,0,0,0.3)',
                'rgba(128,0,128,0.5)',
                'rgba(0,255,0,0.3)'
            ],
            hoverBackgroundColor: [
              'rgba(255,0,0,0.5)',
              'rgba(128,0,128,0.7)',
              'rgba(0,255,0,0.5)'
            ]
        }]
};
  var myDoughnutChart = new Chart(ctx, {
      type: 'doughnut',
      data: data
  })
}
