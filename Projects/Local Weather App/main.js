$(document).ready(function() {

  // Only change code below this line.
  navigator.geolocation.getCurrentPosition(function(position) {
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;
    var murl = "http://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon + "&appid=97bfe2740a87cbc32142b5a1c872564f";

    //alert(murl);
    $.ajax({
      url: murl,
      dataType: 'jsonp',
      success: function(openweathermap) {
        var icon = openweathermap["weather"][0]["icon"]; 
        var iconUrl = "http://openweathermap.org/img/w/" + icon + ".png";
        var weather = openweathermap["weather"][0]["main"];
        $('#weatherFeed').html(weather + "<br>");
        var celcius = openweathermap["main"]["temp"] - 273.15;
        var fahreneit = celcius * 1.8 + 32
        // var newCelcius = parseInt(celcius)– 273.15;
        $('#iconImg').html("<img src='" + iconUrl  + "'>")
        $('#celciusFeed').html(Math.round(celcius) + " °C" + "<br>" );
        $('#fahreneitFeed').html(Math.round(fahreneit) + " °F" + "<br>" );
        
  
      }
    
      
    });

    
  });

});
function changeDegree(){
  $('#celciusFeed').toggle();
  $('#fahreneitFeed').toggle();
}
