
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