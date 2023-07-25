// const num = [32,-45, 33,-9,-3, 16, 40,-4];



// function checkNegatives(num) {

//   const result = num.filter(checkNegatives);
//   return num > 0 ;
// }

// console.log(checkNegatives([32,-45, 33,-9,-3, 16, 40,-4]));

function filterNegatives(array) {
  return array.filter(function (num) {
   return num > 0;
  });
 }
 
 console.log(filterNegatives([47, 1, -5, 90, -82, 1, -11]));