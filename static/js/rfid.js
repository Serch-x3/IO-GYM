//RFID input validator, when its value reachs 10, the form will be sent automatically
function checkRFID(input){
  if(input.value.length == 10){
    input.form.submit();
  }
}


//Set this function as onclick attribute to those buttons made for browsers, id parameter is a string of the id of the input for rfid
function focusRFIDInput(id){
  focus = setTimeout(function(){
    document.getElementById(id).focus();
  }, 20);
}
