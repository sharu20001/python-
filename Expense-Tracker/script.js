let total = 0;

function addExpense(){

let desc = document.getElementById("desc").value;
let amount = document.getElementById("amount").value;

if(desc === "" || amount === ""){
alert("Enter expense details");
return;
}

let list = document.getElementById("expense-list");

let li = document.createElement("li");

li.innerHTML = desc + " - ₹" + amount;

list.appendChild(li);

total += parseInt(amount);

document.getElementById("total").innerText = total;

document.getElementById("desc").value="";
document.getElementById("amount").value="";
}
