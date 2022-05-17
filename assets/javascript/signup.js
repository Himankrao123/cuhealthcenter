function validateForm() {
    var x = document.forms["form"]["password"].value;
    var y = document.forms["form"]["password2"].value;
    if (x !== y){
        alert("Passsword should match!\n");
        return false;
    }
    if (x == y) {
        if (x.length<8){
            alert("Password must be greater than 8 digits.");
            return false;
        }
        return true;
      }
  }