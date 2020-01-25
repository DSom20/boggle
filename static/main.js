$(function () { // on page load

  $("#form").on("submit", async function (event) {
    event.preventDefault();
    let value = $("#guess").val();
    let response = await axios.post("/", { guess: value });
    let response_text = response.data.result;
    $("#result_message").text(response_text);
    $("#result_message").show();

    trackCurrentGameScore(response_text, value);
  })

  function trackCurrentGameScore(response_text, value) {
    let currentScore = +($("#current-score").text());
    if (response_text === "ok") {
      currentScore += value.length;
      $("#current-score").text(currentScore);
    }
  }

  let timer = setInterval(function () {
    let secondsLeftText = $("#seconds-left");
    let secondsLeftNum = +(secondsLeftText.text());
    secondsLeftNum--;
    secondsLeftText.text(secondsLeftNum);
    if (secondsLeftNum <= 0) {
      handleEndGame(); //helper function
    }
  }, 1000);

  function handleEndGame() {
    clearInterval(timer);

    (async function () {
      let currentScore = +($("#current-score").text());

      await axios.post('/endgame', { currentScore: currentScore });
    })();

  }

})






