// https://www.freecodecamp.org/challenges/title-case-a-sentence
// -------------------------------------------------------------

// FIRST VERSION
// -------------------------------------------------------------
function titleCase(str) {
  str = str.toLowerCase();
  var words = str.split(' '),
      fixedWords = [],
      letters;
  for(var n = 0; n < words.length; n++){
    letters = words[n].split('');
      letters[0] = letters[0].toUpperCase();
    fixedWords[n] = letters.join('');
  }
  fixedStr = fixedWords.join(' ');
  return fixedStr;
}
titleCase("I'm a little tea pot"); // I'm A Little Tea Pot

// SECOND VERSION
// -------------------------------------------------------------
function titleCase(str) {
  str = str.toLowerCase();
  var words = str.split(' ');
  var fixedWords = words.map(function(word){
    return word.replace(word.charAt(0),word.charAt(0).toUpperCase());
  });
  fixedStr = fixedWords.join(' ');
  return fixedStr;
}
titleCase("I'm a little tea pot"); // I'm A Little Tea Pot
