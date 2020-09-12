var modalSeconds = 3600;
var alertSeconds = modalSeconds - 30;


// Set the timer


window.setTimeout(function(){
    $('#expiredSessionAlert').modal('hide')
      $('#expiredSession').modal('show');
    }, modalSeconds*1000);

window.setTimeout(function(){
      $('#expiredSessionAlert').modal('show');
      countdown();
    }, alertSeconds*1000);

function countdown(){
  var timeleft = 30;
  var downloadTimer = setInterval(function(){
  timeleft--;
  document.getElementById("secondsLeftSpan").textContent = timeleft;
  if(timeleft <= 0)
      clearInterval(downloadTimer);
  },1000);
}
