//1. calculate the sum of numbers in an array
function sumArray(num){

    let sum = 0 

    for (let i = 0; i < num.length; i++) {
        sum = sum + num[i]
    }
    
    return sum;

}

console.log(sumArray([2,3,4,5,6,7]));


