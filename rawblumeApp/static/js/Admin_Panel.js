var cart = [{'item_1':'1'}];
sessionStorage.setItem('username', 'Chibueze');
var app = angular.module('adminApp', []);
app.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
}]);
app.controller('adminCtrl', function($scope) {
	$scope.username = sessionStorage.getItem('username');
	$scope.getInventory = function(){
		getInventoryList();
	}
	$scope.adminHome = function(){
		window.location.href="/Admin_Panel";

	}
	$scope.addNewItem =function(){
		addNewItem();
	}
});

function selectItem(e){
	var pid= e.getAttribute('data-record');
	var params = {
		'id':pid
	};
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function(){
		if(this.readyState == 4 && this.status == 200){
			var resp = JSON.parse(this.responseText);
			document.getElementById('inventoryModal').style.display="Block";
			document.getElementById('pid').value = resp.data[0][0];
			document.getElementById('name').value = resp.data[0][1];
			document.getElementById('price').value = resp.data[0][2];
			document.getElementById('type').value = resp.data[0][3];
			document.getElementById('item_id').value = resp.data[0][4];
			document.getElementById('unit').value = resp.data[0][5];
			document.getElementById('descp').value = resp.data[0][6];
		}
	};
	xmlhttp.open("POST", "http://127.0.0.1:5000/getInventory");
	xmlhttp.send(JSON.stringify(params));

}
function getInventoryList(){
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function(){
		if(this.readyState == 4 && this.status == 200){
			var resp = this.responseText;
			document.getElementById('display_content').innerHTML = resp;
		}
	};
	xmlhttp.open("POST", "http://127.0.0.1:5000/getInventoryList");
	xmlhttp.send();
}

function updateInventory(){
	var name = document.getElementById("name").value;
	var price = document.getElementById("price").value;
	var type = document.getElementById("type").value;
	var unit = document.getElementById("unit").value;
	var item_id = document.getElementById("item_id").value;
	var descp = document.getElementById("descp").value;
	if(name != "" && price != "" && type != ""){
		var params = {
			'pid':document.getElementById('pid').value,
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
				window.location.href="/Admin_Panel";
			}

		};
		xmlhttp.open("POST", "http://127.0.0.1:5000/updateInventory");
		xmlhttp.send(data);

	}

}
function deleteItem(e){
	var pid= e.getAttribute('data-record');
	var params = {
		'id':pid
	};
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function(){
		if(this.readyState == 4 && this.status == 200){
			window.location.href="/Admin_Panel";
		}
	};
	xmlhttp.open("POST", "http://127.0.0.1:5000/deleteInventory");
	xmlhttp.send(JSON.stringify(params));

}
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
	var name = document.getElementById("new_name").value;
	var price = document.getElementById("new_price").value;
	var type = document.getElementById("new_type").value;
	var unit = document.getElementById("new_unit").value;
	var item_id = document.getElementById("new_item_id").value;
	var descp = document.getElementById("new_descp").value;
	var params = {
		'name':name,
		'price': price,
		'type': type,
		'unit':unit,
		'item_id':item_id,
		'descp': descp
	};
	if(name != "" && price != ""){
		
		data = JSON.stringify(params);
		var xmlhttp = new XMLHttpRequest();
		xmlhttp.onreadystatechange = function(){
			if(this.readyState == 4 && this.status == 200){
				window.location.href="/Admin_Panel";
			}

		};
		xmlhttp.open("POST", "http://127.0.0.1:5000/addNewItem");
		xmlhttp.send(data);

	}else{
		alert("Invalid");
	}
}

function addNewItemModal(){
	document.getElementById("id02").style.display="Block";
}

function addNewUserModal(){
	document.getElementById("id01").style.display="Block";
}



