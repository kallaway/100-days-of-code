// https://www.freecodecamp.org/challenges/check-for-palindromes

function palindrome(str) {
  str = str.replace(/[\W_]/g,"").toLowerCase();
  return str == str.split("").reverse().join("");
}
palindrome("Was it Eliot's toilet I saw?"); // true
