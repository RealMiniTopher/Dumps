let points = 0
let number = 1
function AddPoints() {
  points += number
  document.getElementById("demo").innerHTML = points;
  if (points > 10){
  number = 2
} 
if (points > 100){
  number = 5
} 
if (points > 1000){
  number = 50
} 
if (points > 10000){
  number = 500
} 
if (points > 100000){
  number = 5000
} 
}
const setBg = () => {
  const randomColor = Math.floor(Math.random()*16777215).toString(16);
  document.body.style.backgroundColor = "#" + randomColor;
}

genNew.addEventListener("click", setBg);
setBg();
