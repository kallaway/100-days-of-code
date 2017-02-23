function randomWiki(){
  window.open('https://en.wikipedia.org/wiki/Special:Random')
};

function getSearch(){
  var mUrl = 'https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&list=&continue=&titles=Main+Page&generator=search&formatversion=2&exsentences=2&exlimit=20&exintro=1&explaintext=1&exsectionformat=raw&gsrsearch=' + document.getElementById("search-box").value  +'&gsrnamespace=&gsrlimit=15&gsrqiprofile=wsum_inclinks' ;
//alert(mUrl);
$.ajax({
  url: mUrl,
  dataType:'jsonp',
  success: function(searchResult){
   var resultCount = searchResult["query"]["pages"].length ;
    var i; 
    
    //alert(pageLink);
    for(i = 0 ; i < resultCount ; i++){
     // $("#resultRow").append("<div id=\"result"+i+"\"></div>")
      //var pageLink = searchResult["query"]["pages"][i]["pageid"];
      $("#resultRow").append("<div id=\"title"+i+"\"></div>")
      var title = searchResult["query"]["pages"][i]["title"];
      //$('#title'+i).html("<a href=https://en.wikipedia.org/?curid"+pageLink+"\>" title);
      $("#resultRow").append("<div id=\"extract"+i+"\"></div>")
      var extract = searchResult["query"]["pages"][i]["extract"];
      $('#extract'+i).html(extract);
      
     // alert(pageLink);
    }
    /*$("#resultRow").append("<div id=\"result1\"></div>")
    $("#result1").append("<div id=\"title1\"></div>")
    var title1 = searchResult["query"]["pages"][0]["title"];
     $('#title'+i).html(title1 + "<br>");
    $("#result1").append("<div id=\"extract1\"></div>")
    var extract1 = searchResult["query"]["pages"][0]["extract"];
    $('#extract1').html(extract1 + "<br>");*/
    
    /*for(i = 0 ; i < resultCount ; i++){
      searchResult["query"]["search"][i].title;
      searchResult["query"]["search"][i].snippet;      
    }*/
   /*var title1 = searchResult["query"]["pages"][0]["title"];
     $('#title1').html(title1 + "<br>");*/
   var extract1 = searchResult["query"]["pages"][0]["extract"];
    $('#extract1').html(extract1 + "<br>");
  // alert(resultCount);
    //alert(title);
  }
  
}) 
};
