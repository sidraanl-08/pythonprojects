let target;
let guessInput;
let message = "";
let checkButton, restartButton;

function setup() {
  createCanvas(600, 400);
  target = floor(random(1, 101));

  // Create input box
  guessInput = createInput();
  guessInput.position(250, 200);

  // Check Button
  checkButton = createButton('Check');
  checkButton.position(250, 240);
  checkButton.mousePressed(checkGuess);

  // Restart Button
  restartButton = createButton('Restart');
  restartButton.position(320, 240);
  restartButton.mousePressed(restartGame);
}

function draw() {
  background(100, 150, 255); // sky blue
  fill(255);
  textSize(24);
  textAlign(CENTER);
  text("Guess a number between 1 and 100", width/2, 150);
  text(message, width/2, 300);
}

function checkGuess() {
  let guess = int(guessInput.value());
  if (guess === target) {
    message = "🎉 You guessed it!";
  } else if (guess < target) {
    message = "⬆️ Too low!";
  } else {
    message = "⬇️ Too high!";
  }
}

function restartGame() {
  target = floor(random(1, 101));
  message = "";
  guessInput.value('');
}
