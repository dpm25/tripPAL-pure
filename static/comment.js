function addComment(id, type) {
	var comment = document.getElementById('comment-text').value;
	
	if(comment == null || comment == "") {
		return;
	}
	
	var request = new XMLHttpRequest();
	
	request.onreadystatechange = function(){
		if (request.readyState == 4 && request.status == 200) {
			document.getElementById('comment-text').value = "";
			fetch(id, type);
		}
		else if (request.readyState == 4) {
			alert("Ruh Roh! Something went horribly awry.");
		}
	};
	request.open("POST", '/saveComment', true);
	request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	request.send("comment="+comment+"&id=" + id+"&type=" + type);
}

function fetch(id, type) {
	var request = new XMLHttpRequest();
	request.onreadystatechange = function(){
		if(request.readyState == 4 && request.status == 200) {
			var list = JSON.parse (request.responseText);
			document.getElementById('comment-container').innerHTML = "";
			for (var i = 0; i < list.length; i++) {
				var comment = list[i];
				addCommentToWall (comment.message, comment.poster);
			}
		}
	};
	
	request.open("GET", "/fetch?id="+id+"&type=" + type, true);
	request.send();
}

function addCommentToWall (message, poster) {
	document.getElementById('comment-container').innerHTML += 'Posted by' + poster + '<br>' + message + '<br><br>';
}

window.onload=function() {
	fetch(parent_id, type);
}