// program to count the number of vowels in a string

// defining vowels
// initialize count
 // loop through string to test if each character is a vowel
 // return number of vowels
 // take input  prompt('Enter a string: ')

 
function countVowels(string) {
    const vowels = ["a", "e", "u", "i", "o"];
    let numberOfVowels = 0;
   
    for (let i = 0; i < string.length; i++) {
     if (vowels.includes(string[i].toLowerCase())) {
      numberOfVowels++;
     }
    }
    return numberOfVowels;
   }
   
   console.log(countVowels("Nigeria"));

//    const vowels = ["a", "e", "i", "o", "u"]

// function countVowel(str) {
//      let count = 0;
//  for (let letter of str.toLowerCase()) {
//         if (vowels.includes(letter)) {
//             count++;
//         }
//     }
//     return count
// }
// const string = "Hello World,we are here"
// const result = countVowel(string);
// console.log(countVowel(string));


 