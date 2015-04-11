var autocomplete, placeSearch;

var componentForm = {
  street_number: 'short_name',
  route: 'long_name',
  locality: 'long_name',
  administrative_area_level_1: 'short_name',
  country: 'long_name',
  postal_code: 'short_name'
};

var componentFormCommute = {
  street_number1: 'short_name',
  route1: 'long_name',
  locality1: 'long_name',
  administrative_area_level_11: 'short_name',
  country1: 'long_name',
  postal_code1: 'short_name'
};

function initialize(){
	autocomplete = new google.maps.places.Autocomplete(
      /** @type {HTMLInputElement} */(document.getElementById('autocomplete')),
      { types: ['geocode'] });
	  
	google.maps.event.addListener(autocomplete, 'place_changed', function() {
		fillInAddress();
		fillInAddressCommute();
	});
}

function geolocate() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var geolocation = new google.maps.LatLng(
          position.coords.latitude, position.coords.longitude);
      var circle = new google.maps.Circle({
        center: geolocation,
        radius: position.coords.accuracy
      });
      autocomplete.setBounds(circle.getBounds());
    });
  }
}

function fillInAddress() {
  // Get the place details from the autocomplete object.
  var place = autocomplete.getPlace();
  
  for (var component in componentForm) {
    document.getElementById(component).value = '';
    document.getElementById(component).disabled = false;
  }

  // Get each component of the address from the place details
  // and fill the corresponding field on the form.
  for (var i = 0; i < place.address_components.length; i++) {
    var addressType = place.address_components[i].types[0];
    if (componentForm[addressType]) {
      var val = place.address_components[i][componentForm[addressType]];
      document.getElementById(addressType).value = val;
    }
  }
}

function fillInAddressCommute() {
  // Get the place details from the autocomplete object.
  var place = autocomplete.getPlace();
  for (var component in componentFormCommute) {
    document.getElementById(component).value = '';
    document.getElementById(component).disabled = false;
  }

  // Get each component of the address from the place details
  // and fill the corresponding field on the form.
  for (var i = 0; i < place.address_components.length; i++) {
    var addressType = place.address_components[i].types[0];
	commuteType = addressType + "1";
    if (componentFormCommute[commuteType]) {
      var val = place.address_components[i][componentForm[addressType]];
      document.getElementById(commuteType).value = val;
    }
  }
}