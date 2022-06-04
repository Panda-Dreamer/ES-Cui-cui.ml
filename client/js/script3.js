var script = document.createElement('script');
script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js';
document.getElementsByTagName('head')[0].appendChild(script);

document.getElementById('fileSelect').addEventListener('change', function() {
    console.log("Changed files");
    
    var files = document.getElementById('fileSelect').files;
    if (files.length > 0) {
      gentiltoutou(files[0]);
    }
    else {
        console.log('non')
    }
    
  });


  
function gentiltoutou(file) {
  var reader = new FileReader();
  reader.readAsDataURL(file);
  reader.onload = function () {
    console.log(reader.result);
    var tav = reader.result
    console.log(tav)
    gentilpetittoutou(tav)
  };
  reader.onerror = function (error) {
    console.log('Error: ', error);
  };

}

function gentilpetittoutou(filesend) {
  const fetch = require("node-fetch");

  fetch("https://cui-cui.ml/api/analyze", {
    method: "POST",
    headers: {
      "Content-type": "application/json",
    },
    body: filesend,
  })
    .catch(err => {
      console.log(err)
    })
    .then(result => {
      console.log(result)
      //var result2 = JSON.parse(result)
      console.log(result2)
      //gentilminou(result2)
      gentilminou(result)
    })

}


function gentilminou(resultat){
  try{
  var resultatStr = JSON.stringify(resultat);
  $.ajax({
    url: 'result.php',
    type: 'post',
    data: {resultat:resultatStr},
    success: function (response) {
      console.log("ça a marché!!")  
    }
  });}
  catch(e){
    console.log(e)
  }
}