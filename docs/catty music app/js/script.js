
var months = [January, February, March, April, May, June, July, August, September, October, November, December];
var days = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday];

var today, year, month, day, date;
var num = 4;
today = new Date();
year = today.getFullYear();
month = today.getMonth();
day = today.getDay();
date = today.getDate();

var yearEl = document.getElementsByTagName('p')[0];
yearEl.innerText = num;
var dateEl = document.getElementById('date');
dateEl.innerHTML = 'fuck love';
//dateEl.innerHTML = days[day] + '.' + date + '.' + months[month] + '.' + year;
