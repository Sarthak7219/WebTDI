
    var myDataArray = []; // Create an array to store the data

    for (var i = 1; i <= 18; i++) {
        var myDattaElement = document.getElementById(`my-datta${i}`);
        var myDatta = myDattaElement.getAttribute("data-my-data");
        myDataArray.push(myDatta); // Store the data in the array
    }
    var myDattaElement1 = document.getElementById("my-datta1");
    var myDatta1 = myDattaElement1.getAttribute("data-my-data");
    var myDattaElement2 = document.getElementById("my-datta2");
    var myDatta2 = myDattaElement2.getAttribute("data-my-data");
    var myDattaElement3= document.getElementById("my-datta3");
    var myDatta3= myDattaElement3.getAttribute("data-my-data");
    var myDattaElement4= document.getElementById("my-datta4");
    var myDatta4= myDattaElement4.getAttribute("data-my-data");
    var myDattaElement5= document.getElementById("my-datta5");
    var myDatta5= myDattaElement5.getAttribute("data-my-data");
    const datta = {
        labels: ['January', 'February', 'March', 'April', 'May'],
        datasets: [
          {
            label: 'Sales',
            data: [myDatta1,myDatta2,myDatta3,myDatta4,myDatta5],
            fill: false,
            backgroundColor: 'rgba(75,192,192,0.4)',
            borderColor: 'rgba(75,192,192,1)',
            borderWidth: 1,
          },
        ],
      };
      
      const configg = {
        type: 'bar',
        data: datta,
        options: {
          indexAxis: 'y',
          scales: {
            xAxes: [
              {
                ticks: {
                  beginAtZero: true,
                },
              },
            ],
          },
        },
      };
      
      const myChartt = new Chart(document.getElementById('censored-graph'), configg);
