function processLogin(){
	var username = document.getElementById("username").value;
	var password = document.getElementById("password").value;
	var params = {
		'username':username,
		'password':password
	};
	data = JSON.stringify(params);

	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function(){
		if(this.readyState == 4 && this.status == 200){
			console.log(this.responseText);
			document.getElementById('centered').style.display="None";
		}

	};
	xmlhttp.open("POST", "http://rawblume.com/processLogin");
	xmlhttp.send(data);

}