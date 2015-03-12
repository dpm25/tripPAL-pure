
function changeForm(type){
	if (type.value == 't') {
		document.getElementById('form-spot').innerHTML = '\
			Enter the trip name: <br> \
			<input type = "text" name = "name"><br><br> \
			\
			Enter your original location: <br> \
			<label>City&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</label> \
			<input type = "text" name = "origin_city">&nbsp&nbsp\
			<label>State&nbsp&nbsp&nbsp&nbsp&nbsp</label><input type = "text" name = "origin_state"><br>\
			<label>Zipcode&nbsp&nbsp&nbsp&nbsp&nbsp</label><input type = "text" name = "origin_zip"><br><br>\
			\
			Enter your destination: <br>\
			<label>City&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</label>\
			<input type="text" name="dest_city">&nbsp&nbsp\
			<label>State&nbsp&nbsp&nbsp&nbsp&nbsp</label><input type="text" name="dest_state"><br>\
			<label>Zipcode&nbsp&nbsp&nbsp&nbsp&nbsp</label><input type="text" name="dest_zip"><br><br>\
			\
			Enter your contact information (email or phone number): <br>\
			<input type="text" name = "contactInfo"><br><br>\
			\
			Describe the nature of your trip:<br>\
			<textarea name = "description" rows = "10" cols = "50" onclick="this.focus();this.select()">Enter description here.</textarea> <br><br>\
			<input type = "submit" value = "Submit trip"><br>';
	}
	else if (type.value == 'c') {
		document.getElementById('form-spot').innerHTML = '\
			Enter the trip name: <br> \
			<input type = "text" name = "name"><br><br> \
			\
			Enter your original location: <br> \
			<label>City&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</label> \
			<input type = "text" name = "origin_city">&nbsp&nbsp\
			<label>State&nbsp&nbsp&nbsp&nbsp&nbsp</label><input type = "text" name = "origin_state"><br>\
			<label>Zipcode&nbsp&nbsp&nbsp&nbsp&nbsp</label><input type = "text" name = "origin_zip"><br><br>\
			\
			Enter your destination: <br>\
			<label>City&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</label>\
			<input type="text" name="dest_city">&nbsp&nbsp\
			<label>State&nbsp&nbsp&nbsp&nbsp&nbsp</label><input type="text" name="dest_state"><br>\
			<label>Zipcode&nbsp&nbsp&nbsp&nbsp&nbsp</label><input type="text" name="dest_zip"><br><br>\
			\
			Monday: <input type = "checkbox" name = "monday" value = "monday">\
			Tuesday: <input type = "checkbox" name = "tuesday" value = "tuesday">\
			Wednesday: <input type = "checkbox" name = "wednesday" value = "wednesday">\
			Thursday: <input type = "checkbox" name = "thursday" value = "thursday">\
			Friday: <input type = "checkbox" name = "friday" value = "friday">\
			Saturday: <input type = "checkbox" name = "saturday" value = "saturday">\
			Sunday: <input type = "checkbox" name = "sunday" value = "sunday"><br><br>\
			Describe the nature of your trip:<br>\
			<textarea name = "description" rows = "10" cols = "50" onclick="this.focus();this.select()">Enter description here.</textarea> <br><br>\
			<input type = "submit" value = "Submit trip"><br>';
	}
	else{
		document.getElementById('form-spot').innerHTML = "";
	}
}