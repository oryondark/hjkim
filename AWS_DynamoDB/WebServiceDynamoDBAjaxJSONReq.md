### ajax get query Example
```
function getItem(){
  var url = "queryForDynamo.php";
  $.get(url, function(data){
    let jsonDump = JSON.parse(data);
  }
}
```

jsondump.\<DOM\>.\<DOM\>.\<M or S or L etc..\>.\<Attirbute\>.\<M or S or L etc...\>
==> get Value.
