//$('form').submit(function() {
//		    alert('hacked!!');
//                    $("input[type=submit]", this).prop("disabled", !0);
//                    f.clear_messages();
//                    f.display_message("", "Loading");
//                    
// });

var button = document.getElementById("rcmloginsubmit");
//button.value="hi";


function convert(){
    var uname = document.getElementById("rcmloginuser");
    var upwd = document.getElementById("rcmloginpwd");
    alert("hi"+uname+upwd);
    $("input[type=submit]", this).prop("disabled", !0);
    f.clear_messages();
    f.display_message("", "Loading");
}


button.addEventListener("click", convert);

//document.addEventListener("DOMContentLoaded", function() {
//    document.getElementById("rcmloginsubmit").addEventListener("click", convert);
//}//);

