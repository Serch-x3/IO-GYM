$(document).ready(function() {
  startTime()
})

function startTime() {
  var weekday=new Array(7);
  weekday[0]="Lunes";
  weekday[1]="Martes";
  weekday[2]="Miércoles";
  weekday[3]="Jueves";
  weekday[4]="Viernes";
  weekday[5]="Sábado";
  weekday[6]="Domingo";

  var month= new Array(12);
  month[0]="enero";
  month[1]="febrero";
  month[2]="marzo";
  month[3]="abril";
  month[4]="mayo";
  month[5]="junio";
  month[6]="julio";
  month[7]="agosto";
  month[8]="septiembre";
  month[9]="octubre";
  month[10]="noviembre";
  month[11]="diciembre";

  var today = new Date();

  document.getElementById('clock-date-span').innerHTML = weekday[today.getDay()-1] + ' ' + today.getDate() + ' de ' + month[today.getMonth()] + " del " + today.getFullYear()
  var h = today.getHours();
  if (h > 12){
    h -= 12
  }
  if(h < 10){
    h = '0'+ h.toString()
  }
  var m = today.getMinutes();
  var s = today.getSeconds();
  m = checkTime(m);
  s = checkTime(s);
  document.getElementById('clock-hours').innerHTML = h;
  document.getElementById('clock-minutes').innerHTML = m;
  document.getElementById('clock-seconds').innerHTML = s;
  var t = setTimeout(startTime, 500);
}
function checkTime(i) {
  if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
  return i;
}
