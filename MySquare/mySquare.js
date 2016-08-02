var x = 10;
var y = 10;
var xChange = 10;
var stop = true;
function setup(){
	createCanvas(5000, 500);
}
function draw(){
	background(0,0,255);
	textSize(30);
	fill(90,90,90);
	text("LAWL", x, y, 10, 30);
	x = x + xChange;
	if(x>250 && stop){
		stop = false;
		myButton = document.createElement("button");
		myButton.textContent = "Click!";
		$("body").append(myButton);
		function reverseIt(){
			xChange = xChange * -1;
		}
		$("button").click(reverseIt);
	}
}