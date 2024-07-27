const questionsHelper = [
  "What type of help can you provide?",
  "How much time can you commit?",
  "Are there any specific items or resources you can provide?",
  // Add 7 more questions
];

const questionsHelpee = [
  "What kind of help do you need?",
  "How many people are in your household?",
  "Do you have any special requirements or needs?",
  // Add more questions and resource recommendations
];

function setupChatBot(questions) {
  const chatBotDiv = document.getElementById("chatBot");
  chatBotDiv.innerHTML =
    '<div id="chatBox"></div><input id="userInput" type="text" placeholder="Type your answer here..."><button id="sendBtn">Send</button>';

  let currentQuestionIndex = 0;
  const chatBox = document.getElementById("chatBox");
  const userInput = document.getElementById("userInput");
  const sendBtn = document.getElementById("sendBtn");

  function askQuestion() {
    if (currentQuestionIndex < questions.length) {
      chatBox.innerHTML += `<p><strong>Chatbot:</strong> ${questions[currentQuestionIndex]}</p>`;
      currentQuestionIndex++;
    } else {
      chatBox.innerHTML += `<p><strong>Chatbot:</strong> Thank you for your responses!</p>`;
      // Handle end of conversation here, possibly sending data to the server
    }
  }

  sendBtn.addEventListener("click", function () {
    const userResponse = userInput.value;
    chatBox.innerHTML += `<p><strong>You:</strong> ${userResponse}</p>`;
    userInput.value = "";
    askQuestion();
  });

  // Start the conversation
  askQuestion();
}

window.onload = function () {
  if (window.location.pathname === "/helper") {
    setupChatBot(questionsHelper);
  } else if (window.location.pathname === "/helpee") {
    setupChatBot(questionsHelpee);
  }
};
