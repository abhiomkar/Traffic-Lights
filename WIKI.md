Browser
-------

navigator.geolocation
navigator.geolocation.getCurrentPosition

	// Example
	navigator.geolocation.getCurrentPosition(function(position){ ... });

position.coords.latitude
position.coords.longitude

Google Maps
-----------

google.maps.Map(map_canvas, options)

options:
- zoom (6, 18, 22...)
- mapTypeId

google.maps.LatLng(latitude, longitude)

	// Example
	var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
	initialLocation = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);
	map.setCenter(initialLocation);
