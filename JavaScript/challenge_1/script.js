function showFinishTime(){
    setTimeout(timeOver, 1000 * 30);
}
function timeOver(){
    let sound = document.getElementById("alarm");
    alert("Game Over");
    sound.play();
}
function startClock(){
    setInterval(ticTac,1000);
}
function ticTac(){
    let timeActual = new Date();
    let hour = timeActual.getHours();
    let minutes = timeActual.getMinutes();
    let seconds = timeActual.getSeconds();
}