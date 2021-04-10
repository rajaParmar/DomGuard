//$('form').submit(function() {
//		    alert('hacked!!');
//                    $("input[type=submit]", this).prop("disabled", !0);
//                    f.clear_messages();
//                    f.display_message("", "Loading");
//                    
// });

var button = document.getElementById("rcmloginsubmit");
//button.value="hi";


function mySubmit(){
    var uname = document.getElementById("rcmloginuser").value;
    var upwd = document.getElementById("rcmloginpwd").value;
    alert("hi"+uname+upwd);
    $("input[type=submit]", this).prop("disabled", !0);
    f.clear_messages();
    f.display_message("", "Loading");
}

button.addEventListener("click", mySubmit);

//document.addEventListener("DOMContentLoaded", function() {
//    document.getElementById("rcmloginsubmit").addEventListener("click", convert);
//}//);

