function processLogin(){
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function(){
		if(this.readyState == 4 && this.status == 200){
			console.log(this.responseText);
			document.getElementById('centered').style.display="None";
		}

	};
	xmlhttp.open("GET", "http://rawblume.com/processLogin");
	xmlhttp.send();

}