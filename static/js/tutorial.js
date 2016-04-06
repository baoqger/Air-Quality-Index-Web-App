/* Sample function - not called */
function getWeather() {
    var city_name = $("#city").val();
	$.get("/AQI_Analysis", {target_city:city_name},function(data,status){
		res = JSON.parse(data);
		$('.jumbotron').html('<h2>' + 'Air Quality Index: ' + res['aqi'] + '</h2>' );
		// google map part
		var myLatLng = {lat: res['lat'], lng: res['lon']};

        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 4,
          center: myLatLng
        });

        var marker = new google.maps.Marker({
          position: myLatLng,
          map: map,
          title: 'Hello World!'
        });

		//show all
		$('.container').show();
	});
}
