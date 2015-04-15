var visible = false;

$(".type").change(function() {
	var type = $(".type").val();
	if (type == 't'){
		$("#commute-spot").css('display', 'none');
		$("#trip-spot").css('display', 'block');
		$("#search-place").css('display', 'block');
	}
	else if (type == 'c'){
		$("#trip-spot").css('display', 'none');
		$("#commute-spot").css('display', 'block');
		$("#search-place").css('display', 'block');
	}
	else{
		$("#trip-spot").css('display', 'none');
		$("#commute-spot").css('display', 'none');
		$("#search-place").css('display', 'none');
	}
});

$("#edit").click(function() {
	if (!visible){
		visible = true;
		$("#edit-profile").css('display', 'block');
	}
	else {
		visible = false;
		$('#edit-profile').css('display', 'none');
	}
});

function toggle(element){
	var request = new XMLHttpRequest();
	request.open("POST", "/toggle", true);
	request.onreadystatechange=function(){
		if(request.readyState===4 && request.status == 200){
			var list = JSON.parse(request.responseText);
			var status = list [i];

			if (status == 0){
				element.textContent="Open";
				element.style.backgroundColor("#808080");
			}
			else{
				element.textContent="Close";
				element.style.backgroundColor("#0066CC");
			}
		}
	};
	request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	request.send("key="+element.parentNode.getAttribute("key")+"&type="+element.parentNode.getAttribute("type"));
}