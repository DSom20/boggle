$("#form").on("submit", async function(event){
  event.preventDefault();
  let value = $("#guess").val();
  let response = await axios.post("/", {guess: value});
  let response_text = response.data.result;
  $("#result_message").text(response_text);
  $("#result_message").show();
})







