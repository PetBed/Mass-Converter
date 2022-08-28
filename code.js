const types = ["Tonne", "Kilogram", "Gram", "Milligram", "Microgram", "Imperial Ton", "US Ton",  "Stone", "Pound", "Ounce"];
const formula = [1000000, 1000, 1, 0.001, 0.00001, 1016000, 907200, 6350, 453.6, 28.35]

const leftCon = document.getElementById("left-convert");
const rightCon = document.getElementById("right-convert");
const leftInp = document.getElementById("left-input");
const rightInp = document.getElementById('right-input');

var option
function addOptions(id) {
    types.forEach((type) => {
        option += "<option>" + type + "</option>";
    })
    id.innerHTML = option;
    option = "";
}
addOptions(leftCon);
addOptions(rightCon); 
/* function addOptions(id) {
    var option = document.createElement("option")
    types.forEach((type) => {
        id.add(option);
        option.text = type;
    })
}
addOptions(leftCon); */

var lastLeft;
var lastRight;
var lastConLeft;
var lastConRight;
setInterval(() => {
    var conLeft = formula[types.indexOf(leftCon.value)]
    var conRight = formula[types.indexOf(rightCon.value)]
    if (lastConLeft != conLeft) {
        lastConLeft = conLeft;
        leftInp.value = rightInp.value*conRight/conLeft;
        lastRight = rightInp.value;
        lastLeft = leftInp.value;
    }
    if (lastConRight != conRight) {
        lastConRight = conRight;
        rightInp.value = leftInp.value*conLeft/conRight;
        lastLeft = leftInp.value;
        lastRight = rightInp.value;
    }
    if(lastLeft != leftInp.value) {
        rightInp.value = leftInp.value*conLeft/conRight;
        lastRight = rightInp.value;
        lastLeft = leftInp.value;
    }
    if(lastRight != rightInp.value) {
        leftInp.value = rightInp.value*conRight/conLeft;
        lastLeft = leftInp.value;
        lastRight = rightInp.value;
    }
}, 30);