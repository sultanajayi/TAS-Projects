// const num = [2,3,4,5,7,6,7]

// num.sort();
// num.reverse();

// console.log(num)

//  Sort an array of NUMBERS in DESC order
function sortNumArray(numArray) {
    function compare(a, b) {
     return a - b;
    }
    const sorted = numArray.sort(compare);
    return sorted.reverse();
   }
   
   console.log(sortNumArray([30, 400, 3, 19, 73, 1003, 201, 8]));