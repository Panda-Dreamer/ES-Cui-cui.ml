var script = document.createElement("script");
script.src = "https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js";
document.getElementsByTagName("head")[0].appendChild(script);

document.getElementById("fileSelect").addEventListener("change", (e) => {  
  e.preventDefault();
  console.log("Cliked file select");
  const selectedFile = document.getElementById("fileSelect").files[0];

  const formData = new FormData();
  formData.append("complete", true);
  formData.append("audio", selectedFile);
  formData.append("idOnly", true);
  console.log("Sending files...");
  fetch("https://cui-cui.ml/api/analyze", {
    method: "post",
    body: formData,
  })
    .then((res) => {
      console.log("Success");
      let json = res.json().then((json) => {
        if (json.status==false){
          alert("Erreur lors du traitement")
          return 
        }
        console.log(json);
        console.log(json.results[0].specie_name)
        transfo(json.results).then(obj=>{
          upload_results(obj)
        })
      });
    })
    .catch((err) => {
      console.log("Error");
      console.log(err);
    });
});


function transfo(resultat){
  const newobj = {
    'len':resultat.length
}
 i= 1
  let promise = new Promise((resolve, reject) => {
  resultat.forEach(item=>{
    console.log("Processing item: ",i, item)
    if(item.FR_label=="Not found"){
      newobj[`name_${i}`]=item.label.split("_")[0]
    }
    else{
    newobj[`name_${i}`]=item.FR_label.split("_")[1]  
    }

    newobj[`desc_${i}`]=item.desc
    newobj[`conf_${i}`]=item.confidence
    newobj[`image_${i}_1`]=item.images[0]
    newobj[`image_${i}_2`]=item.images[1]
    newobj[`image_${i}_3`]=item.images[2]
    
    i=i+1
  })
    resolve(newobj)
  })
  return promise
}



function upload_results(results) {
  console.log("Dico a afficher:", results)
  for (let i = 1; i < results.len+1; i++) {
    obj = {
      results[``]
    }
    document.cookie=`cuicuiml_data_${i}=${JSON.stringify()}`;
  }
  console.log(obj['name_1']);
  location.href = "result.php"
}

function erreur(){
  alert("L'enregistrement sonore n'est pas encore disponible")
}
  