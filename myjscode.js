function getData(){
  ajaxGetRequest('/linechart', showline)
  ajaxGetRequest('/piechart', showpie)
}

function showline(receive){
      let data = JSON.parse(receive)
      let line = document.getElementById('linegraph')
      Plotly.newPlot(line, data)
  }


function showpie(receive){
  let datalist = JSON.parse(receive)
  let pie = document.getElementById('piegraph')
  Plotly.newPlot(pie, datalist[0],datalist[1])
}
  
