let timeOver;
let timeInterval;

function showFinishTime(){
    timeOver = setTimeout(timeFinish, 1000*30);
    timeInterval = setInterval(ticTac,1000);

    document.getElementById("countdown").textContent = 30;
}
function ticTac(){
    let time = document.getElementById("countdown").textContent;
    document.getElementById("countdown").textContent = time -1;
}
function timeFinish(){
    clearInterval(timeInterval);
    document.getElementById("countdown").textContent = 0;
    document.getElementById("alarm").play();
    alert("Game Over:  time is finish, Try Again");
}
function finish(){
    clearTimeout(timeOver);
    clearInterval(timeInterval);
    let date = new Date();
    let answer1 = document.getElementById("Answer_1").value;
    let answer2 = document.getElementById("Answer_2").value;
    let answer3 = document.getElementById("Answer_3").value;
    let answer4 = document.getElementById("Answer_4").value;
    let answer5 = document.getElementById("Answer_5").value;

    let message = `${date.toLocaleDateString("es-Es")}
    \n 1: ${answer1}\n 2: ${answer2}\n 3: ${answer3}\n 4: ${answer4}\n 5: ${answer5}`;
    alert(message);
}
function tryAgain(){
    location.reload();
}