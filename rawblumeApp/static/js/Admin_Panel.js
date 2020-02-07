var cart = [{'item_1':'1'}];
sessionStorage.setItem('totalCartItem', cart.length);
sessionStorage.setItem('username', 'Chibueze');
var app = angular.module('adminApp', []);
app.controller('adminCtrl', function($scope, $http) {
	$scope.username = sessionStorage.getItem('username');
	$scope.totalCartItem = sessionStorage.getItem('totalCartItem');
});


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
			document.getElementById('main_container').style.display="Block";
			alert(this.responseText);
		}

	};
	xmlhttp.open("POST", "http://rawblume.com/processLogin");
	xmlhttp.send(data);

}
function addNewItem(){
	var name = document.getElementById("name").value;
	var price = document.getElementById("price").value;
	var type = document.getElementById("type").value;
	var unit = document.getElementById("unit").value;
	var item_id = document.getElementById("item_id").value;
	var descp = document.getElementById("descp").value;
	if(name != "" && price != "" && type != ""){
		var params = {
			'name':name,
			'price': price,
			'type': type,
			'unit':unit,
			'item_id':item_id,
			'descp': descp
		};
		data = JSON.stringify(params);
		var xmlhttp = new XMLHttpRequest();
		xmlhttp.onreadystatechange = function(){
			if(this.readyState == 4 && this.status == 200){
				console.log(this.responseText);
				alert(this.responseText);
			}

		};
		xmlhttp.open("POST", "http://rawblume.com/addNewItem");
		xmlhttp.send(data);

	}
}

function addNewItemModal(){
	document.getElementById("id02").style.display="Block";
}

function addNewUserModal(){
	document.getElementById("id01").style.display="Block";
}



