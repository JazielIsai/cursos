//Create references to the input elements we wish to validate
var username = document.getElementById('name');
var emailid = document.getElementById('email');

function checkData() {
    //Check if username field is empty
    if(username.value == "") {
        alert("Please enter the name");
        username.focus(); //The fname.focus() statement is used to bring the input focus back to the element where we found a problem, in this case, name.
        return false;
    }
    //Check if emailid field is empty
    if(emailid.value == ""){
        alert("Please enter the email");
        emailid.focus();
        return false;
    }
    alert('Form validation is successful');
    return true;
}