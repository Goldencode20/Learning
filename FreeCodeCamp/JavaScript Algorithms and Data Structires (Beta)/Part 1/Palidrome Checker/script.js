const userInput = document.getElementById('text-input');
const checkButton = document.getElementById('check-btn');
const result = document.getElementById('result');

function checkPaliddrome() {
    if (userInput.value === undefined || userInput.value == null || userInput.value.length <= 0) {
        alert("Please input a value");
    }

    let userInputCleaned = userInput.value;
    let reversedInput = userInput.value.split("").reverse().join("");
    const regex = /[^a-zA-Z0-9]/g;
    userInputCleaned = userInputCleaned.replace(regex, '');
    userInputCleaned = userInputCleaned.toLowerCase();
    reversedInput = reversedInput.replace(regex, '');
    reversedInput = reversedInput.toLowerCase();

    if (userInputCleaned === reversedInput) {
        result.innerHTML = `${userInput.value} is a palindrome`;
    } else {
        result.innerHTML = `${userInput.value} is not a palindrome`;
    }
    result.removeAttribute('hidden');
}

checkButton.addEventListener("click", checkPaliddrome);
