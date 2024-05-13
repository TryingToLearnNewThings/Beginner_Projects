let dictionary = JSON.parse(localStorage.getItem('dictionary')) || {};
let randomGermanWord;

function addVocab() {
    dictionary[germanText.value] = englishText.value;

    germanText.value = '';
    englishText.value = '';

    localStorage.setItem('dictionary', JSON.stringify(dictionary));
    render();
}

function render() {
    vocabularyList.innerHTML = '';
    for (let key in dictionary) {
        vocabularyList.innerHTML += `<li class="mdl-list__item">
        <span class="mdl-list__item-primary-content">
        ${key} - ${dictionary[key]}
        </span>
      </li> <hr>`;
    }
}

function nextVocab() {
    let obj_keys = Object.keys(dictionary);
    randomGermanWord = obj_keys[Math.floor(Math.random() * obj_keys.length)];
    word.innerHTML = `${dictionary[randomGermanWord]}?`
}

function compare() {
    if (sample3.value == randomGermanWord) {
        // Richtig!!
        text.innerHTML = 'Richtig!!';
    } else {
        //Falsch
        text.innerHTML = 'Falsch!!';
    }
    sample3.value = '';
    nextVocab();
}